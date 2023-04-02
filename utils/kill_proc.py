import psutil

def kill_proc(name):
    # Get a list of all running Python processes
    python_procs = [p for p in psutil.process_iter(attrs=['pid', 'name']) if p.info['name'] == 'python3']

    # Find the process ID of the script you want to kill
    called_script_pid = None
    for proc in python_procs:
        cmdline = proc.cmdline()
        if len(cmdline) > 1 and cmdline[1] == 'called_script.py':
            called_script_pid = proc.pid
            break

    # Kill the process if it was found
    if called_script_pid is not None:
        psutil.Process(called_script_pid).kill()
        return True
    else:
        print('Process not found')
        return False