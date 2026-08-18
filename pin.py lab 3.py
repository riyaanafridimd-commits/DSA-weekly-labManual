secret = "basanthi"
n = 0

while n < 3:
    password = input("Enter password: ")

    if password == secret:
        print("Access Granted")
        break
    else:
        n += 1
        if n < 3:
            print("Incorrect. Try again!")
        else:
            print("Access Denied")
