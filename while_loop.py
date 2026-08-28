count = 1

while count <= 5:
    print(count)
    count += 1

    #nested while loop


i = 1

while i <= 3:
    print("Outer:", i)

    j = 1

    while j <= 2:
        print("  Inner:", j)
        j += 1

    i += 1