import os
import subprocess
import asyncio
import psutil

async def start_proc(script_name):
    command = ['python3', script_name]
    process = await asyncio.create_subprocess_exec(*command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    asyncio.create_task(process.communicate())

def kill_proc(name):
    python_procs = [p for p in psutil.process_iter(attrs=['pid', 'name']) if p.info['name'] == 'python3']

    called_script_pid = None
    for proc in python_procs:
        cmdline = proc.cmdline()
        if len(cmdline) > 1 and cmdline[1] == 'called_script.py':
            called_script_pid = proc.pid
            break

    if called_script_pid is not None:
        psutil.Process(called_script_pid).kill()
        return True
    else:
        print('Process not found')
        return False

def is_process_running(name):
    python_procs = [p for p in psutil.process_iter(attrs=['pid', 'name']) if p.info['name'] == 'python3']

    called_script_pid = None
    for proc in python_procs:
        cmdline = proc.cmdline()
        if len(cmdline) > 1 and cmdline[1] == name:
            called_script_pid = proc.pid
            break
    if called_script_pid is not None:
        return True
    else:
        return False