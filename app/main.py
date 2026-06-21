import os
import shlex
import subprocess
import sys

from app.utils import find_executable


def main():
    builtin_commands = ["exit", "echo", "type", "cd", "pwd"]

    while True:
        sys.stdout.write("$ ")
        command = input()

        try:
            parts = shlex.split(command)
        except ValueError as e:
            print(f"Error parsing command: {e}")
            continue

        if not parts:
            continue

        cmd_name = parts[0]
        cmd_args = parts[1:]

        # 1. exit
        if cmd_name == "exit":
            break

        # 2. echo
        elif cmd_name == "echo":
            print(" ".join(cmd_args))

        # 3. type
        elif cmd_name == "type":
            if not cmd_args:
                continue
            target = cmd_args[0]
            if target in builtin_commands:
                print(f"{target} is a shell builtin")
            else:
                result = find_executable(target)
                if result:
                    print(f"{target} is {result}")
                else:
                    print(f"{target}: not found")

        # 4. cd
        elif cmd_name == "cd":
            if not cmd_args:
                target_path = os.environ.get("HOME", "/")
            else:
                path_string = cmd_args[0]
                if path_string == "~":
                    target_path = os.environ.get("HOME", "/")
                elif path_string.startswith("~/"):
                    home_dir = os.environ.get("HOME", "/")
                    target_path = os.path.join(home_dir, path_string[2:])
                else:
                    target_path = path_string

            try:
                os.chdir(target_path)
            except FileNotFoundError:
                print(f"cd: {cmd_args[0]}: No such file or directory")

        # 5. pwd
        elif cmd_name == "pwd":
            print(os.getcwd())

        # 6. External Commands
        else:
            result = find_executable(cmd_name)
            if result:
                # Runs the binary in `result`, but sets argv[0] to `cmd_name`
                subprocess.run([cmd_name] + cmd_args, executable=result)
            else:
                print(f"{cmd_name}: command not found")


if __name__ == "__main__":
    main()
