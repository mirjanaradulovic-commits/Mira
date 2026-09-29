import random


#os.remove
while True:
    liste = []
    
    eingabe = input("Wie oft soll geworfen werden? (oder 'exit' zum Beenden): ")
    
    if eingabe.lower() == 'exit':
        print("Spiel beendet. Alle Zähler wurden zurückgesetzt.")
        break
        
    wurf = int(eingabe)

    for x in range(wurf):
        wuerfel = random.randint(1, 6)
        liste.append(wuerfel)


    eins   = liste.count(1)
    zwei   = liste.count(2)
    drei   = liste.count(3)
    vier   = liste.count(4)
    fuenf  = liste.count(5)
    sechs  = liste.count(6)

    # Ausgabe
    print(f"""
--- Statistik für diese Runde ---
Sie haben {eins}x die 1 geworfen
Sie haben {zwei}x die 2 geworfen
Sie haben {drei}x die 3 geworfen
Sie haben {vier}x die 4 geworfen
Sie haben {fuenf}x die 5 geworfen
Sie haben {sechs}x die 6 geworfen
Gesamtanzahl Würfe: {len(liste)}
--------------------------------
""")