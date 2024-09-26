# Hướng Dẫn Nộp Bài Tập Trên GitHub

Xin chào sinh viên,

Dưới đây là hướng dẫn để bạn sử dụng **GitHub CLI** hoặc **GitHub Desktop** để nộp bài tập của mình lên repository cá nhân cho từng tuần. Quy trình nộp bài yêu cầu bạn tạo branch mới, push code lên branch đó, sau đó merge vào `main`, và cuối cùng comment trong Issue tương ứng.

## 1. Cách Nộp Bài Tập Bằng GitHub CLI

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

### Bước 3: Tạo Branch Mới
- Trước khi bắt đầu làm bài tập, bạn cần tạo một branch mới để lưu trữ bài tập. Tạo branch có tên là `submit-assignment`:

    ```bash
    git checkout -b submit-assignment
    ```

### Bước 4: Thêm Bài Tập
- Vào thư mục tương ứng của tuần hiện tại. Ví dụ, nếu bạn đang làm bài tập tuần 1, hãy di chuyển vào thư mục `Week1/student-work/`:

    ```bash
    cd Week1/student-work/
    ```

- Tạo các file bài tập của bạn trong thư mục này.

### Bước 5: Commit và Push Bài Tập Lên Branch
- Khi bạn đã hoàn thành bài tập, bạn cần commit và push bài tập lên branch `submit-assignment`:

    ```bash
    git add .
    git commit -m "Nộp bài tập tuần <X>"
    git push origin submit-assignment
    ```

    Thay `<X>` bằng số tuần tương ứng (ví dụ: `tuần 1`).

### Bước 6: Merge Branch `submit-assignment` Vào `main`
- Sau khi push, bạn cần merge branch `submit-assignment` vào branch `main` để hoàn tất việc nộp bài:

    ```bash
    gh pr create --base main --head submit-assignment --title "Merge bài tập tuần <X>"
    gh pr merge
    ```

### Bước 7: Comment Trong Issue Tương Ứng
- Sau khi bài tập đã được merge vào `main`, bạn hãy tìm **Issue** tương ứng với tuần hiện tại trên repository của mình. Comment theo yêu cầu của Issue để hoàn tất quá trình nộp bài:

    ```bash
    gh issue comment <issue-number> --body "Bài tập tuần <X> đã được nộp."
    ```

    Thay `<issue-number>` bằng số của Issue tương ứng, và `<X>` bằng số tuần hiện tại.

---

## 2. Cách Nộp Bài Tập Bằng GitHub Desktop

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

### Bước 3: Tạo Branch Mới
- Trước khi bắt đầu làm bài tập, bạn cần tạo một branch mới có tên `submit-assignment` trên GitHub Desktop. Vào menu **Branch > New Branch** và nhập tên branch là `submit-assignment`. Sau đó nhấn **Create Branch**.

### Bước 4: Thêm Bài Tập
- Mở thư mục repository vừa được clone trên máy tính của bạn.
- Di chuyển đến thư mục tương ứng với tuần hiện tại, ví dụ `Week1/student-work/`, và thêm các tệp bài tập vào đó.

### Bước 5: Commit và Push Bài Tập Lên Branch
- Quay lại GitHub Desktop, bạn sẽ thấy các thay đổi mà bạn đã thực hiện.
- Nhập mô tả commit, ví dụ: "Nộp bài tập tuần 1", và nhấn **Commit to submit-assignment**.
- Sau khi commit, nhấn **Push origin** để đẩy branch `submit-assignment` lên GitHub.

### Bước 6: Merge Branch `submit-assignment` Vào `main`
- Vào repository của bạn trên GitHub, tạo một Pull Request để merge branch `submit-assignment` vào `main`. Sau đó nhấn nút **Merge** để hoàn tất quá trình nộp bài.

### Bước 7: Comment Trong Issue Tương Ứng
- Tìm **Issue** tương ứng với tuần hiện tại trên repository của mình. Comment theo yêu cầu của Issue để hoàn tất quá trình nộp bài. 

---

## 3. Lưu Ý

- **Deadline**: Mỗi tuần, bạn phải nộp bài trước khi hết hạn. Hạn nộp bài là **23:59:59, thứ Bảy tuần tiếp theo**.
- **Branch submit-assignment**: Mỗi bài tập cần được push lên branch `submit-assignment` và merge vào `main`.
- **Nội dung commit**: Khi commit, hãy luôn ghi chú rõ ràng nội dung của bài nộp, ví dụ: "Nộp bài tập tuần 1".
- **Comment trong Issue**: Sau khi merge thành công, hãy comment vào Issue tương ứng để hoàn tất quá trình nộp bài.

---

Chúc các bạn học tốt!
