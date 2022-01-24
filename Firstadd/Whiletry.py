def sum():
    sum = 0
    variable = input("Enter number to add or just press Enter to exit\t")
    number = 0
    while variable != "":
        number = int(variable)
        sum = sum + number
        print(sum)
        variable = input("Enter number to add or just press Enter to exit\t")
    return sum
def mod2():
    count = 100
    while count > 1:
        print(count%2)
        count -= 1
def bettersum():
    sum = 0
    while True:
        variable = input("Enter a nuber or press enter to quit\t")
        if variable == '':
            break
        number = int(variable)
        sum += number
        print("The sum is: %-15d" % sum )
