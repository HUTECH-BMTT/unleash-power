import os
import pandas as pd
from github import Github

# GitHub token is retrieved from the environment variable
token = os.getenv("GIT_FULL_ACCESS_TOKEN")

# Initialize GitHub API client
g = Github(token)

# Organization name and class name
org_name = "HUTECH-BMTT"
class_name = "22DTHB4"

# Get organization from GitHub
org = g.get_organization(org_name)

# Read the list of students from the CSV file
students = pd.read_csv('students.csv')

for index, student in students.iterrows():
    student_id = student['student_id']
    full_name = student['full_name'].replace(" ", "-")
    github_username = student['github_username']
    
    # Create repository name
    repo_name = f"{class_name}-{student_id}-{full_name}"
    
    # Create repository
    repo = org.create_repo(repo_name, private=True)
    
    # Add student as collaborator
    repo.add_to_collaborators(github_username, permission="admin")
    
    print(f"Repository {repo_name} created for {github_username}")
