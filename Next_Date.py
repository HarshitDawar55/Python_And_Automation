# Pushing
def check_century(n):
    l = []
    # l=[x for x in range(0,2)]
    for i in range(0, 2):
        r = n % 10
        l.append(r)
        n = n // 10
    if l[0] == 0 and l[1] == 0:
        return 1, n
    else:
        return -1, n


def leap(n):
    a, remainder = check_century(n)
    mul_of_4 = [x for x in range(1, 1001) if x % 4 == 0]
    if a == 1:
        if remainder in mul_of_4:
            if n % 400 == 0 and n % 4 == 0:
                return 1
        if remainder not in mul_of_4:
            if n % 4 == 0:
                return 1
    if a == -1:
        if n % 4 == 0:
            return 1
        else:
            return -1


again = True


while again:
    # print(199//10)
    day, month, year = int(input("Enter The Day\n")), int(input("Enter The Month\n")), int(input("Enter The Year\n"))

    z = leap(year)

    l31 = [1, 3, 5, 7, 8, 10, 12]
    l30 = [4, 6, 9, 11]
    l2 = [2]
    if month in l31:
        if day == 31:
            print("Tomorrow is 01/%d/%d" % (month + 1, year))
        elif 31 > day > 0:
            print("Tomorrow is %d/%d/%d" % (day + 1, month, year))
        else:
            print("Wrong day entered for month having 31 days!!!")

    elif month in l30:
        if 30 > day > 0:
            print("Tomorrow is %d/%d/%d" % (day + 1, month, year))
        elif day == 30:
            print("Tomorrow is 01/%d/%d" % (month + 1, year))
        else:
            print("Wrong day entered for month having 30 days!!!")

    elif month in l2:
        if day > 29:
            print("Wrong day entered as February does not contains more than 29 days")
        elif z == 1 and day == 28:
            print("Tomorrow is 29/02/%d" % year)
        elif z == 1 and day < 28:
            print("Tomorrow is %d/02/%d" % (day + 1, year))
        elif z == -1 and day == 28:
            print("Tomorrow is 01/03/%d" % year)
        elif z == -1 and day < 28:
            print("Tomorrow is %d/02/%d" % (day + 1, year))
        else:
            print("Wrong Day Entered because of february month")

    else:
        print("Wrong month entered")

    checker = input("Want to try again? \nEnter y or Y or Yes to try again!!!\n")
    if checker in ('y', 'Y', 'yes'):
        again = True
    else:
        again = False
