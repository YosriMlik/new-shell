import sys, os
from pathlib import Path

def main():
    builtin_commands = ["exit", "echo", "type"]
    EXECUTABLE_EXTENSIONS = ['.exe', '.bat', '.cmd', '.com']

    
    while True:
        sys.stdout.write("$ " )
        command = input()
        if command == "": continue
        if command == "exit": break
        elif command.startswith("echo "): print(command[5:])
        elif command.startswith("type "):
            if(command[5:] in builtin_commands): print(f"{command[5:]} is a shell builtin")
            else : 
                path_val = os.environ.get('PATH')
                GOT_COMMAND = False
                for folder in path_val.split(os.pathsep):
                    try:
                        files = [f for f in Path(folder).iterdir() if f.is_file() and f.suffix in EXECUTABLE_EXTENSIONS]
                    except FileNotFoundError: pass  
                    #print("\n")
                    for file in files:
                        #full_path = folder + "" +file.name
                        #print(file.name[:-4])
                        if command[5:] == file.name[:-4]:
                            print(f"{command[5:]} is {os.path.join(folder, file.name)}")
                            GOT_COMMAND = True
                if not GOT_COMMAND: print(f"{command[5:]}: not found")
                
            #else: print(f"{command[5:]}: not found")
        else: print(f"{command}: command not found")
    pass





if __name__ == "__main__":
    main()
