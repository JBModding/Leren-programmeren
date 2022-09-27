print("Welkom bij de davinci pizza shop:")

small=float(8.99)
medium=float(14.99)
largo=float(20.99)
var = 0
#########################

smallsize=int(input("hoeveel kleine pizza's wilt u? "))
mediumsize=int(input("hoeveel medium pizza's wilt u? "))
largesize=int(input("hoeveel grote pizza's wilt u? "))
################################################
totaal = smallsize * small + mediumsize * medium + largesize * largo 
totaal_af = round(totaal,2)
print(f'''U heeft gekozen voor:
---------------------------------------------------------
\033[1m{smallsize}\033[0m kleine pizza's
---------------------------------------------------------
\033[1m{mediumsize}\033[0m medium pizza's
---------------------------------------------------------
\033[1m{largesize}\033[0m grote pizza's.''' )
print(f"""---------------------------------------------------------
uw eindprijs word \033[1m€{totaal_af}\033[0m
---------------------------------------------------------""")
#################################################
