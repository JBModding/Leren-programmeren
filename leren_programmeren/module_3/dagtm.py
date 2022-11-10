dagenvdweek = ["maandag","dinsdag", "woensdag" , "donderdag" , "vrijdag" , "zaterdag" , "zondag"]

while True :
    dag = input("Kies een dag van de week uit: ").lower()
    if dag in dagenvdweek: 
        break

    else:
        print("Probeer de dag nog een x in te vullen")

index = 0

while True:
    print(dagenvdweek[index])
    if dagenvdweek[index] == dag:
        break

    index += 1
