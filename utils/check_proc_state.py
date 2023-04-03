import psutil

def is_process_running(name):
    for proc in psutil.process_iter(attrs=['name']):
        if proc.info['name'] == name:
            return True
    return False