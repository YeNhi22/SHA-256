from flask import Flask, render_template, request, redirect, session, send_from_directory
from flask_socketio import SocketIO, emit, join_room, leave_room
import os, hashlib, uuid

app = Flask(__name__)
app.secret_key = "supersecretkey"
socketio = SocketIO(app, cors_allowed_origins="*")

UPLOAD_FOLDER = "files/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

USER_FILE = "users.txt"
online_users = {}

# ----- Hàm tiện ích -----
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    users = {}
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as f:
            for line in f:
                if ":" in line:
                    username, hashed_pw = line.strip().split(":", 1)
                    users[username] = hashed_pw
    return users

def save_user(username, password):
    with open(USER_FILE, "a") as f:
        f.write(f"{username}:{hash_password(password)}\n")

# ----- Routes chính -----
@app.route("/")
def index():
    if "username" in session:
        return render_template("index.html",
                               username=session["username"],
                               users=list(online_users.keys()))
    return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        users = load_users()
        if username in users and users[username] == hash_password(password):
            session["username"] = username
            return redirect("/")
        return "Sai tên đăng nhập hoặc mật khẩu. <a href='/login'>Thử lại</a>"
    return render_template("login.html")

@app.route("/register", methods=["POST"])
def register():
    username = request.form.get("username")
    password = request.form.get("password")
    confirm = request.form.get("confirm_password")
    users = load_users()

    if username in users:
        return "Tài khoản đã tồn tại. <a href='/login'>Thử lại</a>"
    if password != confirm:
        return "Mật khẩu xác nhận không khớp. <a href='/login'>Thử lại</a>"

    save_user(username, password)
    return redirect("/login")

@app.route("/logout")
def logout():
    username = session.get("username")
    if username in online_users:
        del online_users[username]
    session.pop("username", None)
    return redirect("/login")

@app.route("/download/<file_id>_<filename>")
def download_file(file_id, filename):
    return send_from_directory(UPLOAD_FOLDER, f"{file_id}_{filename}", as_attachment=True)

# ----- WebSocket -----
@socketio.on("connect")
def on_connect():
    if "username" in session:
        username = session["username"]
        join_room(username)
        online_users[username] = True
        emit("update_users", list(online_users.keys()), broadcast=True)
        emit("status", f"Connected as {username}")

@socketio.on("disconnect")
def on_disconnect():
    username = session.get("username")
    if username and username in online_users:
        del online_users[username]
        emit("update_users", list(online_users.keys()), broadcast=True)

@socketio.on("send_file")
def handle_send_file(data):
    sender = session.get("username")
    receiver = data.get("receiver")
    filename = data.get("filename")
    file_bytes = bytes(data.get("filedata"))
    client_sha256 = data.get("sha256")

    if not sender or not receiver or not filename or not file_bytes or not client_sha256:
        emit("error", "Thiếu thông tin gửi file")
        return

    if receiver not in online_users:
        emit("error", f"Người dùng {receiver} không online")
        return

    server_sha256 = hashlib.sha256(file_bytes).hexdigest()
    if client_sha256 != server_sha256:
        print(f"CẢNH BÁO: SHA256 client và server KHÔNG KHỚP! client={client_sha256} server={server_sha256}")

    file_id = str(uuid.uuid4())
    filepath = os.path.join(UPLOAD_FOLDER, f"{file_id}_{filename}")
    with open(filepath, "wb") as f:
        f.write(file_bytes)

    emit("receive_file", {
        "file_id": file_id,
        "filename": filename,
        "sha256": server_sha256,
        "sender": sender
    }, room=receiver)

    emit("status", f"File '{filename}' đã gửi đến {receiver}")

if __name__ == "__main__":
    socketio.run(app, debug=True)
