from os import system
import time
import signal

def add():
    data = []
    system('cls')
    name = input("Please enter ID: ")
    data.append(name)
    system('cls')
    size = input("Please enter real size: ")
    while not size.isdigit():
        system('cls')
        size = input("Wrong input! please enter in valid format: ")
    size = int(size)
    data.append(size)
    system('cls')
    foundation_size = input("Please enter foundation size: ")
    while not foundation_size.isdigit():
        system('cls')
        foundation_size = input("Wrong input! please enter in valid format: ")
    foundation_size = int(foundation_size)
    data.append(foundation_size)
    system('cls')
    rooms = input("Pleas enter number of bedrooms:")
    while not rooms.isdigit():
        system('cls')
        rooms = input("Wrong input! please enter in valid format: ")
    rooms = int(rooms)
    data.append(rooms)
    system('cls')
    type = input("Please enter the type of deal (rent, sale, mortage, rent-mortage): ")
    valid_types = ("rent", "sale", "mortage", "rent-mortage")
    while type not in valid_types:
        system('cls')
        type = input("Wrong input! please enter in valid format: ")
    data.append(type)
    system('cls')
    price = input("Please enter the price: ")
    while not price.isdigit():
        system('cls')
        price = input("Wrong input! please enter in valid format: ")
    data.append(price)
    database.append(data)
    system('cls')
    print("House has been successfully added to the database.")
    print("Press Enter to Continue...")
    input()


def delete():
    print()


def edit():
    print()


def report():
    while True:
        system("cls")
        print("1. All")
        print("2. by size")
        print("3. by status")
        print("4. by cost")
        print("5. by room")
        print("6. Back")
        print("===========================")
        x = input("Please enter your choice (1‐6): ")
        header = ['ID', 'Size(real)', 'Size(Foundation)', 'Rooms', 'State', 'Cost(s)']
        if x == '1':
            system("cls")
            print("{: >20} {: >20} {: >20} {: >20} {: >20} {: >23}".format(*header))
            database.sort(key=lambda y: len(y[0]))
            for row in database:
                if row[4] == 'rent' or row[4] == 'mortage' or row[4] == 'rent-mortage':
                    print("{: >20} {: >20} {: >20} {: >20} {: >20} {: >20}$ M".format(*row))
                else:
                    print("{: >20} {: >20} {: >20} {: >20} {: >20} {: >20}$".format(*row))
            print("\nPress enter to continue...")
            input()
        elif x == '2':
            system("cls")
            lower = input("Enter the lower bound: ")
            while not lower.isdigit():
                system('cls')
                lower = input("Wrong input! please enter in valid format: ")
            lower = int(lower)
            system("cls")
            upper = input("Enter the upper bound: ")
            while not upper.isdigit():
                system('cls')
                upper = input("Wrong input! please enter in valid format: ")
            upper = int(upper)
            while lower > upper:
                system("cls")
                print("Upper size must be bigger than the lower size!")
                lower = input("Enter the lower bound: ")
                while not lower.isdigit():
                    system('cls')
                    lower = input("Wrong input! please enter in valid format: ")
                lower = int(lower)
                upper = input("Enter the upper bound: ")
                while not upper.isdigit():
                    system('cls')
                    upper = input("Wrong input! please enter in valid format: ")
                upper = int(upper)
            temp_db = []
            for i in database:
                if i[2] >= lower and i[2] < upper:
                    temp_db.append(i)
            temp_db.sort(key=lambda y: y[2])
            temp_db.reverse()
            system('cls')
            print("{: >20} {: >20} {: >20} {: >20} {: >20} {: >23}".format(*header))
            for row in temp_db:
                if row[4] == 'rent' or row[4] == 'mortage' or row[4] == 'rent-mortage':
                    print("{: >20} {: >20} {: >20} {: >20} {: >20} {: >20}$ M".format(*row))
                else:
                    print("{: >20} {: >20} {: >20} {: >20} {: >20} {: >20}$".format(*row))
            print("\nPress enter to continue...")
            input()
        elif x == '3':
            edit()
        elif x == '4':
            system("cls")
            lower = input("Enter the lower bound: ")
            while not lower.isdigit():
                system('cls')
                lower = input("Wrong input! please enter in valid format: ")
            lower = int(lower)
            system("cls")
            upper = input("Enter the upper bound: ")
            while not upper.isdigit():
                system('cls')
                upper = input("Wrong input! please enter in valid format: ")
            upper = int(upper)
            while lower > upper:
                system("cls")
                print("Upper price must be bigger than the lower price!")
                lower = input("Enter the lower bound: ")
                while not lower.isdigit():
                    system('cls')
                    lower = input("Wrong input! please enter in valid format: ")
                lower = int(lower)
                upper = input("Enter the upper bound: ")
                while not upper.isdigit():
                    system('cls')
                    upper = input("Wrong input! please enter in valid format: ")
                upper = int(upper)
            temp_db = []
            for i in database:
                if i[5] >= lower and i[5] < upper:
                    temp_db.append(i)
            temp_db.sort(key=lambda y: y[5])
            temp_db.reverse()
            system('cls')
            print("{: >20} {: >20} {: >20} {: >20} {: >20} {: >23}".format(*header))
            for row in temp_db:
                if row[4] == 'rent' or row[4] == 'mortage' or row[4] == 'rent-mortage':
                    print("{: >20} {: >20} {: >20} {: >20} {: >20} {: >20}$ M".format(*row))
                else:
                    print("{: >20} {: >20} {: >20} {: >20} {: >20} {: >20}$".format(*row))
            print("\nPress enter to continue...")
            input()
        elif x == '5':
            print()
        elif x == '6':
            return
        else:
            system('cls')
            print("Wrong input! Please enter a number between 1-6")
            print("Press enter to continue...")
            input()


def main():
    while True:
        system("cls")
        print("1.Add")
        print("2.Delete")
        print("3.Edit")
        print("4.Report")
        print("5.Exit")
        print("===========================")
        x = input("Please enter your choice (1‐5): ")
        if x == '1':
            add()
        elif x == '2':
            delete()
        elif x == '3':
            edit()
        elif x == '4':
            report()
        elif x == '5':
            system('cls')
            print("Are you sure you want to exit?(y/n)")
            ans = input()
            if ans == 'y':
                exit(0)
        else:
            system('cls')
            print("Wrong input! Please enter a number between 1-5")
            print("Press enter to continue:")
            input()


signal.signal(signal.SIGINT, signal.SIG_IGN)
database = []
#test cases:
database.append(["MH's House", 150, 100, 3, "rent", 1200])
database.append(["Mammad's House", 250, 200, 4, "sale", 10000])
database.append([])
if __name__ == "__main__":
    main()
