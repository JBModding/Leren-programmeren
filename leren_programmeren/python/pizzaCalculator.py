print("Welkom bij de davinci pizza shop:")

small=float(8.99)
medium=float(14.99)
largo=float(20.99)
#########################

smallsize=int(input("hoeveel kleine pizza's wilt u? "))
mediumsize=int(input("hoeveel medium pizza's wilt u? "))
largesize=int(input("hoeveel grote pizza's wilt u? "))
################################################
totaal = smallsize * small + mediumsize * medium + largesize * largo
print(f'''U heeft gekozen voor {smallsize} pizza's, {mediumsize} pizza's, {largesize} pizza's. uw eindprijs word {totaal}''' )
#################################################
