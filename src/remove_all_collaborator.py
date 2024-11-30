from github import Github
import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

# Load GitHub token từ biến môi trường
GIT_FULL_ACCESS_TOKEN = os.getenv("GIT_FULL_ACCESS_TOKEN")
ORG_NAME = "HUTECH-BMTT"  # Thay bằng tên tổ chức của bạn

# Khởi tạo GitHub client
g = Github(GIT_FULL_ACCESS_TOKEN)

# Lấy tổ chức GitHub
org = g.get_organization(ORG_NAME)

# Duyệt qua tất cả repositories trong tổ chức
for repo in org.get_repos():
    print(f"Processing repository: {repo.name}")

    # Duyệt qua tất cả collaborators trong repository
    for collaborator in repo.get_collaborators():
        # Xóa collaborator trừ khi họ là owner
        if not collaborator.permissions.admin:
            print(f"Removing collaborator: {collaborator.login} from {repo.name}")
            repo.remove_from_collaborators(collaborator)
        else:
            print(f"Skipping owner: {collaborator.login}")

print("Completed removing collaborators.")
