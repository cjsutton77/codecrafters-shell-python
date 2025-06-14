import sys
import os
EXIT_STRING = "exit 0"

def main():
        while (True):
            PATH = os.environ.get("PATH").split(":")
            sys.stdout.write("$ ")
            command = input()
            commArr = command.split(' ')
            if (command == EXIT_STRING):
                sys.exit(0)
            elif (commArr[0] == 'echo'):
                commArr.pop(0)
                print(f'{' '.join(commArr)}')
            elif (commArr[0] == 'type'):
                match commArr[1]:
                    case "pwd":
                        print(f'{commArr[1]} is a shell builtin')
                    case "echo":
                        print(f'{commArr[1]} is a shell builtin')
                    case "exit":
                        print(f'{commArr[1]} is a shell builtin')
                    case "type":
                        print(f'{commArr[1]} is a shell builtin')    
                    case _:
                        finder(commArr[1],PATH,True)
            elif (commArr[0] == 'pwd'):
                print(os.getcwd())
            elif (commArr[0] == 'cd'):
                if os.path.isdir(commArr[1]):
                    os.chdir(commArr[1])
                else:
                    print(f'cd: {commArr[1]}: No such file or directory')
                    
            elif finder(commArr[0],PATH,False):
                os.system(command)
            else:
                print(f"{command}: command not found")

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
