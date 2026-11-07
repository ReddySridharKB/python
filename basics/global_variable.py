

a = 10                        #global variable
print("first Outside function:", a)

def display():
    global a                    #accessing global variable
    a = 20                    #local variable
    print("Inside function:", a)

display()

print("Outside function:", a)