import pandas as pd
import unidecode
from github_client import init_github_client
from repo_manager import create_repository
from collaborator_manager import add_collaborator

def main():
    # Khởi tạo GitHub API client
    g = init_github_client()
    
    # Tên tổ chức và lớp học
    org_name = "HUTECH-BMTT"
    org = g.get_organization(org_name)

    # Đọc danh sách sinh viên từ file CSV
    students = pd.read_csv('students.csv')

    for index, student in students.iterrows():
        student_id = student['student_id']
        full_name = unidecode.unidecode(student['full_name']).replace(" ", "")
        class_name = student['class_name']
        github_username = student['github_username']
        
        # Tạo repository cho sinh viên
        repo = create_repository(org, class_name, student_id, full_name)
        
        if repo:
            # Thêm sinh viên làm collaborator nếu repo được tạo thành công
            add_collaborator(repo, github_username, g)
        else:
            print(f"Skipping collaborator addition due to repo creation failure for {github_username}.")
        
if __name__ == "__main__":
    main()
