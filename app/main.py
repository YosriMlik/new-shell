import os
import subprocess
import sys
from pathlib import Path

from app.utils import find_executable


def main():
    builtin_commands = ["exit", "echo", "type", "pwd"]

    while True:
        sys.stdout.write("$ ")
        command = input()

        if command == "":
            continue

        if command == "exit":
            break

        elif command.startswith("echo "):
            print(command[5:])

        elif command.startswith("type "):
            if command[5:] in builtin_commands:
                print(f"{command[5:]} is a shell builtin")
            else:
                result = find_executable(command[5:])
                if result:
                    print(f"{command[5:]} is {result}")
                else:
                    print(f"{command[5:]}: not found")

        elif command.startswith("pwd"):
            current_path = Path.cwd()
            print(current_path)

        elif find_executable(command.split()[0]):
            parts = command.split()  # e.g., ["custom_exe_1234", "alice"]
            cmd_name = parts[0]
            cmd_args = parts[1:]
            subprocess.run([cmd_name] + cmd_args)

        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
