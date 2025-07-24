from github import Github
import time 
import subprocess

GITHUB_TOKEN = "hp_5T84OLnz9k6cpUqUqzubvTbLEc9RXL2GAEXy"

REPO_NAME = "TaliaGeo/ci-cd-sourceRepo.git"
BRANCH_NAME = "master"
CHECK_INTERVAL = 3

g = github.Github(GITHUB_TOKEN)
repo = g.get_repo(REPO_NAME)
lates_commit = repo.get_branch(BRANCH_NAME).commit.sha

print(f"Latest commit on {BRANCH_NAME} branch: {lates_commit}")

while True:
    time.sleep(CHECK_INTERVAL)
    latest_commit = repo.get_branch(BRANCH_NAME).commit.sha
    if latest_commit != lates_commit:
        print(f"New commit detected: {latest_commit}")
        subprocess.run(["python3", "cicdpipeline.py"])
        lates_commit = latest_commit
    else:
        print("No new commits detected.")