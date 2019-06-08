from os import system
import time
import signal
import os
import platform

def clear_scr():
    if platform.system() == 'Windows':
        system('cls')
    elif platform.system() == 'Linux':
        system('clear')
def add():
    data = [] #temporary list for storing house data
    clear_scr()
    print("Please enter ID: ")
    name = my_input()
    data.append(name)
    clear_scr()
    print("Please enter real size: ")
    size = my_input()
    while not size.isdigit():#valid format checking
        clear_scr()
        print("Wrong input! please enter in valid format: ")
        size = my_input()
    size = int(size) #converting string to integer
    data.append(size)
    clear_scr()
    print("Please enter foundation size: ")
    foundation_size = my_input()
    while not foundation_size.isdigit():
        clear_scr()
        print("Wrong input! please enter in valid format: ")
        foundation_size = my_input()
    foundation_size = int(foundation_size)
    data.append(foundation_size)
    clear_scr()
    print("Pleas enter number of bedrooms:")
    rooms = my_input()
    while not rooms.isdigit():
        clear_scr()
        print("Wrong input! please enter in valid format: ")
        rooms = my_input()
    rooms = int(rooms)
    data.append(rooms)
    clear_scr()
    print("Please enter the type of deal (rent, sale, mortage, rent-mortage): ")
    type = my_input()
    valid_types = ("rent", "sale", "mortage", "rent-mortage")
    while type not in valid_types:
        clear_scr()
        print("Wrong input! please enter in valid format: ")
        type = my_input()
    data.append(type)
    clear_scr()
    print("Please enter the price: ")
    price = my_input()
    while not price.isdigit():
        clear_scr()
        print("Wrong input! please enter in valid format: ")
        price = my_input()
    data.append(price)
    database.append(data)
    clear_scr()
    print("House has been successfully added to the database.")
    print("Press Enter to Continue...")
    my_input()
def delete():
    clear_scr()
    database_len = len(database)
    counter = 0
    must_del = []
    while counter != database_len:
        must_del.append(database[counter][0])
        counter += 1
    counter = 0
    must_del = sorted(must_del, key=lambda s: s.lower())
    must_del.sort(key = len,reverse=True)
    while counter != len(must_del):
        print(counter+1,'-',must_del[counter],sep = ' ')
        counter +=1
    counter = 0
    print("===========================")
    print("pleas enter some part of the id you want to delete :")
    delete_id = my_input()
    must_del = []
    index = []
    while counter != database_len :
        if delete_id in database[counter][0]:
            index.append(counter)
            must_del.append(database[counter][0])
        counter +=1
    counter = 0
    if len(must_del) == 0 :
        clear_scr()
        delete()
        return
    if len(must_del) > 1:
        index = []
        clear_scr()
        must_del = sorted(must_del, key=lambda s: s.lower())
        must_del.sort(key = len,reverse=True)
        while counter != len(must_del):
            print(counter + 1, '-', must_del[counter], sep=' ')
            counter += 1
        print("===========================")
        print("your input was unclear pleas enter a number that show the id that you want to delete : ")
        delete_id = my_input()
        while not delete_id.isdigit() or not (int(delete_id) <= counter and 0 <int(delete_id)):
            clear_scr()
            print("Wrong input! please enter in valid format or range: ")
            delete_id = my_input()
        counter = 0
        while not must_del[int(delete_id)-1] in database[counter][0]:
            counter +=1
        index.append(counter)
    clear_scr()
    print("Are you sure you want to delete",database[index[0]],"(y/n)?")
    if(my_input() == 'y'):
        del(database[index[0]])
        clear_scr()
        print("House has been successfully deleted from the database.")
    else :
        print("House can not be delete")
    print("Press Enter to Continue...")
    my_input()
def edit():
    clear_scr()
    database_len = len(database)
    counter = 0
    must_edit = []
    while counter != database_len:
        must_edit.append(database[counter][0])
        counter += 1
    counter = 0
    must_edit = sorted(must_edit, key=lambda s: s.lower())
    must_edit.sort(key=len, reverse=True)
    while counter != len(must_edit):
        print(counter+1,'.',must_edit[counter],sep = '')
        counter +=1
    counter = 0
    print("===========================")
    print("pleas enter number or some part of the id you want to edit :")
    edit_id = my_input()
    while edit_id.isdigit() and int(edit_id) > 0 and not int(edit_id) <= len(database):
        clear_scr()
        print("Wrong input! please enter in valid format or range: ")
        edit_id = my_input()
        if not edit_id.isdigit():
            break
    if (edit_id.isdigit()):
        while counter != len(database):
            if must_edit[int(edit_id)-1] in database[counter]:
                clear_scr()
                print("Are you sure you want to edit", database[counter], "(y/n)?", )
                if (my_input() == 'y'):
                    edit_id = str(counter+1)
                    clear_scr()
                    print("which parameter do you want to Edite ?")
                    print("1 - id")
                    print("2 - real size")
                    print("3 - foundation size:")
                    print("4 - room number")
                    print("5 - status")
                    print("6 - price")
                    print("===========================")
                    print("please enter number : ")
                    x = my_input()
                    while not x.isdigit() and (int(x) > 6 or x < 1):
                        clear_scr()
                        print("please enter number in valid format or range : ")
                        x = my_input()
                    if int(x) == 1:
                        clear_scr()
                        print("please enter new id")
                        database[int(edit_id) - 1][0] = my_input()
                    elif int(x) == 2:
                        clear_scr()
                        print("please enter new real size")
                        x = my_input()
                        while not x.isdigit:
                            clear_scr()
                            print("please enter number in valid format : ")
                            x = my_input()
                        database[int(edit_id) - 1][1] = int(x)
                    elif int(x) == 3:
                        print("Please enter new foundation size: ")
                        x = my_input()
                        while not x.isdigit:
                            clear_scr()
                            print("please enter number in valid format : ")
                            x = my_input()
                        database[int(edit_id) - 1][2] = int(x)
                    elif int(x) == 4:
                        clear_scr()
                        print("Pleas enter new number of bedrooms:")
                        x = my_input()
                        while not x.isdigit:
                            clear_scr()
                            print("please enter number in valid format : ")
                            x = my_input()
                        database[int(edit_id) - 1][3] = int(x)
                    elif int(x) == 5:
                        clear_scr()
                        print("Please enter the new type of deal (rent, sale, mortage, rent-mortage): ")
                        type = my_input()
                        valid_types = ("rent", "sale", "mortage", "rent-mortage")
                        while type not in valid_types:
                            clear_scr()
                            print("Wrong input! please enter in valid format: ")
                            type = my_input()
                        database[int(edit_id) - 1][4] = type
                    elif int(x) == 6:
                        clear_scr()
                        print("Please enter the new price: ")
                        x = my_input()
                        while not x.isdigit():
                            clear_scr()
                            print("Wrong input! please enter in valid format: ")
                            x = my_input()
                        database[int(edit_id) - 1][5] = int(x)
                    print("House has been successfully edited.")
                    print("Press Enter to Continue...")
                    my_input()
                    return
                else:
                    print("House can not be edited")
                    print("Press Enter to Continue...")
                    my_input()
                    return
            counter +=1
    else:
        flag = 1
        must_edit = []
        while counter < len (database):
            if edit_id in database[counter][0]:
                edit_id = str(counter+1)
                must_edit.append(database[counter][0])
            counter += 1
    if flag == 1 and len(must_edit) == 0:
        clear_scr()
        print("your input was wrong!")
        print("Press Enter to Continue...")
        my_input()
        return
    elif len(must_edit) > 1:
        counter = 0
        clear_scr()
        while counter != len(must_edit):
            print(counter + 1, '-', must_edit[counter], sep=' ')
            counter += 1
        print("===========================")
        print("your input was unclear pleas enter a number that show the id that you want to edit : ")
        edit_id = my_input()
        while not edit_id.isdigit() or not (int(edit_id) <= counter and 0 < int(edit_id)):
            clear_scr()
            print("Wrong input! please enter in valid format or range: ")
            edit_id = my_input()
    print("Are you sure you want to edit", database[int(edit_id)-1], "(y/n)?", )
    if (my_input() == 'y'):
        clear_scr()
        print("which parameter do you want to Edite ?")
        print("1 - id")
        print("2 - real size")
        print("3 - foundation size:")
        print("4 - room number")
        print("5 - status")
        print("6 - price")
        print("===========================")
        print("please enter number : ")
        x = my_input()
        while not x.isdigit() and (int(x)>6 or x<1):
            clear_scr()
            print("please enter number in valid format or range : ")
            x = my_input()
        if int(x) == 1:
            clear_scr()
            print("please enter new id")
            database[int(edit_id) - 1][0] = my_input()
        elif int(x) == 2:
            clear_scr()
            print("please enter new real size")
            x = my_input()
            while not x.isdigit:
                clear_scr()
                print("please enter number in valid format : ")
                x = my_input()
            database[int(edit_id) - 1][1] = int(x)
        elif int(x) == 3:
            print("Please enter new foundation size: ")
            x = my_input()
            while not x.isdigit:
                clear_scr()
                print("please enter number in valid format : ")
                x = my_input()
            database[int(edit_id) - 1][2] = int(x)
        elif int(x) == 4:
            clear_scr()
            print("Pleas enter new number of bedrooms:")
            x = my_input()
            while not x.isdigit:
                clear_scr()
                print("please enter number in valid format : ")
                x = my_input()
            database[int(edit_id) - 1][3] = int(x)
        elif int(x) == 5:
            clear_scr()
            print("Please enter the new type of deal (rent, sale, mortage, rent-mortage): ")
            type = my_input()
            valid_types = ("rent", "sale", "mortage", "rent-mortage")
            while type not in valid_types:
                clear_scr()
                print("Wrong input! please enter in valid format: ")
                type = my_input()
            database[int(edit_id) - 1][4] = type
        elif int(x) == 6:
            clear_scr()
            print("Please enter the new price: ")
            x = my_input()
            while not x.isdigit():
                clear_scr()
                print("Wrong input! please enter in valid format: ")
                x = my_input()
            database[int(edit_id) - 1][5] = int(x)
        print("House has been successfully edited.")
        print("Press Enter to Continue...")
        my_input()
        return
    else:
        print("House can not be edit")
        print("Press Enter to Continue...")
        my_input()
        return


def report():
    while True:
        clear_scr()
        print("1. All")
        print("2. by size")
        print("3. by status")
        print("4. by cost")
        print("5. by room")
        print("6. Back")
        print("===========================")
        print("Please enter your choice (1‐6): ")
        x = my_input()
        #Name of each house variable to be printed in each report:
        header = ['ID', 'Size(real)', 'Size(Foundation)', 'Rooms', 'State', 'Cost(s)']
        if x == '1':
            clear_scr()
            #Dedicating 20 chracters to each field:
            print("{: >20} {: >20} {: >20} {: >20} {: >20} {: >23}".format(*header))
            #sorting by the length of the house name
            database.sort(key=lambda y: y[0].lower())
            database.sort(key=lambda y: len(y[0]),reverse=True)
            for row in database:
                if row[4] == 'rent' or row[4] == 'mortage' or row[4] == 'rent-mortage':
                    #if house is for rent or mortage print an extra 'M' indicating
                    #that the price is per month
                    print("{: >20} {: >20} {: >20} {: >20} {: >20} {: >20}$ M".format(*row))
                else:
                    print("{: >20} {: >20} {: >20} {: >20} {: >20} {: >20}$".format(*row))
            print("\nPress enter to continue...")
            my_input()
        elif x == '2':
            clear_scr()
            print("Enter the lower bound: ")
            lower = my_input()
            while not lower.isdigit(): #error handling for wrong inputs
                clear_scr()
                print("Wrong input! please enter in valid format: ")
                lower = my_input()
            lower = int(lower)
            clear_scr()
            print("Enter the upper bound: ")
            upper = my_input()
            while not upper.isdigit():
                clear_scr()
                print("Wrong input! please enter in valid format: ")
                upper = my_input()
            upper = int(upper)
            while lower > upper:
                clear_scr()
                print("Upper size must be bigger than the lower size!")
                print("Enter the lower bound: ")
                lower = my_input()
                while not lower.isdigit():
                    clear_scr()
                    print("Wrong input! please enter in valid format: ")
                    lower = my_input()
                lower = int(lower)
                print("Enter the upper bound: ")
                upper = my_input()
                while not upper.isdigit():
                    clear_scr()
                    print("Wrong input! please enter in valid format: ")
                    upper = my_input()
                upper = int(upper)
            temp_db = [] #creating a temporary database for storing desired data
            for i in database:
                if i[2] >= lower and i[2] < upper:
                    temp_db.append(i)
            #sorting the temporary list by the foundation size
            temp_db.sort(key=lambda y: y[2])
            temp_db.reverse()
            clear_scr()
            print("{: >20} {: >20} {: >20} {: >20} {: >20} {: >23}".format(*header))
            for row in temp_db:
                if row[4] == 'rent' or row[4] == 'mortage' or row[4] == 'rent-mortage':
                    print("{: >20} {: >20} {: >20} {: >20} {: >20} {: >20}$ M".format(*row))
                else:
                    print("{: >20} {: >20} {: >20} {: >20} {: >20} {: >20}$".format(*row))
            print("\nPress enter to continue...")
            my_input()
        elif x == '3':
            clear_scr()
            print("Please enter the type of deal (rent, sale, mortage, rent-mortage): ")
            type = my_input()
            valid_types = ("rent", "sale", "mortage", "rent-mortage")
            while type not in valid_types:
                clear_scr()
                print("Wrong input! please enter in valid format: ")
                type = my_input()
            clear_scr()
            print("{: >20} {: >20} {: >20} {: >20} {: >20} {: >23}".format(*header))
            for row in database:
                if row[4] == type:
                    if row[4] == 'rent' or row[4] == 'mortage' or row[4] == 'rent-mortage':
                        print("{: >20} {: >20} {: >20} {: >20} {: >20} {: >20}$ M".format(*row))
                    else:
                        print("{: >20} {: >20} {: >20} {: >20} {: >20} {: >20}$".format(*row))
            print("\nPress enter to continue...")
            my_input()
        elif x == '4':
            clear_scr()
            print("Enter the lower bound: ")
            lower = my_input()
            while not lower.isdigit():
                clear_scr()
                print("Wrong input! please enter in valid format: ")
                lower = my_input()
            lower = int(lower)
            clear_scr()
            print("Enter the upper bound: ")
            upper = my_input()
            while not upper.isdigit():
                clear_scr()
                print("Wrong input! please enter in valid format: ")
                upper = my_input()
            upper = int(upper)
            while lower > upper:
                clear_scr()
                print("Upper price must be bigger than the lower price!")
                print("Enter the lower bound: ")
                lower = my_input()
                while not lower.isdigit():
                    clear_scr()
                    print("Wrong input! please enter in valid format: ")
                    lower = my_input()
                lower = int(lower)
                print("Enter the upper bound: ")
                upper = my_input()
                while not upper.isdigit():
                    clear_scr()
                    print("Wrong input! please enter in valid format: ")
                    upper = my_input()
                upper = int(upper)
            temp_db = []
            for i in database:
                if i[5] >= lower and i[5] < upper:
                    temp_db.append(i)
            temp_db.sort(key=lambda y: y[5])
            temp_db.reverse()
            clear_scr()
            print("{: >20} {: >20} {: >20} {: >20} {: >20} {: >23}".format(*header))
            for row in temp_db:
                if row[4] == 'rent' or row[4] == 'mortage' or row[4] == 'rent-mortage':
                    print("{: >20} {: >20} {: >20} {: >20} {: >20} {: >20}$ M".format(*row))
                else:
                    print("{: >20} {: >20} {: >20} {: >20} {: >20} {: >20}$".format(*row))
            print("\nPress enter to continue...")
            my_input()
        elif x == '5':
            clear_scr()
            print("Enter the number of rooms: ")
            num_rooms = my_input()
            while not num_rooms.isdigit():
                clear_scr()
                print("Wrong input! please enter in valid format: ")
                num_rooms = my_input()
            num_rooms = int(num_rooms)
            clear_scr()
            print("Enter the proximity diameter: ")
            proximity = my_input()
            #considering a proximity diamater for the number of rooms
            #so if the absoloute value of rooms of the house - num_rooms
            #is within the proximity range it will be displayed
            while not proximity.isdigit():
                clear_scr()
                print("Wrong input! please enter in valid format: ")
                proximity = my_input()
            proximity = int(proximity)
            clear_scr()
            print("{: >20} {: >20} {: >20} {: >20} {: >20} {: >23}".format(*header))
            for row in database:
                if abs(row[3] - num_rooms) <= proximity:
                    if row[4] == 'rent' or row[4] == 'mortage' or row[4] == 'rent-mortage':
                        print("{: >20} {: >20} {: >20} {: >20} {: >20} {: >20}$ M".format(*row))
                    else:
                        print("{: >20} {: >20} {: >20} {: >20} {: >20} {: >20}$".format(*row))
            print("\nPress enter to continue...")
            my_input()
        elif x == '6':
            return
        else:
            clear_scr()
            print("Wrong input! Please enter a number between 1-6")
            print("Press enter to continue...")
            my_input()

def my_input():
    while True :
        try :
            x = input()
            return x
        except EOFError:
            pass

def main():
    while True:
        # clearing screen on each update
        clear_scr()
        print("1.Add")
        print("2.Delete")
        print("3.Edit")
        print("4.Report")
        print("5.Exit")
        print("===========================")
        print("Please enter your choice (1‐5): ")
        x = my_input()
        if x == '1':
            add()
        elif x == '2':
            delete()
        elif x == '3':
            edit()
        elif x == '4':
            report()
        elif x == '5':
            clear_scr()
            print("Are you sure you want to exit?(y/n)")
            ans = my_input()
            if ans == 'y':
                exit(0)
        else:
            clear_scr()
            #error handling for wrong input
            print("Wrong input! Please enter a number between 1-m5")
            print("Press enter to continue:")
            my_input()

#ignoring CTRL+C signal

def signal_handle(sig, frame):
    #main()
    return


#signal.signal(signal.SIGINT, signal_handle)
signal.signal( signal.SIGINT, signal.SIG_IGN )

database = [] #main database
#test cases:
database.append(["aammad's", 150, 100, 3, "rent", 1200])
database.append(["aammad's House", 150, 100, 3, "rent", 1200])
database.append(["Mammad's House", 250, 200, 4, "sale", 10000])
database.append(["Aammad's House", 250, 200, 4, "sale", 10000])
if platform.system() == 'Windows':
    os.system('mode con: cols=135 lines=30')
elif platform.system() == 'Linux':
    os.system('resize -s 30 130')
if __name__ == "__main__":
    #while True:
    main()
