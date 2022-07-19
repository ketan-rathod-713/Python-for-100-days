# Now whenver working with pycharm add .gitignore file with the two folders specified and then start coding
# and each time making project track the day number as the project title so that i helps further to document the python coding journey

# Now program of coffee machine

# May be i can make dictionary of coffee names with their specifications like price , and all
myCoffees = {

}


def prompt():
    print("1. print report (say r)")
    print("2. expresso / latto / cappuchino (e, l, c)")
    print("3. Turn off (say O)")
    a = input("What would you like ? ")
    return a.lower()


def printReport(water, milk, coffee, money):
    print(f"Water : {water}")
    print(f"Milk : {milk}")
    print(f"Coffee : {coffee}")
    print(f"Money : {money}")


def isResourcesSufficient(rwater, rmilk, rcoffee, water, milk, coffee):
    if (rwater <= water and rmilk <= milk and rcoffee <= coffee):
        return True
    return False


def Transaction(rmoney, money):
    if rmoney <= money:
        return [True, money - rmoney]
    else:
        return [False, rmoney - money]


def coffee(water, milk, cofee, money):
    choice = prompt()
    if choice == 'r':
        printReport(water, milk, cofee, money)
    elif choice == 'o':
        return
    else:
        print("In working")
        if choice == 'l' and isResourcesSufficient(100, 50, 20, water, milk, cofee):
            given = int(input("Enter the money .. "))
            trans = Transaction(20,given)
            if trans[0]:
                water -= 100
                milk -= 50
                cofee -= 20
                print("Transaction success")
                print("Enjoy with this delicious latte :)))")
                print(f"here is your refund {trans[1]}")
            else:
                print("Transaction unsuccessful")
                print(f"You require more {trans[1]} money")
        elif choice == 'e' and isResourcesSufficient(100, 50, 20, water, milk, cofee):
            given = int(input("Enter the money .. "))
            trans = Transaction(20, given)
            if trans[0]:
                water -= 100
                milk -= 50
                cofee -= 20
                print("Transaction success")
                print("Enjoy with this delicious latte :)))")
                print(f"here is your refund {trans[1]}")
            else:
                print("Transaction unsuccessful")
                print(f"You require more {trans[1]} money")
        elif choice == 'c' and isResourcesSufficient(100, 50, 20, water, milk, cofee):
            given = int(input("Enter the money .. "))
            trans = Transaction(20, given)
            if trans[0]:
                water -= 100
                milk -= 50
                cofee -= 20
                print("Transaction success")
                print("Enjoy with this delicious latte :)))")
                print(f"here is your refund {trans[1]}")
            else:
                print("Transaction unsuccessful")
                print(f"You require more {trans[1]} money")
        else:
            print("Resources are not sufficient")
    print("\n")
    coffee(water, milk, cofee, money)


coffee(300, 200, 100, 0)

# Now only change the resources and all otherwise it's fine