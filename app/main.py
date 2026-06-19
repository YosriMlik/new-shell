import shlex
import subprocess
import sys

from app.utils import find_executable, split_echo


def main():
    builtin_commands = ["exit", "echo", "type"]

    while True:
        sys.stdout.write("$ ")
        command = input()
        if command == "":
            continue
        if command == "exit":
            break
        elif command.startswith("echo "):
            text = command[5:]
            print(" ".join(shlex.split(text)))
        elif command.startswith("type "):
            if command[5:] in builtin_commands:
                print(f"{command[5:]} is a shell builtin")
            else:
                result = find_executable(command[5:])
                if result:
                    print(f"{command[5:]} is {result}")
                else:
                    print(f"{command[5:]}: not found")
        elif command not in builtin_commands:
            parts = shlex.split(command)  # e.g., ["custom_exe_1234", "alice"]
            cmd_name = parts[0]
            cmd_args = parts[1:]
            print(f"Executing external command: {cmd_name}")
            result = find_executable(cmd_name)
            if result:
                subprocess.run([result] + cmd_args)
        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
