username = input("Enter username: ")
password = input("Enter password: ")

if username == "reddy":
    if password == "1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Wrong username")