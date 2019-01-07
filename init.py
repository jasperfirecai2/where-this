import subprocess

print("Fetching updates from github")
if (subprocess.call(['./GitPull.sh']) != 0):
    print("Updated from github, loading devices")
    import main.py
else:
    print("something went wrong with updating. \n Please try again later")
