<h2 align="center">ỨNG DỤNG CHIA SẺ FILE AN TOÀN SỬ DỤNG MÃ BẢO MẬT SHA-256</h2>

<p>
Dự án được xây dựng bằng Python và WebSocket, cung cấp giải pháp chia sẻ file bảo mật với khả năng xác thực tính toàn vẹn của dữ liệu sử dụng thuật toán băm SHA-256 (Secure Hash Algorithm 256-bit).
</p>

<h3>Tính năng chính</h3>

<ul>
  <li><strong>Hệ thống chia sẻ file bảo mật:</strong>
    <ul>
      <li>Đăng kí tài khoản</li>li>
      <li>Đăng nhập với tên người dùng để xác thực</li>
      <li>Gửi/nhận file theo thời gian thực qua WebSocket</li>
      <li>Tạo mã băm SHA-256 cho mỗi file được gửi</li>
      <li>Hiển thị danh sách người dùng online</li>
      <li>Giao diện thân thiện với drag & drop</li>
    </ul>
  </li>
  <li><strong>Xác thực tính toàn vẹn dữ liệu:</strong>
    <ul>
      <li>Tự động tính toán mã băm SHA-256 cho file gửi</li>
      <li>Hiển thị mã băm ở cả phía gửi và nhận</li>
      <li>So sánh mã băm để đảm bảo file không bị thay đổi</li>
      <li>Định dạng mã băm dễ đọc và so sánh</li>
    </ul>
  </li>
  <li><strong>Bảo mật nâng cao:</strong>
    <ul>
      <li>Xác thực người dùng trước khi truy cập</li>
      <li>Giới hạn kích thước file tối đa 10MB</li>
      <li>Kiểm tra tính hợp lệ của file trước khi gửi</li>
      <li>Thông báo lỗi chi tiết và xử lý exception</li>
      <li>Copy mã băm nhanh chóng để xác minh</li>
    </ul>
  </li>
</ul>

<h3>Công nghệ sử dụng</h3>

<ul>
  <li>Ngôn ngữ lập trình: Python, JavaScript</li>
  <li>Giao thức real-time: WebSocket (Socket.IO)</li>
  <li>Thuật toán băm: SHA-256 (Web Crypto API)</li>
  <li>Giao diện: HTML5, CSS3 (Tailwind CSS), Font Awesome</li>
  <li>Framework: Flask (Python backend)</li>
  <li>Xử lý file: File API, ArrayBuffer, Uint8Array</li>
</ul>

<h3>Hướng dẫn sử dụng</h3>

<ol>
  <li>Cài đặt thư viện: <code>pip install flask flask-socketio</code></li>
  <li>Khởi chạy server: <code>python app.py</code></li>
  <li>Truy cập ứng dụng qua trình duyệt: <code>http://localhost:5000</code></li>
  <li>Đăng kí tài khoản</li>
  <li>Đăng nhập với tên người dùng</li>
  <li>Chọn người nhận và file muốn gửi</li>
  <li>Hệ thống tự động tạo mã băm SHA-256</li>
  <li>So sánh mã băm giữa người gửi và người nhận để xác minh</li>
</ol>

<h3>Kiến trúc hệ thống</h3>

<p><strong>Quy trình hoạt động:</strong></p>

<ol>
  <li>Client kết nối WebSocket tới server</li>
  <li>Người dùng đăng nhập với tên định danh</li>
  <li>Chọn file và người nhận → tính toán mã băm SHA-256</li>
  <li>File được chuyển đổi thành ArrayBuffer và gửi qua WebSocket</li>
  <li>Server lưu trữ file và chuyển tiếp tới người nhận</li>
  <li>Người nhận xem mã băm để xác minh tính toàn vẹn</li>
  <li>Tải file về với đầy đủ thông tin xác thực</li>
</ol>

<h3>Tính năng bảo mật</h3>

<ul>
  <li><strong>Xác thực tính toàn vẹn:</strong> Mã băm SHA-256 đảm bảo file không bị thay đổi trong quá trình truyền</li>
  <li><strong>Hiển thị trực quan:</strong> Mã băm được chia thành các nhóm dễ đọc với màu sắc phân biệt</li>
  <li><strong>Copy nhanh:</strong> Tính năng copy mã băm một clic để so sánh</li>
  <li><strong>Thông báo realtime:</strong> Cập nhật trạng thái người dùng và file ngay lập tức</li>
  <li><strong>Giao diện thân thiện:</strong> Drag & drop, preview file, thông báo trạng thái</li>
</ul>

<h3>Giao diện ứng dụng</h3>

<p align="center">
  <img src="https://github.com/YeNhi22/FT4012_ATBMMT/blob/main/secure-file-transfer-interface.png" alt="Giao diện gửi file bảo mật" width="600">
</p>

<p align="center">
  <img src="https://github.com/YeNhi22/FT4012_ATBMMT/blob/main/file-hash-verification.png" alt="Xác minh mã băm file" width="600">
</p>

<p>Nguyễn Vũ Yến Nhi - Khoa Công nghệ thông tin, Đại học Đại Nam</p>
