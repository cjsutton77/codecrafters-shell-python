import sys
import os
import shlex
import subprocess
EXIT_STRING = "exit 0"

def main():
    while (True):
        PATH = os.environ.get("PATH").split(":")
        sys.stdout.write("$ ")
        command = sys.stdin.readline().strip()
        if not command:
            continue
        executor = shlex.split(command)
        if (command == EXIT_STRING):
            sys.exit(0)
        elif (executor[0] == 'echo'):
            print(' '.join(executor[1:]))
        elif (executor[0] == 'type'):
            match executor[1]:
                case "pwd" | "echo" | "exit" | "type":
                    print(f'{executor[1]} is a shell builtin')
                case _:
                    finder(executor[1], PATH, True)
        elif (executor[0] == 'pwd'):
            print(os.getcwd())
        elif (executor[0] == 'cd'):
            if len(executor) > 1 and executor[1] == '~':
                HOME = os.environ.get("HOME")
                os.chdir(HOME)
            elif len(executor) > 1 and os.path.isdir(executor[1]):
                os.chdir(executor[1])
            else:
                print(f'cd: {executor[1] if len(executor) > 1 else ""}: No such file or directory')
        else:
            # Try to run the command as an executable, even if quoted
            try:
                subprocess.run(executor)
            except FileNotFoundError:
                print(f"{executor[0]}: command not found")
            except Exception as e:
                print(f"Error: {e}")

def finder(command,path,output=True):
    cmd_found = None
    for p in path:
        if (os.path.isdir(p) and command in os.listdir(p)):
            cmd_found = (f'{command} is {p}/{command}')
            found = True
            break
        else: 
            continue
    if cmd_found is not None:
        if output: 
            print(cmd_found)
        return True
    else:
        if output: 
            print(f'{command}: not found')
        return False
    
if __name__ == "__main__":
    main()
