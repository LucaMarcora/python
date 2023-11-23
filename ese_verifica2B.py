tupla_vendite = [
    ("Prodotto A", ("contanti", 1000)),
    ("Prodotto B", ("carta di credito", 1500)),
    ("Prodotto C", ("carta di credito", 1200)),
    ("Prodotto D", ("contanti", 200)),
    ("Prodotto E", ("contanti", 800)),
    ("Prodotto F", ("N/D", 200)),
    ("Prodotto A", ("contanti", 1500)),
    ("Prodotto B", ("carta di credito", 900))
]

def media_globale(tupla_vendite):
    importi = [vendita[2][1] for vendita in tupla_vendite]
    return sum(importi) / len(importi) 

def media(tupla_vendite, categoria, tipologia_pagamento):
    importi = [vendita[2][1] for vendita in tupla_vendite if vendita[0][1] == categoria and vendita[1][1][0] == tipologia_pagamento]
    return sum(importi) / len(importi) 

def venditaMax(tupla_vendite):
    max_vendita = max(tupla_vendite)
    return max_vendita

def venditaMin(tupla_vendite):
    repartoA_vendite = [vendita for vendita in tupla_vendite if vendita[0][0] == "RepartoA"]
    min_vendita = min(repartoA_vendite)
    return min_vendita

#La percentuale delle vendite non so come farla 

# Menu di scelta
while True:
    print("\nMenu:")
    print("1. Calcola l'importo medio globale delle vendite")
    print("2. Calcola l'importo medio per categoria e tipologia di pagamento")
    print("3. Trova la vendita massima")
    print("4. Trova la vendita minima in RepartoA")
    print("0. Esci")

    scelta = input("Inserisci il numero corrispondente all'operazione desiderata: ")

    if scelta == "1":
        print("Media globale delle vendite:", media_globale(tupla_vendite))
    elif scelta == "2":
        categoria = input("Inserisci la categoria: ")
        tipologia_pagamento = input("Inserisci la tipologia di pagamento (contanti o carta di credito): ")
        print("Media delle vendite per categoria e tipologia di pagamento:", media(tupla_vendite, categoria, tipologia_pagamento))
    elif scelta == "3":
        vendita_max = venditaMax(tupla_vendite)
        print("Vendita massima:", vendita_max[1][0], "con importo:", vendita_max[1][1][1])
    elif scelta == "4":
        vendita_min = venditaMin(tupla_vendite)
        print("Vendita minima in RepartoA:", vendita_min[1][0], "con importo:", vendita_min[1][1][1])
    elif scelta == "0":
        break
    else:
        print("Scelta non valida. Riprova.")