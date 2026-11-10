n = 0
subscription = 0  # 0 - Basic subscription, 1 - Pro+ subscription

print("Welcome to the list creation program!")

if subscription == 0:
    print("Subscription: Basic, up to 10 items per list\n")
else:
    print("Subscription: Pro+, unlimited items per list\n")

while n == 0:
    try:
        n = int(input("Enter the number of items: "))
        if subscription == 0:
            if n > 10:
                print("\nAccess denied! You cannot enter more than 10 items!")
                print("Please purchase the Pro+ subscription.\n")
                n = 0
    except ValueError:
        print("Text and special characters are not allowed! Please enter a valid number.")

data_list = []
i = 0

while i < n:
    user_string = input(f"Enter item #{i + 1} that you want to add: ")
    
    if user_string.strip() != "":
        if user_string == "/stop":
            break
        else:
            data_list.append(user_string)
            i += 1
    else:
        print("\n     Error: Item cannot be empty! Please try again.")
    print("\nYou can also stop the process and display the list immediately! Command: /stop")

print("\nYou have created a list!\n")
print(data_list)

if subscription == 0:
    print("\nTo create a larger list, \npurchase a subscription from the developer of this mini-project @L1nemiq\n")
elif data_list == []:
    print("\nThe list is empty! Create a new one by running the program again.")
else:
    print("\nSubscription detected! \nThank you for using the program and for your support!\n")
