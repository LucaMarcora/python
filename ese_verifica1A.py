dati_pluviometrici_lombardia = [
    ("Milano", [("gennaio", 10), ("febbraio", 15), ("marzo", "N/D"), ("aprile", "N/D")]),
    ("Brescia", [("gennaio", 5), ("febbraio", "N/D"), ("marzo", 18), ("aprile", 25)]),
]

def analizza_precipitazioni(citta, dati_pluviometrici):
    tupla_citta = None
    for tupla in dati_pluviometrici:
        if tupla[0] == citta:
            tupla_citta = tupla
            break
    #Se città non presenta returna nulla
    if tupla_citta == None:
        return ()

    somma = 0
    c = 0
    valore_max = 0
    mese_max = ""
    valore_min = 0
    mese_min = ""

    for mese, valore in tupla_citta[1]:
        # Verifica se il valore è disponibile
        if valore != "N/D":
            somma += valore
            c += 1

            # Aggiorna il massimo
            if valore > valore_max:
                valore_max = valore
                mese_max = mese

            # Aggiorna il minimo
            if valore < valore_min:
                valore_min = valore
                mese_min = mese

    # Calcola la media
    media = somma / c
    # Restituisci la tupla richiesta
    return (media, (valore_max, mese_max), (valore_min, mese_min))

risultato = analizza_precipitazioni("Milano", dati_pluviometrici_lombardia)
print(risultato)