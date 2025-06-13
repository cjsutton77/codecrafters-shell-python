import sys

EXIT_STRING = "exit 0"

def main():
        while (command != EXIT_STRING):
            # Uncomment this block to pass the first stage
            sys.stdout.write("$ ")

            # Wait for user input
            command = input()
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
