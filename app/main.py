import sys

EXIT_STRING = "exit 0"

def main():
        while (True):
            # Uncomment this block to pass the first stage
            sys.stdout.write("$ ")

            # Wait for user input
            command = input()
            if (command == EXIT_STRING):
                break
            commArr = command.split(' ')
            if (commArr[0] == 'echo'):
                commArr.pop(0)
                print(f'{' '.join(commArr)}')
            else:
                print(f"{command}: command not found")


if __name__ == "__main__":
    main()
