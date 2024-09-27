def handle_repository(repo):
    """Handle the operations needed for each repository."""
    reset_issues(repo)
    trigger_ci_workflow(repo)

def trigger_ci_workflow(repo):
    """Trigger a dummy CI workflow by creating or updating a dummy file."""
    try:
        contents = repo.get_contents("trigger-ci.txt", ref="main")
        repo.update_file(contents.path, "Trigger CI workflow", "This is a dummy file to trigger CI workflow", contents.sha, branch="main")
        print(f"CI workflow triggered in {repo.name}.")
    except Exception as e:
        if e.status == 404:
            repo.create_file("trigger-ci.txt", "Trigger CI workflow", "This is a dummy file to trigger CI workflow", branch="main")
            print(f"CI workflow triggered in {repo.name}.")
        else:
            print(f"Failed to trigger workflow in {repo.name}: {e}")
def reset_issues(repo):
    """Reset the issues in a repository."""
    try:
        issues = repo.get_issues(state="open")
        for issue in issues:
            issue.edit(state="closed")
            print(f"Issue #{issue.number} closed in {repo.name}.")
    except Exception as e:
        print(f"Failed to reset issues in {repo.name}: {e}")
