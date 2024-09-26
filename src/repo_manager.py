import os
from github import Github

def create_repository(org, class_name, student_id, full_name):
    # Create repository name
    repo_name = f"{class_name}-{student_id}-{full_name}"
    
    try:
        # Check if the repository already exists
        repo = org.get_repo(repo_name)
        print(f"Repository {repo_name} already exists.")
        return repo
    except Exception:
        # If the repository does not exist, create a new repository
        try:
            repo = org.create_repo(repo_name, private=True)
            print(f"Repository {repo_name} created successfully.")
            
            # Create folder structure
            create_repo_structure(repo)
            
            # Set Actions secret
            set_repo_secret(repo, "PAT", os.getenv("GIT_FULL_ACCESS_TOKEN"))
            
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

    print(f"Folder structure created in {repo.name}.")

def set_repo_secret(repo, secret_name, secret_value):
    try:
        repo.create_secret(secret_name, secret_value)
        print(f"Secret {secret_name} set successfully in {repo.name}.")
    except Exception as e:
        print(f"Failed to set secret {secret_name} in {repo.name}: {e}")
