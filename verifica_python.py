vendite_mensili = [ ("Alimentare", [("Gennaio", "N/D"),("Febbraio", 3000), ("Marzo",2500)])
                    ("Vestiario", [("Gennaio", 3000),("Febbraio", "N/D"), ("Marzo",4000)])
                    ("Igiene", [("Gennaio", 1500),("Febbraio", 1000), ("Marzo","N/D")])
]

def calcola_media_vendite(vendite_mensili, reparto):
    for rep, vendite in vendite_mensili:
        if rep == reparto:
            venditeTot = 0
            c = 0
            max_vendite = 0
            max_mese = ""
            min_vendite = 0
            min_mese = ""
            

            for mese, valore in vendite:
                if valore != "N/D":
                    venditeTot += valore
                    c += 1

                    if valore > max_vendite:
                        max_vendite = valore
                        max_mese = mese

                    if valore < min_vendite:
                        min_vendite = valore
                        min_mese = mese

            if c > 0:
                media = venditeTot / c
                return (media, (max_vendite, max_mese), (min_vendite, min_mese))
            else:
                return () #questa parte è sbagliata dovrei fare il return con il clear ma non mi ricordo come si fa 

reparto_cercato = input("Inserisci il nome del reparto: ")

ris = calcola_media_vendite(vendite_mensili, reparto_cercato)

if ris:
    print("Risultato:")
    print(ris)
else:
    print(f"Nessun dato trovato per il reparto {reparto_cercato}.")


    


