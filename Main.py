import Add
import Delete
import Edit
import Report
from os import system

def main():
    while True:
        system("cls")
        print("1.Add")
        print("2.Delete")
        print("3.Edit")
        print("4.Report")
        print("5.Exit")
        x = input()
try:
    main()
except KeyboardInterrupt:
    main()
finally:
    main()