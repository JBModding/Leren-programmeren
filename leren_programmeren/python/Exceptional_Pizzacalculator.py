print("Welkom in Pizza shop")
small=8.99
medium=14.99
large=20.99
var = 0
#####
while var == 0:
    try:
        smallsizepizza=int(input("Hoeveel Small size pizza's wilt u? "))
        var = +1
    except:
        print('onjuiste ingevoerde waarde')

while var == 1:
    try:
        mediumsizepizza=int(input("Hoeveel medium size pizza's wilt u?"))
        var = +2
    except:
        print('onjuiste ingevoerde waarde')
    
while var == 2:
    try:
        largesizepizza=int(input("Hoeveel Large size pizza's wilt u?"))
        var = +3
    except:
        print('onjuiste ingevoerde waarde')
    
    

smallsizepizzaprize = smallsizepizza * small
mediumsizepizzaprize = mediumsizepizza * medium
largesizepizzaprize = largesizepizza * large

totaal = smallsizepizza * small + mediumsizepizza * medium + largesizepizza * large
var = 3
##
print(f'''U heeft gekozen voor:
---------------------------------------------------------
\033[1m{smallsizepizzaprize}\033[0m kleine pizza's
---------------------------------------------------------
\033[1m{mediumsizepizzaprize}\033[0m medium pizza's
---------------------------------------------------------
\033[1m{largesizepizzaprize}\033[0m grote pizza's.''' )
print(f"""---------------------------------------------------------
uw eindprijs word \033[1m€{totaal}\033[0m
---------------------------------------------------------""")
#################################################
