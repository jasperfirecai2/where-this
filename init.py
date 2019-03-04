import subprocess

print("Fetching updates from github")
subprocess.call(['/home/pi/Wedstrijd/GitPull.sh'])
print("Updated from github, loading devices")
import main.py
