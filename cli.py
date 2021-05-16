def start_menu() -> int:
    print("\nSTART MENU", 15 * "-", ">")
    print("0. Exit.")
    print("1. Regression..")
    print("2. Regression..")
    print("3. ?\n")
    return int(input("Enter the number of action: "))

def start():
    while True:
        action = start_menu()

        if action == 0:
            print("Goodbye, have a good day :)")
            break

        elif action == 1:
            #todo
            break

        elif action == 2:
            # todo
            break

        else:
            print("Choose only available [0-3] actions :)")

if __name__ == '__main__':
    start()