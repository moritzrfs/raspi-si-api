import subprocess

def run_command(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode == 0:
        print("Command executed successfully:")
        print(result.stdout.decode())
    else:
        print("Error executing command:")
        print(result.stderr.decode())