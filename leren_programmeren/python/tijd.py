dag = 23
uur = 60


tijd = int(input("hoelaat is het in uren? "))
min = int(input("hoelaat is het in minuten? "))

eind_uren = dag - tijd
eind_min = uur - min

print(f"Dan duurt de dag nog {eind_uren} uur en {eind_min} minuten voordat de dag voorbij is")

