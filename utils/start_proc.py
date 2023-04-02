import os
import subprocess
import asyncio

async def start_proc(script_name):
    command = ['python3', script_name]
    process = await asyncio.create_subprocess_exec(*command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    asyncio.create_task(process.communicate())