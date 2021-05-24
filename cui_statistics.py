from stat_helper import describe_products, get_linear_regression

def statistics_menu():
    print("\nSTATISTICS MENU", 15 * "-", ">")
    print("0. Exit.")
    print("1. Describe prices of bread.")
    print("2. Describe prices of milk.")
    print("3. Describe prices of cheese.")
    print("4. Regression for price of products.\n")
    return int(input("Enter the number of action: "))

def statistics():
    while True:
        action = statistics_menu()

        if action == 0:
            print("Bye-bye math! -_-")
            break

        elif action == 1:
            describe_products('baguette')
            describe_products('whole-grain')
            print("Don't forget to look at plots :)")

        elif action == 2:
            describe_products('baked')
            describe_products('ordinary')
            print("Don't forget to look at plots :)")

        elif action == 3:
            describe_products('mozzarella')
            describe_products('dorblu')
            describe_products('camambert')
            print("Don't forget to look at plots :)")

        elif action == 4:
            print('Enter what product you want to analyze:')
            print(' - bread -> [baguette, whole-grain]')
            print(' - milk -> [ordinary, baked]')
            print(' - cheese -> [mozzarella, dorblu, camambert]')
            # name = str(input)
            get_linear_regression('mozzarella', 'silpo', '2100-07-23', True)

        else:
            print("Choose only available [0-4] actions :)")

if __name__ == '__main__':
    statistics()