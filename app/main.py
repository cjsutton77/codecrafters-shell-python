import sys
import os
EXIT_STRING = "exit 0"

def main():
        while (True):
            PATH = os.environ.get("PATH").split(":")
            # path = 
            # Uncomment this block to pass the first stage
            sys.stdout.write("$ ")
            # Wait for user input
            command = input()
            commArr = command.split(' ')
            if (command == EXIT_STRING):
                sys.exit(0)
            elif (commArr[0] == 'echo'):
                commArr.pop(0)
                print(f'{' '.join(commArr)}')
            elif (commArr[0] == 'type'):
                match commArr[1]:
                    case "echo":
                        print(f'{commArr[1]} is a shell builtin')
                    case "exit":
                        print(f'{commArr[1]} is a shell builtin')
                    case "type":
                        print(f'{commArr[1]} is a shell builtin')    
                    case _:
                        found = False
                        for p in PATH:
                            #directoryListing = os.listdir(p)
                            #print(commArr[1],p)
                            if (os.path.isdir(p) and commArr[1] in os.listdir(p)):
                                print(f'{commArr[1]} is {p}/{commArr[1]}')
                                found = True
                                break
                            else: 
                                continue
                        if (not found):
                            print(f'{commArr[1]}: not found') 
            else:
                print(f"{command}: command not found")


if __name__ == "__main__":
    main()
