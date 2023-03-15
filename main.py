import math
def triagle_area():
    a=float(input("Enter First Arm= "))
    b=float(input("Enter Second Arm="))
    c=float(input("Enter Third Arm="))
    if(a+b)>c and (b+c)>a   and (a+c)>b:
        s=(a+b+c)/2
        area=math.sqrt(s*(s-a)*(s-b)*(s-c))
        print("Triangle Area=",area)
    else:
        print("Triangle is not possiable")
        triagle_area()
