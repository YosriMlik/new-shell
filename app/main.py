import os
import subprocess
import sys

# from pathlib import Path
from app.utils import find_executable


def main():
    BUILTIN_COMMANDS = ["exit", "echo", "type", "pwd", "cd"]
    CURENT_DIRECTORY = os.getcwd()

    while True:
        sys.stdout.write("$ ")
        command = input()
        splitted_command = command.split()

        if command == "":
            continue

        if command == "exit":
            break

        elif command.startswith("echo "):
            print(command[5:])

        elif command.startswith("type "):
            if command[5:] in BUILTIN_COMMANDS:
                print(f"{command[5:]} is a shell builtin")
            else:
                result = find_executable(command[5:])
                if result:
                    print(f"{command[5:]} is {result}")
                else:
                    print(f"{command[5:]}: not found")

        elif command == "pwd":
            # Get current directory
            print(CURENT_DIRECTORY)

        elif splitted_command[0] == "cd":
            if len(splitted_command) == 2:
                if splitted_command[1] != " ":
                    if os.path.isdir(splitted_command[1]):
                        CURENT_DIRECTORY = splitted_command[1]
                    else:
                        print(f"cd: {splitted_command[1]}: No such file or directory")
                    # os.chdir(splitted_command[1])
                    # print(splitted_command[1])

        elif find_executable(splitted_command[0]):
            parts = splitted_command  # e.g., ["custom_exe_1234", "alice"]
            cmd_name = parts[0]
            cmd_args = parts[1:]
            subprocess.run([cmd_name] + cmd_args)

        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
