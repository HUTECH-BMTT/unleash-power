def handle_repository(repo):
    """Handle the operations needed for each repository."""
    reset_issues(repo)
    trigger_ci_workflow(repo)

def trigger_ci_workflow(repo):
    """Trigger a dummy CI workflow by updating the content of an existing dummy file."""
    try:
        contents = repo.get_contents("trigger-ci.txt", ref="main")
        new_content = contents.decoded_content.decode() + "\nTrigger CI workflow update"
        repo.update_file(contents.path, "Trigger CI workflow update", new_content, contents.sha, branch="main")
        print(f"CI workflow triggered in {repo.name}.")
    except Exception as e:
        print(f"Failed to trigger workflow in {repo.name}: {e}")

def reset_issues(repo):
    """Reset the issues in a repository."""
    try:
        issues = repo.get_issues(state="open")
        for issue in issues:
            issue.edit(state="closed")
            print(f"Issue #{issue.number} closed in {repo.name}.")
        
        # Create a new issue to mark the reset
        repo.create_issue(title="Issue reset", body="All previous issues have been closed and reset.")
        print(f"New issue created to mark the reset in {repo.name}.")
    except Exception as e:
        print(f"Failed to reset issues in {repo.name}: {e}")
