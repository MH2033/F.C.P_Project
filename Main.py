from Add import add
from Delete import delete
from Edit import edit
from Report import report
from os import system
import time

def main():
    while True:
        system("cls")
        print("1.Add")
        print("2.Delete")
        print("3.Edit")
        print("4.Report")
        print("5.Exit")
        print("===========================")
        print("Please enter your choice (1‐5):")
        x = input()
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

try:
    main()
except KeyboardInterrupt:
    main()
finally:
    main()