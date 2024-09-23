def add_collaborator(repo, github_username, github_client):
    try:
        # Check if the user exists on GitHub
        user = github_client.get_user(github_username)
        print(f"Adding collaborator: {user.login}")
        
        # Add the user as a collaborator
        repo.add_to_collaborators(github_username, permission="write")
        print(f"Collaborator {github_username} added to repository.")
    except Exception as e:
        print(f"Failed to add collaborator {github_username}: {e}")
