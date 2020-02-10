import cmath
import math


fone = 14
limit = 4

n = 1
while limit != 0:
    print("Welcome to Time Domain Analysis; Pick An Option")

    print("1. Delay Time(td)", "\n2. Rise Time(tr)",
          "\n3. Peak Time(tp)", "\n4. Setting Time(ts)",
          "\n5. Max. Overshoot(mp)",)
    print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

    print()

    option = input("Please Enter Your Option: \n")
    print()

    fone >= limit

    if option == "1":

        print("Delay time: This is the time taken for the response to reach 50% Of the final value for the first time.")

    elif option == "2":

        print("For Rise Time(tp); Enter The Parameters(ωn & ξ): \n")

        x = int(input("Enter The value of ωn:\n"))
        y = float(input("Enter The Value of ξ:\n"))

        a = math.sqrt((1 - (y ** 2))) / y
        b = math.sqrt((1 - (y ** 2))) * x

        tr = (3.141592654-(math.atan(a))) / b

        print("Rise Time is equal to", tr, "secs")
        print("Approximately", round(tr, 2), "secs")
        print()

    elif option == "3":

        print("For Peak Time (tp); Enter The Parameters(ωn & ξ):\n")

        x = int(input("Enter The value of ωn:\n"))
        y = float(input("Enter The Value of ξ:\n"))

        tp = (n * 3.141592654) / math.sqrt((1 - (y ** 2))) * x

        print("Peak Time is equal to", tp, "secs")
        print("Approximately", round(tp, 2), "secs")

    elif option == "4":

        print("For Settling Time (ts); Enter The Parameters(ωn & ξ):\n")

        x = int(input("Enter The value of ωn:\n"))
        y = float(input("Enter The Value of ξ:\n"))

        ts = 4 / (x * y)

        print("Settling Time is equal to", ts, "secs")
        print("Approximately", round(ts, 2), "secs")

    elif option == "5":

        print("For Maximum Overshoot (mp); Enter The Parameters(ωn & ξ):\n")

        x = int(input("Enter The value of ωn:\n"))
        y = float(input("Enter The Value of ξ:\n"))

        mp = (2.718281828 ** -((3.141592654) * y / math.sqrt((1 - (y ** 2))))) * 100

        print("Maximum Overshoot is equal to", mp, "secs")
        print("Approximately", round(mp, 2), "secs")

    option = 0
    choice = input("enter q to quit or c to countinue: \n")
    if choice == "q":
        quit()
    else:
        pass
    print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
