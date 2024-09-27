import os
from github import Github

def create_repository(org, class_name, student_id, full_name):
    # Create repository name
    repo_name = f"{class_name}-{student_id}-{full_name}"
    try:
        # Check if the repository already exists
        repo = org.get_repo(repo_name)
        print(f"Repository {repo_name} already exists.")
        # Add new CI workflow if necessary
        add_ci_workflow_to_repo(repo)
        return repo
    except Exception:
        # If the repository does not exist, create a new repository
        try:
            repo = org.create_repo(repo_name, private=True)
            print(f"Repository {repo_name} created successfully.")
            # Create folder structure
            create_repo_structure(repo)
            return repo
        except Exception as e:
            print(f"Failed to create repository {repo_name}: {e}")
            return None

def create_repo_structure(repo):
    # Create the folder structure and copy the instructions file
    for week in range(1, 7):
        # Create student-work folder
        week_folder = f"Week{week}/student-work/"
        repo.create_file(f"{week_folder}.gitkeep", "create folder structure", "", branch="main")
    # Copy assignment instructions to Readme.md at the root level
    with open('resources/assignment-instructions.md', 'r') as file:
        content = file.read()
        repo.create_file("Readme.md", "Add assignment instructions", content, branch="main")
    # Copy ci-workflow.yml to .github/workflows 
    with open('resources/ci-workflow.yaml', 'r') as file:
        content = file.read()
        repo.create_file(".github/workflows/ci-workflow.yaml", "Add CI workflow", content, branch="main")
    print(f"Folder structure created in {repo.name}.")

def add_ci_workflow_to_repo(repo):
    # Check if the new CI workflow file exists
    file_path = ".github/workflows/ci-mark-submission.yaml"
    try:
        repo.get_contents(file_path, ref="main")
        print(f"{file_path} already exists in {repo.name}. Skipping...")
    except:
        # If the workflow doesn't exist, add it
        with open('resources/ci-mark-submission.yaml', 'r') as file:
            content = file.read()
            repo.create_file(file_path, "Add new CI workflow", content, branch="main")
        print(f"New CI workflow added to {repo.name}.")
