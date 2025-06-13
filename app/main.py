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
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
