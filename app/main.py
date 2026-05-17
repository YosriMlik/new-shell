import sys


def main():
    builtin_commands = ["exit", "echo", "type"]
    
    while True:
        sys.stdout.write("$ ")
        command = input()
        if command == "exit": break
        if command.startswith("echo "): print(command[5:])
        if command.startswith("type "):
            if(command[5:] in builtin_commands): print(f"{command[5:]} is a shell builtin")
            else: print(f"{command[5:]}: command not found")
        else: print(f"{command}: command not found")
    pass


if __name__ == "__main__":
    main()
