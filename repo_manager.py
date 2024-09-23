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
            return repo
        except Exception as e:
            print(f"Failed to create repository {repo_name}: {e}")
            return None
