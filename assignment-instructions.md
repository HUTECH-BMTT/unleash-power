# Hướng Dẫn Nộp Bài Tập Trên GitHub

Xin chào sinh viên,

Dưới đây là hướng dẫn để bạn sử dụng **GitHub CLI** hoặc **GitHub Desktop** để nộp bài tập của mình lên repository cá nhân cho từng tuần.

## 1. Cách Nộp Bài Tập Bằng GitHub CLI

GitHub CLI là công cụ dòng lệnh để tương tác với GitHub. Bạn có thể sử dụng nó để clone repository, commit code và push bài tập của mình.

### Bước 1: Cài Đặt GitHub CLI
- Tải và cài đặt GitHub CLI theo hướng dẫn tại: [https://cli.github.com/](https://cli.github.com/)
- Sau khi cài đặt, mở terminal và chạy lệnh sau để đăng nhập vào tài khoản GitHub của bạn:

    ```bash
    gh auth login
    ```

### Bước 2: Clone Repository
- Bạn sẽ nhận được lời mời (invite) vào repository cá nhân trên GitHub. Chấp nhận lời mời và sau đó clone repository về máy tính bằng lệnh:

    ```bash
    gh repo clone <organization>/<repo-name>
    ```

    Thay `<organization>` bằng tên tổ chức của lớp học (ví dụ: `HUTECH-BMTT`) và `<repo-name>` bằng tên repository cá nhân của bạn (ví dụ: `DTH-123456-NguyenVanA`).

### Bước 3: Tạo Thư Mục Bài Tập
- Vào thư mục tương ứng của tuần hiện tại. Ví dụ, nếu bạn đang làm bài tập tuần 1, hãy di chuyển vào thư mục `Week1/student-work/`:

    ```bash
    cd Week1/student-work/
    ```

- Tạo các file bài tập của bạn trong thư mục này.

### Bước 4: Commit Và Push Bài Tập
- Khi bạn đã hoàn thành bài tập, bạn cần commit và push bài tập lên repository.

    ```bash
    git add .
    git commit -m "Nộp bài tập tuần <X>"
    git push origin main
    ```

    Thay `<X>` bằng số tuần tương ứng (ví dụ: `tuần 1`).

## 2. Cách Nộp Bài Tập Bằng GitHub Desktop

Nếu bạn thích giao diện đồ họa thay vì dòng lệnh, bạn có thể sử dụng GitHub Desktop để nộp bài tập.

### Bước 1: Cài Đặt GitHub Desktop
- Tải và cài đặt GitHub Desktop tại: [https://desktop.github.com/](https://desktop.github.com/)
- Đăng nhập vào GitHub Desktop bằng tài khoản GitHub của bạn.

### Bước 2: Clone Repository
- Sau khi chấp nhận lời mời vào repository cá nhân, mở GitHub Desktop và nhấn **File > Clone repository**.
- Chọn tab **URL**, sau đó nhập URL của repository cá nhân của bạn. Ví dụ:

    ```
    https://github.com/HUTECH-BMTT/DTH-123456-NguyenVanA.git
    ```

- Chọn nơi lưu repository trên máy tính và nhấn **Clone**.

### Bước 3: Thêm Bài Tập
- Mở thư mục repository vừa được clone trên máy tính của bạn.
- Di chuyển đến thư mục tương ứng với tuần hiện tại, ví dụ `Week1/student-work/`, và thêm các tệp bài tập vào đó.

### Bước 4: Commit Và Push Bài Tập
- Quay lại GitHub Desktop, bạn sẽ thấy các thay đổi mà bạn đã thực hiện.
- Nhập mô tả commit, ví dụ: "Nộp bài tập tuần 1", và nhấn **Commit to main**.
- Sau khi commit, nhấn **Push origin** để đẩy các thay đổi lên GitHub.

## 3. Kiểm Tra Bài Tập Trên GitHub

Sau khi đã push bài tập, bạn có thể vào repository trên GitHub để kiểm tra lại bài tập của mình đã được upload thành công hay chưa. Truy cập vào repository qua đường dẫn:

```URL
https://github.com/HUTECH-BMTT/<repo-name>
```

## 4. Lưu Ý

- **Deadline**: Mỗi tuần, bạn phải nộp bài trước khi hết hạn. Hạn nộp bài là **6 ngày sau buổi học**.
- **Thư mục làm bài**: Mỗi bài tập cần được đặt trong thư mục tương ứng của từng tuần. Ví dụ, bài tập tuần 1 phải nằm trong thư mục `Week1/student-work/`.
- **Nội dung commit**: Khi commit, hãy luôn ghi chú rõ ràng nội dung của bài nộp, ví dụ: "Nộp bài tập tuần 1".

Chúc các bạn học tốt!
