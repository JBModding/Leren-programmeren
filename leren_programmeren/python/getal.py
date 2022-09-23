print("welkom bij het min max script")
#######################################
# a = 6
#b = 2
#######################################
a = float(input("Vul uw getal in: "))
b = float(input("VUl uw getal in: "))
if a > b: #true false
        print("A is groter dan B")
        print(f"Het grootste getal is {a}")
        print(f"Het klienste getal is {b}")
        maximum = a
        minimum = b


elif (a==b):
    print("A is gelijk aan B")
    maximum = a
    minimum = a

else:
    print("A is kleiner dan B")
    print(f"Het klienste getal is {a}")
    print(f"Het grootste getal is {b}")
    maximum = b
    minimum = a


print("Auther: Justin Boom 99064305 V1.2.0")