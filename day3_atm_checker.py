print("Welcome to Atm Access Checker")
age =int(input("How old are you? "))



if age >=18:
    print("You can use the Atm")
    id_card =input("Do you have an Id card? yes or no ").lower()
    if id_card == "yes":
        pin=input("Do you know your pin? yes or no ").lower()
        if pin== "yes":
            print("You can use the ATM")
        else:
            print("Access Denied: PIN not confirmed.")

    else:
        print("Access Denied: No ID card.")
        
else:
    print("Access Denied")
    exit()