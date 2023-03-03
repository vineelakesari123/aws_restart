import os

import subprocess

os.system("ls")

subprocess.run(["ls"])

subprocess.run(["ls","-l"])

subprocess.run(["ls","-l","while-loop.py"])
#Retrieving system information using uname command
command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])
#Retrieving information about disk space
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])
