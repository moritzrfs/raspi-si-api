import os
import sys
import time

def create_file(data):
    filename = content = data
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            f.write(content+'\n')
            f.write('Created at: '+time.ctime()+'\n')
            f.close()
            print(f"File {filename} created successfully.")
