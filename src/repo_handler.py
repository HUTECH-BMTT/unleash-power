def handle_repository(repo):
    """Handle the operations needed for each repository."""
    reset_issues(repo)
    delete_milestones(repo)
    trigger_ci_workflow(repo)
    reset_issue_number_file(repo)

def trigger_ci_workflow(repo):
    """Trigger a dummy CI workflow by updating the content of an existing dummy file."""
    try:
        contents = repo.get_contents("trigger-ci.txt", ref="main")
        new_content = contents.decoded_content.decode() + "\nTrigger CI workflow update"
        repo.update_file(contents.path, "Trigger CI workflow update", new_content, contents.sha, branch="main")
        print(f"CI workflow triggered in {repo.name}.")
    except Exception as e:
        if "404" in str(e):  # If the error is 404 (file not found)
            new_content = "Trigger CI workflow update"
            repo.create_file("trigger-ci.txt", "Create trigger file", new_content, branch="main")
            print(f"Created and triggered CI workflow in {repo.name}.")
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

def delete_milestones(repo):
    """Delete all milestones in a repository."""
    try:
        milestones = repo.get_milestones(state="open")
        for milestone in milestones:
            milestone.delete()
            print(f"Milestone '{milestone.title}' deleted in {repo.name}.")
    except Exception as e:
        print(f"Failed to delete milestones in {repo.name}: {e}")

def reset_issue_number_file(repo):
    """Reset the ISSUE_NUMBER file to 1 in a repository."""
    try:
        issue_number_file_path = ".github/ISSUE_NUMBER"
        new_content = "1"
        try:
            contents = repo.get_contents(issue_number_file_path, ref="main")
            repo.update_file(contents.path, "Reset ISSUE_NUMBER to 1", new_content, contents.sha, branch="main")
        except Exception as e:
            if "404" in str(e):  # If the error is 404 (file not found)
                repo.create_file(issue_number_file_path, "Create ISSUE_NUMBER file", new_content, branch="main")
            else:
                raise e
        print(f"ISSUE_NUMBER file reset to 1 in {repo.name}.")
    except Exception as e:
        print(f"Failed to reset ISSUE_NUMBER file in {repo.name}: {e}")
