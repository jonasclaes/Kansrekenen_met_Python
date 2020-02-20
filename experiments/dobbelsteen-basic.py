import random

# Kies hoeveel keer je wilt gooien.
aantal_worpen = 10000

# Maak een lege lijst met resultaten aan.
resultaten = list()

# Gooi een x aantal keer en sla de resultaten op in de lijst.
for i in range(0, aantal_worpen):
    # Gooi een getal tussen 1 en 6, zoals een dobbelsteen dus.
    worp = random.randint(1, 6)

    # Sla de worp op.
    resultaten.append(worp)

# Laat zien hoeveel keer er gegooid is.
print("Er werd in totaal %i keer gegooid." % aantal_worpen)

# Laat zien hoevaak per aantal ogen dat er gegooid is.
for i in range(1, 7):
    # Tel het aantal keer dat dit voorkomt.
    worpen = resultaten.count(i)

    # Bereken de procentuele waarde.
    procent = (worpen / aantal_worpen) * 100

    # Laat de waarden zien.
    print("Er werd %i keer %i gegooid." % (worpen, i))
    print("Dit is dus %.2f%%." % procent)