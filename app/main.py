import os
import re
import subprocess
import sys
from pathlib import Path

# from pathlib import Path
from app.utils import find_executable


def main():
    BUILTIN_COMMANDS = ["exit", "echo", "type", "pwd", "cd"]
    CURRENT_DIRECTORY = os.getcwd()

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
            print(CURRENT_DIRECTORY)

        elif splitted_command[0] == "cd":
            # print("0")
            if len(splitted_command) == 2:
                # print("1")
                if splitted_command[1] != " ":
                    # print("22")
                    path_string = splitted_command[1]
                    # print("8")
                    if path_string.startswith("/"):
                        try:
                            os.chdir(path_string)
                            # print(path_string + " i s adirectory !")
                            CURRENT_DIRECTORY = path_string
                        except FileNotFoundError:
                            print(f"cd: {path_string}: No such file or directory")

                    elif path_string.startswith("./"):
                        # print("2")
                        y = CURRENT_DIRECTORY + "" + path_string[1:]
                        if os.chdir(y):
                            # print("3")
                            CURRENT_DIRECTORY = y
                    elif (
                        re.search(r"(?:\.\./)+", path_string)
                        and len(path_string) % 3 == 0
                    ):
                        # print(f"Current path : {CURRENT_DIRECTORY}")
                        steps_back = len(path_string) // 3
                        # print(f"Steps back : {steps_back}")
                        new_path_string = str(
                            Path(CURRENT_DIRECTORY).parents[steps_back - 1]
                        )
                        CURRENT_DIRECTORY = new_path_string
                        # print(f"New path : {new_path_string}")

                    else:
                        last_chance = CURRENT_DIRECTORY + "/" + path_string
                        # print(f"Last chance for : {last_chance}")
                        try:
                            # Attempt to change directory
                            os.chdir(last_chance)

                            # If it succeeds, Python moves to the next line automatically

                            # Update your variable to the absolute, verified path
                            CURRENT_DIRECTORY = os.getcwd()

                        except (
                            FileNotFoundError,
                            NotADirectoryError,
                            PermissionError,
                        ):
                            # If it fails, Python jumps straight here
                            pass
                            # print(f"cd: {path_string}: No such file or directory")

            else:
                print(f"cd:{command[2:]}: No such file or directory")
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
