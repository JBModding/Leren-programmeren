print("totaal prijs voor aantal personen")
ticketsaantal = int(input("aantal tickets: "))
#######################################
ticketprijspp = 7.45
tickets = ticketsaantal * ticketprijspp
tickets_af = round(tickets,0)
########################################
vipvr = int(input("aantal minuten: "))
########################################
vipvrprijs = 0.37 / 5
vrprijs = vipvr * vipvrprijs
vip_af = round(vrprijs,0)
########################################
print("ticket totaalprijs: ", tickets)
print("vr totaalprijs: ", vip_af)
#######################################
eindprijs = tickets + vip_af
eindprijs_cent = eindprijs * 100
#######################################
print(f'''Dit geweldige dagje-uit met {ticketsaantal} mensen in de Speelhal met {vipvr} minuten VR kost je maar {eindprijs_cent} cent''')