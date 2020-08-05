def userRound(num):

    
    b = []
    c = []

    decimal = float(num) - int(float(num))
    if decimal == 0:
        str(decimal)
        for each in decimal:
            c.append(decimal)
        return
    
    decimal = str(decimal)

    for each in decimal:
        b.append(each)
    
    if (int(b[3]) >= 5):
        b[2] = int(b[2])
        b[2] = b[2] + 1
        if(b[2] > 9):
            num = int(float(num)) + 1
            
    c.append(str(int(float(num))))
    
    if (int(b[2]) <= 9):
        c.append(".")
        c.append(str(b[2]))

    print ("Your rounded number is: ")
    for each in c:
        print(each, end = "")

again = str("y")
while again != "n":
    numEntered = input("Please enter a number: ")
    if type(numEntered) is int:
        print("yikes")
    else:
        userRound(numEntered)
        again = input("\n\nDo you wou want to round another number? (y/n) ")
