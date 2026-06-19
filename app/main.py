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

        # Parse the command line into tokens (handles quotes and escapes)
        try:
            tokens = shlex.split(command)
        except ValueError:
            # In case of unbalanced quotes, print an error and continue
            print("error: unbalanced quotes")
            continue

        if not tokens:
            continue

        cmd = tokens[0]
        args = tokens[1:]

        # --- Builtins ---
        if cmd == "exit":
            break

        elif cmd == "echo":
            # echo just prints the arguments separated by a space
            print(" ".join(args))

        elif cmd == "type":
            if not args:
                continue
            target = args[0]
            if target in builtin_commands:
                print(f"{target} is a shell builtin")
            else:
                result = find_executable(target)
                if result:
                    print(f"{target} is {result}")
                else:
                    print(f"{target}: not found")

        else:
            # External command
            executable = find_executable(cmd)
            if executable:
                # ❌ DO NOT PRINT ANYTHING HERE – the tester expects only the program output
                subprocess.run([executable] + args)
            else:
                print(f"{cmd}: command not found")


if __name__ == "__main__":
    main()
