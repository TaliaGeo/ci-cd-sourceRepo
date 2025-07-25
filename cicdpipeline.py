from github import Github, Auth
import time 
import subprocess
import os
from dotenv import load_dotenv

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
print("Loaded token:", GITHUB_TOKEN)
if not GITHUB_TOKEN:
    raise ValueError("GITHUB_TOKEN is not set . please recheck your .env file")
REPO_NAME = "TaliaGeo/ci-cd-sourceRepo"
BRANCH_NAME = "master"
CHECK_INTERVAL = 3

auth = Auth.Token(GITHUB_TOKEN)
g = Github(auth=auth)
repo = g.get_repo(REPO_NAME)
lates_commit = repo.get_branch(BRANCH_NAME).commit.sha

print(f"Latest commit on {BRANCH_NAME} branch: {lates_commit}")

while True:
    time.sleep(CHECK_INTERVAL)
    latest_commit = repo.get_branch(BRANCH_NAME).commit.sha
    if latest_commit != lates_commit:
        print(f"New commit detected: {latest_commit}")
        subprocess.run(["bash", "sourcephase.sh"])
        lates_commit = latest_commit
    else:
        print("No new commits detected.")
     
