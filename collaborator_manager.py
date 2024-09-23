def add_collaborator(repo, github_username, github_client):
    try:
        # Kiểm tra nếu user tồn tại trên GitHub
        user = github_client.get_user(github_username)
        print(f"Adding collaborator: {user.login}")
        
        # Thêm student như là collaborator
        repo.add_to_collaborators(github_username, permission="write")
        print(f"Collaborator {github_username} added to repository.")
    except Exception as e:
        print(f"Failed to add collaborator {github_username}: {e}")
