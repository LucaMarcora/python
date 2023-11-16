
tupla_pluviometrica = (
    (("Vittuone", "Milano"), (2022, ("gennaio", 20))),
    (("Vittuone", "Milano"), (2023, ("marzo", 80))),
    (("Vittuone", "Milano"), (2023, ("aprile", 60))),
    (("Vittuone", "Milano"), (2023, ("maggio", 80))),
    (("Vittuone", "Milano"), (2023, ("luglio", 30))),
    (("Vittuone", "Milano"), (2023, ("agosto", "N/D"))),
    (("Varenna", "Lecco"), (2023, ("luglio", 150))),
    (("Morbegno", "Sondrio"), (2023, ("luglio", 165)))
)

#calcolo media globale
def media_globale(tupla_pluviometrica):
    TotPrep = 0
    c = 0
    for i, data in tupla_pluviometrica:
        for anno, (mese, valore) in data:
            if anno == 2023 and valore != "N/D":
                TotPrep += valore
                c += 1
    if c == 0:
        return 0
    else:
        return TotPrep / c

#calcolo quantitativo medio pioggia
def media(tupla_pluviometrica, provincia, mese):
    TotPrep = 0
    c = 0

    for (città, provincia), data in tupla_pluviometrica:
        for anno, (mese, valore) in data:
            if provincia == provincia and mese == mese and valore != "N/D":
                TotPrep += valore
                c += 1
    if c == 0:
        return 0
    else:
        return TotPrep / c

#calcolo pioggia max
def pioggiaMax(tupla_pluviometrica):
    PrepMax = 0
    CittàMaxPrep = []

    for (città, prov), data in tupla_pluviometrica:
        for anno, (mese, valore) in data:
            if prov == "" and valore != "N/D" and valore > PrepMax:
               PrepMax = valore
               CittàMaxPrep = [(città, mese)]
            elif prov == "" and valore != "N/D" and valore == PrepMax:
                CittàMaxPrep.append((città, mese))

    return tuple(CittàMaxPrep)#creazione e restituzione della tupla per città max con valori

#calcolo pioggia min
def pioggiaMin(tupla_pluviometrica):
    PrepMin = 0
    MeseMin = []

    for mese in tupla_pluviometrica:
        for mese, valore in mese:
            if valore != "N/D" and valore < PrepMin:
                PrepMin = valore
                MeseMin = mese

    return tuple(MeseMin)#creazione e restituzione della tupla per mese min con valori


# def provinciaPer(tupla_pluviometrica): 



#Menu di scelta
while True:
    print("\nMenu:")
    print("1. Calcola la media globale delle precipitazioni nell'anno 2023")
    print("2. Calcola la media delle precipitazioni per provincia e mese")
    print("3. Trova la città e il mese più piovoso/i della provincia di Milano")
    print("4. Trova il mese con le precipitazioni più basse")
    print("5. Calcola la percentuale delle precipitazioni per provincia rispetto al totale")
    print("0. Esci")

    scelta = input("Inserisci il numero corrispondente all'azione desiderata: ")

    if scelta == "1":
        print(f"La media globale delle precipitazioni nell'anno 2023 è: {media_globale(tupla_pluviometrica)} mm")
    elif scelta == "2":
        provincia = input("Inserisci la provincia: ")
        mese = input("Inserisci il mese: ")
        print(f"La media delle precipitazioni per {provincia} nel mese di {mese} è: {media(tupla_pluviometrica, provincia, mese)} mm")
    elif scelta == "3":
        print(f"La città e il mese più piovoso della provincia di Milano sono: {pioggiaMax(tupla_pluviometrica)}")
    elif scelta == "4":
        print(f"Il mese con le precipitazioni più basse è: {pioggiaMin(tupla_pluviometrica)}")
    #elif scelta == "5":
        #print(f"Il calcolo della percentuale per provincia rispetto al totale è: {provinciaPer(tupla_pluviometrica)}")
    elif scelta == "0":
        break
    else:
        print("Scelta non valida. Riprova.")
        
    

