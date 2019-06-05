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
    time.sleep(1)

def delete():
    print()

def edit():
    print()

def report():
    print()

def main():
    while True:
        system("cls")
        print("1.Add")
        print("2.Delete")
        print("3.Edit")
        print("4.Report")
        print("5.Exit")
        print("===========================")
        x = input("Please enter your choice (1‐5):")
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
if __name__ == "__main__":
    main()
