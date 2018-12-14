import subprocess

print("Fetching updates from github")
subprocess.call(['./GitPull.sh'])
print("Updated from github, loading devices")
import main.py