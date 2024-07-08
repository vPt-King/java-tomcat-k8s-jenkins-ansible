import subprocess
def read_last_line(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        if lines:
            return lines[-1].strip()
        else:
            return None

file_path = 'version.txt'
last_line = read_last_line(file_path)
version = last_line.split()[1]

command = f"./bash.sh {version}".split()
res = subprocess.run(command)
