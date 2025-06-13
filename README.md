<h2 align="center">ỨNG DỤNG TRUYỀN FILE VỚI CHỮ KÝ SỐ RSA</h2>

<p>
Dự án được xây dựng bằng JavaScript và Web Crypto API, cung cấp giải pháp truyền file bảo mật với khả năng xác thực tính toàn vẹn của dữ liệu sử dụng thuật toán mã hóa RSA và chữ ký số.
</p>

<h3>Tính năng chính</h3>

<ul>
  <li><strong>Hệ thống ký và xác minh file:</strong>
    <ul>
      <li>Tạo cặp khóa RSA 1024-bit, 2048-bit hoặc 4096-bit</li>
      <li>Ký file bằng khóa riêng tư</li>
      <li>Xác minh chữ ký bằng khóa công khai</li>
      <li>Tạo package chứa file đã ký và thông tin xác thực</li>
      <li>Giao diện thân thiện với drag & drop</li>
    </ul>
  </li>
  <li><strong>Xác thực tính toàn vẹn dữ liệu:</strong>
    <ul>
      <li>Tự động tạo chữ ký số SHA-256 với RSA cho file</li>
      <li>Hiển thị thông tin hash và chữ ký</li>
      <li>So sánh để đảm bảo file không bị thay đổi</li>
      <li>Hiển thị kết quả xác minh trực quan</li>
    </ul>
  </li>
  <li><strong>Bảo mật nâng cao:</strong>
    <ul>
      <li>Bảo vệ khóa riêng tư tuyệt đối</li>
      <li>Hỗ trợ nhiều độ dài khóa RSA</li>
      <li>Kiểm tra tính hợp lệ của khóa trước khi sử dụng</li>
      <li>Thông báo lỗi chi tiết khi xác minh thất bại</li>
      <li>Copy khóa và chữ ký dễ dàng</li>
    </ul>
  </li>
</ul>

<h3>Công nghệ sử dụng</h3>

<ul>
  <li>Ngôn ngữ lập trình: JavaScript</li>
  <li>Mã hóa: Web Crypto API</li>
  <li>Thuật toán: RSA, SHA-256</li>
  <li>Giao diện: HTML5, CSS3</li>
  <li>Xử lý file: File API, ArrayBuffer, Base64</li>
</ul>

<h3>Hướng dẫn sử dụng</h3>

<ol>
  <li>Truy cập ứng dụng qua trình duyệt</li>
  <li>Chọn tab "Tạo Khóa" để tạo cặp khóa RSA mới</li>
  <li>Chuyển sang tab "Ký File" để tải lên file và ký bằng khóa riêng tư</li>
  <li>Tải về package file đã ký (.json)</li>
  <li>Gửi package và khóa công khai cho người nhận</li>
  <li>Người nhận sử dụng tab "Xác Minh" để kiểm tra tính xác thực</li>
  <li>Hệ thống sẽ thông báo kết quả xác minh</li>
</ol>

<h3>Kiến trúc hệ thống</h3>

<p><strong>Quy trình hoạt động:</strong></p>

<ol>
  <li>Tạo cặp khóa RSA (public/private)</li>
  <li>Người gửi tải file lên và ký bằng khóa riêng tư</li>
  <li>File được chuyển đổi thành Base64 và tạo chữ ký SHA-256 với RSA</li>
  <li>Lưu thông tin vào package JSON</li>
  <li>Người nhận tải package lên và xác minh bằng khóa công khai</li>
  <li>Hệ thống kiểm tra tính hợp lệ của chữ ký</li>
  <li>Thông báo kết quả và cho phép tải file gốc nếu xác minh thành công</li>
</ol>

<h3>Tính năng bảo mật</h3>

<ul>
  <li><strong>Xác thực mạnh mẽ:</strong> Chữ ký số RSA đảm bảo file không bị giả mạo</li>
  <li><strong>Hiển thị trực quan:</strong> Thông tin khóa và chữ ký được định dạng rõ ràng</li>
  <li><strong>Bảo vệ khóa:</strong> Cảnh báo bảo mật khi sử dụng khóa riêng tư</li>
  <li><strong>Kiểm tra realtime:</strong> Validate khóa ngay khi nhập</li>
  <li><strong>Giao diện thân thiện:</strong> Tab hệ thống, drag & drop, thông báo chi tiết</li>
</ul>

<h3>Giao diện ứng dụng</h3>

<p align="center">
  <img src="Screenshot-2025-06-13-213705.png" alt="Giao diện chính" width="400">
</p>

<p align="center">
  <img src="Screenshot-2025-06-13-213724.png" alt="Tạo khóa RSA" width="400">
</p>

<p align="center">
  <img src="Screenshot-2025-06-13-213806.png" alt="Ký file" width="400">
</p>

<p align="center">
  <img src="Screenshot-2025-06-13-213911.png" alt="Xác minh chữ ký" width="400">
</p>

<p>Nguyễn Vũ Yến Nhi - Khoa Công nghệ thông tin, Đại học Đại Nam</p>
