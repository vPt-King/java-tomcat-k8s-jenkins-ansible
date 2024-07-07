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
login_command = "docker -u thanhvu638 -p Conbo2chan@".split()
result = subprocess.run(login_command, capture_output=True, text=True)
push_command = f"docker push thanhvu638/javaweb:v{version}".split()
res = subprocess.run(push_command,capture_output=True, text=True)