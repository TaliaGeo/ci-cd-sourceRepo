# CI/CD Inventory Management Pipeline

## Project Overview

This project demonstrates a complete CI/CD pipeline built using:

- Python (for automation and backend logic)
- Bash scripts (for pipeline phases)
- Docker (for containerization)
- GitHub API (for commit monitoring)
- Flask (for the web interface)

It processes a restaurant inventory stored in a `.csv` file, splits it based on quantity thresholds, and displays the data in a user-friendly Flask web application.

---

## Project Structure

ci-cd-project/
│
├── cicdpipeline.py # Monitors GitHub for new commits
├── manage_inventory.py # Processes inventory data
├── sourcephase.sh # Clones updated repo and runs processing
├── buildphase.sh # Builds Docker image
├── deployphase.sh # Runs Docker container
├── app.py # Flask web application
├── Dockerfile # Defines container setup
├── requirements.txt # Python dependencies
├── .env # Stores GitHub token securely
├── templates/ # Flask HTML templates
│ ├── home.html
│ └── inventory.html
├── inventory.csv # Sample inventory data
└── temprory-sourceRepo/ # Temporary folder for cloned repo

---

## Technologies Used

| Tool           | Purpose                          |
|----------------|----------------------------------|
| Python         | Main logic and scripting         |
| PyGithub       | GitHub API interaction           |
| Flask          | Web application framework        |
| Docker         | Containerizing the application   |
| Bash           | Running automation scripts       |
| python-dotenv  | Load environment variables       |

---

## How the Pipeline Works

3 Source Phase
- `cicdpipeline.py` checks for new commits in the GitHub repository using PyGithub.
- When a new commit is detected, it triggers `sourcephase.sh`.
- The repo is cloned into a temporary directory.
- `manage_inventory.py` processes the CSV and creates reports.

2 Build Phase
- `buildphase.sh` builds a Docker image using the `Dockerfile`.
- The image includes the Flask app and all required dependencies.

 3 Deployment Phase
- `deployphase.sh` stops any existing container and runs a new one.
- The Flask app is now running and accessible at `http://localhost:8080`.

---
