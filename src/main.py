import pandas as pd
import unidecode
from github_client import init_github_client
from repo_manager import create_repository
from collaborator_manager import add_collaborator
# from repo_handler import handle_repository

def main():
    # Initialize GitHub API client
    g = init_github_client()
    
    # Organization and class name
    org_name = "HUTECH-BMTT"
    org = g.get_organization(org_name)

    # Read the list of students from the CSV file
    students = pd.read_csv('resources/students.csv')

    for index, student in students.iterrows():
        student_id = student['student_id']
        full_name = unidecode.unidecode(student['full_name']).replace(" ", "")
        class_name = student['class_name']
        github_username = student['github_username']
        
        # Create a repository for the student
        repo = create_repository(org, class_name, student_id, full_name)
        
        if repo:
            # Add the student as a collaborator
            add_collaborator(repo, github_username, g)
            # Handle repository-specific actions
            # handle_repository(repo)
        else:
            print(f"Skipping collaborator addition due to repo creation failure for {github_username}.")
        
if __name__ == "__main__":
    main()
