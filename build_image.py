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

command = ["docker", "build", "-f", "Dockerfile", "-t", f"thanhvu638/javaweb:v{version}", "/var/lib/jenkins/workspace/java-tomcat"]

result = subprocess.run(command, capture_output=True, text=True)

if result.returncode == 0:
    print("Docker build thành công!")
    print(result.stdout)
else:
    print("Docker build thất bại.")
    print(result.stderr)
