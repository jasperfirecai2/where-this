import subprocess

print("Fetching updates from github")
subprocess.call(['./GitPull.sh'])
print("Updated from github, starting beacon")
import beacon.py