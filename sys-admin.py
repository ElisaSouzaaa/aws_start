import os
import subprocess

os.system("ls")

subprocess.run(["ls"])

subprocess.run(["ls","-l"])

subprocess.run(["ls","-l","README.md"])

command = "uname"
commandArgument = "-a"
print(f"Reunindo informações do sistema com o comando: {command} {commandArgument}")
subprocess.run([command, commandArgument])

command = "ps"
commandArgument = "-x"
print(f"Reunindo informações de processos de atividades com o comando: {command} {commandArgument}")
subprocess.run([command, commandArgument])