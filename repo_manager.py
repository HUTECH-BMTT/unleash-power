def create_repository(org, class_name, student_id, full_name):
    # Tạo tên repository
    repo_name = f"{class_name}-{student_id}-{full_name}"
    
    try:
        # Tạo repository
        repo = org.create_repo(repo_name, private=True)
        print(f"Repository {repo_name} created successfully.")
        return repo
    except Exception as e:
        print(f"Failed to create repository {repo_name}: {e}")
        return None
