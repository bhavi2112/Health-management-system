def getdate ():
    import datetime
    return datetime.datetime.now()
def a (z):
    if l_r == 1:
        print("Press 1 for Harry, Press 2 for Rohan and Press 3 for Hammad\n")
        which = int(input("type here\n"))
        print("Press 1 for food and press 2 for exercises")
        which1 = int(input())
        if which == 1:
            if which1 == 1:
                print("Type what you eat")
                h_eat = input()
                h_eat1 = input("How many / How much\n")
                with open("ex5harryfood.txt", "a") as x:
                    x.write((str([getdate()]))+":"+h_eat1+h_eat+"\n")
                    print("Writen")
            elif which1 == 2:
                print("Type what you have done in  exercises")
                h_ex = input()
                h_ex1 = input("How many / How much\n")
                with open("ex5harryex.txt", "a") as x:
                    x.write((str([getdate()]))+":"+h_ex1+h_ex+"\n")
                    print("Writen")
            else:
                print("Please type a valid number (Press 1 for food and press 2 for exercises)")
        elif which == 2:
            if which1 == 1:
                print("Type what you have eat")
                r_eat = input()
                r_eat1 = input("How many / How much\n")
                with open("ex5rohanfood.txt", "a") as x:
                    x.write((str([getdate()]))+":"+r_eat1+r_eat+"\n")
                    print("Writen")
            elif which1 == 2:
                print("Type what you have done in  exercises")
                r_ex = input()
                r_ex1 = input("How many / How much\n")
                with open("ex5rohanex.txt", "a") as x:
                    x.write((str([getdate()]))+":"+r_ex1+r_ex+"\n")
                    print("Writen")
            else:
                print("Please type a valid number (Press 1 for food and press 2 for exercises)")
        elif which == 3:
            if which1 == 1:
                print("Type what you have eat")
                h_eat = input()
                h_eat1 = input("How many / How much\n")
                with open("ex5hammadfood.txt", "a") as x:
                    x.write((str([getdate()]))+":"+h_eat1+h_eat+"\n")
                    print("Writen")
            elif which1 == 2:
                print("Type what you have done in  exercises")
                h_ex = input()
                h_ex1 = input("How many / How much\n")
                with open("ex5hammadex.txt", "a") as x:
                    x.write((str([getdate()]))+":"+h_ex1+h_ex+"\n")
                    print("Writen")
            else:
                print("Please type a valid number (Press 1 for food and press 2 for exercises)")
        else:
            print("Please type a valid number (Press 1 for Harry, Press 2 for Rhona and Press 3 for Hammad)")
print("Welcome to !!VICTOR FITNESS CLUB!!\n")
print("Press 1 for lock or press 2 for retrieve\n")
l_r = int(input())
a(l_r)
def a (z):
    if l_r == 2:
        print("Whom do you want to retrieve Press 1 for Harry, Press 2 for Rhona and Press 3 for Hammad\n")
        rwhich = int(input("Type here\n"))
        if rwhich == 1:
            print("Press 1 to retrieve food and Press 2 to retrieve exercises\n")
            rwhich2 = int(input())
            if rwhich2 == 1:
                with open("ex5harryfood.txt") as o:
                    g = o.read()
                    print(g)
            elif rwhich2 == 2:
                with open("ex5harryex.txt") as o:
                    g = o.read()
                    print(g)
            else:
                print("Please type a valid number (Press 1 for food and press 2 for exercises)")
        elif rwhich == 2:
            print("Press 1 to retrieve food and Press 2 to retrieve exercises\n")
            rwhich2 = int(input())
            if rwhich2 == 1:
                with open("ex5rohanfood.txt") as o:
                    g = o.read()
                    print(g)
            elif rwhich2 == 2:
                with open("ex5rohanex.txt") as o:
                    g = o.read()
                    print(g)
            else:
                print("Please type a valid number (Press 1 for food and press 2 for exercises)")
        elif rwhich == 3:
            print("Press 1 to retrieve food and Press 2 to retrieve exercises\n")
            rwhich2 = int(input())
            if rwhich2 == 1:
                with open("ex5hammadfood.txt") as o:
                    g = o.read()
                    print(g)
            elif rwhich2 == 2:
                with open("ex5hammadex.txt") as o:
                    g = o.read()
                    print(g)
            else:
                print("Please type a valid number (Press 1 for food and press 2 for exercises)")
        else:
            print("Please type a valid number (Press 1 for Harry, Press 2 for Rohan and Press 3 for Hammad)")

a(l_r)

