import os
from github import Github
import subprocess
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

# Thông tin tổ chức và token
GIT_FULL_ACCESS_TOKEN = os.getenv("GIT_FULL_ACCESS_TOKEN")
ORG_NAME = "HUTECH-BMTT"  # Thay bằng tên tổ chức của bạn

# Khởi tạo GitHub client
g = Github(GIT_FULL_ACCESS_TOKEN)
org = g.get_organization(ORG_NAME)

# Đường dẫn để lưu các repositories
BASE_DIR = "./cloned_repos"

# Tạo thư mục gốc nếu chưa có
os.makedirs(BASE_DIR, exist_ok=True)

# Lặp qua tất cả các repositories trong tổ chức
for repo in org.get_repos():
    repo_name = repo.name
    repo_url = repo.clone_url

    # Kiểm tra tên repo để phân loại thư mục
    if "22DTHG3" in repo_name:
        repo_dir = os.path.join(BASE_DIR, "22DTHG3")
    elif "22DTHG5" in repo_name:
        repo_dir = os.path.join(BASE_DIR, "22DTHG5")
    else:
        repo_dir = os.path.join(BASE_DIR, "others")

    # Tạo thư mục cho từng nhóm nếu chưa có
    os.makedirs(repo_dir, exist_ok=True)

    # Clone repository vào thư mục tương ứng
    print(f"Cloning {repo_name} into {repo_dir}")
    subprocess.run(["git", "clone", repo_url, os.path.join(repo_dir, repo_name)])

print("Completed cloning all repositories.")
