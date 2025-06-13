import sys

EXIT_STRING = "exit 0"

def main():
        while (True):
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
                        print(f'{commArr[1]}: not found') 
            else:
                print(f"{command}: command not found")


if __name__ == "__main__":
    main()
