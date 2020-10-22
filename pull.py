import subprocess
import time

while True:
	subprocess.run(["git", "pull", "https://github.com/ipratt-code/my-website"], check=True, stdout=subprocess.PIPE).stdout
	print("GIT PULL: done")
	time.sleep(300)