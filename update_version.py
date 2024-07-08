import subprocess
from datetime import datetime
file = open("version.txt", "r")
words = []
while True:
	content=file.readline()
	if not content:
		break
	words.append(content)
file.close()
if len(words) == 0:
	today = datetime.now()
	formatted_date = today.strftime("%d/%m/%Y")
	file = open("version.txt","w")
	file.write(f"thanhvu638/javaweb 1 {formatted_date}")
	file.close()
else:
	curr_version = int(words[len(words)-1].split()[1])
	next_version = curr_version + 1

	today = datetime.now()

	formatted_date = today.strftime("%d/%m/%Y")

	file = open("version.txt","a")
	file.write(f"\nthanhvu638/javaweb {next_version} {formatted_date}")
	file.close()

command = "echo 123 | sudo cp version.txt /home/thanhnga/Documents/learn/ansible/project/javaweb/version.txt"
res = subprocess.run(command)
            