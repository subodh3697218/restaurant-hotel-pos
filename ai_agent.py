import os
import subprocess

# GitHub Configuration
GITHUB_USERNAME = "subodh3697218"
GITHUB_REPO = "restaurant-hotel-pos"

# Uses an environment variable instead of hardcoding the token
GITHUB_PAT = os.getenv("GITHUB_PAT")

# Set up the local repository path
REPO_PATH = r"C:\Users\DELL\Desktop\ai-agent\restaurant-hotel-pos"

def generate_code():
    """Simulate AI generating code and saving it."""
    new_code = "print('Hello from AI!')"
    with open(os.path.join(REPO_PATH, 'ai_generated_code.py'), 'w') as file:
        file.write(new_code)
    print("✅ Code generated and saved locally.")

def git_commit_push():
    """Automatically commit and push code to GitHub."""
    os.chdir(REPO_PATH)

    # Configure Git credentials for HTTPS authentication
    subprocess.run(["git", "config", "--global", "user.name", GITHUB_USERNAME], check=True)
    subprocess.run(["git", "config", "--global", "user.email", f"{GITHUB_USERNAME}@users.noreply.github.com"], check=True)

    # Set up remote URL with token authentication
    remote_url = f"https://{GITHUB_USERNAME}:{GITHUB_PAT}@github.com/{GITHUB_USERNAME}/{GITHUB_REPO}.git"
    subprocess.run(["git", "remote", "set-url", "origin", remote_url], check=True)

    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "AI generated code update"], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("🚀 Code successfully pushed to GitHub.")
    except subprocess.CalledProcessError as e:
        print("❌ Git push failed:", e)

if __name__ == "__main__":
    generate_code()
    git_commit_push()
