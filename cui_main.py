from db.generator import generate_cheese, generate_milk, generate_bread
from db.backup import backup, restore
from cui_statistics import statistics
from db.repository import ProductsRepository

PR = ProductsRepository()

def start_menu() -> int:
    print("\nSTART MENU", 15 * "-", ">")
    print("0. Exit.")
    print("1. Generate new data.")
    print("2. Make backup.")
    print("3. Drop DB.")
    print("4. Make restore.")
    print("5. Statictics.\n")
    return int(input("Enter the number of action: "))

def start():
    while True:
        action = start_menu()

        if action == 0:
            print("Goodbye, have a good day :)")
            break

        elif action == 1:
            generate_bread()
            generate_milk()
            generate_cheese()

        elif action == 2:
            backup()

        elif action == 3:
            PR.drop()

        elif action == 4:
            restore()

        elif action == 5:
            statistics()

        else:
            print("Choose only available [0-5] actions :)")

if __name__ == '__main__':
    start()