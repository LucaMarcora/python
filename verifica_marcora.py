class Articolo:
  def __init__(self, codice, fornitore, marca,prezzo, quantita): # 1 Implementa il costruttore
    self.codice = codice 
    self.fornitore = fornitore
    self. marca = marca 
    self.prezzo = prezzo
    self.quantita = quantita

  def scheda_articolo(self): # 2 Ritorna una stringa contenente gli attributi dell'articolo
    return f"""
    Codice: {self.codice}
    fornitore: {self.fornitore}
    marca: {self.marca}
    prezzo: {self.prezzo}
    quantità: {self.quantita}"""

  def modifica_scheda(self): # 3 Permette di modificare gli attributi dell'articolo
     while True:
        print("\nMenu:")
        print("1. Modifica fornitore. ")
        print("2. Modifica marca. ")
        print("3. Modifica prezzo. ")
        print("4. Modifica quantità. ")
        print("0. Esci")
        scelta = input("Scegli un'opzione: ")
        if scelta == "1":
            nuovo_fornitore = input(f'Nuovo fornitore: ')
            self.fornitore = nuovo_fornitore
        elif scelta == "2":
            nuova_marca = input(f'Nuova marca: ')
            self.marca = nuova_marca
        elif scelta == "3":
            nuovo_prezzo = float(input(f'Nuovo prezzo: '))
            self.prezzo = nuovo_prezzo
        elif scelta == "4":
            nuova_quantita = float(input(f'Nuova quantità: '))
            self.quantita = nuova_quantita
        elif scelta == "0":
            print("Uscita dal menù.")
            break
        else:
            print("Scelta non valida. Riprova.")

# Codice controllato alle 09:29 dal prof. Spinarelli ^^

class Televisore(Articolo):
    def __init__(self, codice, fornitore,marca,prezzo,quantita,pollici,tipo): # 4 Implementa il costruttore
      super().__init__(codice, fornitore, marca, prezzo, quantita)
      self.pollici = pollici
      self.tipo = tipo

    def scheda_articolo(self): # 5 Ritorna una stringa contenente gli attributi del televisore
      return f"""
      Codice: {self.codice}
      fornitore: {self.fornitore}
      marca: {self.marca}
      prezzo: {self.prezzo}
      quantità: {self.quantita}
      pollici: {self.pollici}
      tipo: {self.tipo}"""
    
# Codice controllato alle 09:36 dalla prof. Invernizzi ^^

class Frigorifero(Articolo):
  def __init__(self, codice, fornitore, marca, prezzo, quantita,dimensioni,modello): # 6 Implementa il costruttore
      super().__init__(codice, fornitore, marca, prezzo, quantita)
      self.dimensioni = dimensioni 
      self.modello = modello

  def scheda_articolo(self):   # 7 Ritorna una stringa contenente gli attributi del frigorifero
      return f"""
      Codice: {self.codice}
      fornitore: {self.fornitore}
      marca: {self.marca}
      prezzo: {self.prezzo}
      quantità: {self.quantita}
      pollici: {self.dimensioni}
      tipo: {self.modello}"""     


t1 = Televisore(1,"Fornitore 1","Sony",700,10,40,"Schermo piatto")
print(t1.scheda_articolo())
t1.modifica_scheda()
print(t1.scheda_articolo())

# Codice controllato alle 09:41 dal prof. Spinarelli (funzionalità testate e funzionanti)^^
# ----------------------------------------------------------------------------------------------------------------------------------------------------

class Ordine():
  def __init__(self,codice,data, piva,indirizzo): # 8 Implementa il costruttore
    self.codice = codice
    self.data = data
    self.piva = piva
    self.indirizzo = indirizzo
    self.lista_articoli = []

  def aggiungi_articolo(self,articolo): # 9 Completa il metodo aggiungendo l'oggetto alla lista e stampando il messaggio opportuno
    if isinstance(articolo,Televisore):
      if(articolo not in self.lista_articoli):
        self.lista_articoli.append(articolo)
      else:
        print("Articolo già presente. ")

    elif isinstance(articolo,Frigorifero):
      if(articolo not in self.lista_articoli):
        self.lista_articoli.append(articolo)
      else:
        print("Articolo già presente. ")
    print(f"Articolo agggiunto con successo: {articolo.scheda_articolo()}")
    
  def rimuovi_articolo(self,articolo): # 10 Implementa il metodo
    if isinstance(articolo,Televisore):
      if(articolo in self.lista_articoli):
        self.lista_articoli.remove(articolo)
        print("Articolo rimosso con successo ")
      else:
        print("Articolo non trovato. ")

    elif isinstance(articolo,Frigorifero):
      if(articolo in self.lista_articoli):
        self.lista_articoli.remove(articolo)
        print("Articolo rimosso con successo ")
      else:
        print("Articolo non trovato. ")

  def importo_ordine(self): # 11 Stampa il numero di articoli e per ogni articolo l'importo (prezzo*quantita)
      totale = 0
      tot_articoli = 0
      for articolo in self.lista_articoli:
        tot_articoli += 1
        tot_importo = articolo.prezzo * articolo.quantita
        totale += tot_importo
      print(f"Articolo: {articolo}, Importo: {tot_importo} €")
      print(f"Importo totale dell'ordine: {totale} €")
      return [(tot_articoli, tot_importo)]

  def dettaglio_ordine(self): # 12 Stampa i dettagli dell'ordine e restituisce una lista contenente / [somma importi televisori, somma importi frigoriferi, somma importi totali ]
      sommaT = 0
      sommaF = 0
      for articolo in self.lista_articoli:
        importo = articolo.prezzo * articolo.quantita
        if isinstance(articolo, Televisore):
            sommaT += importo
        elif isinstance(articolo, Frigorifero):
            sommaF += importo
        totale = sommaT + sommaF

      print(f"Dettaglio Vendita:")
      print(f"Somma dei televisori: €{sommaT:.2f}")
      print(f"Somma dei frigoriferi: €{sommaF:.2f}")
      print(f"Somma del totale: €{totale:.2f}")
      return([self.sommaT,self.sommaF,self.sommaT+self.sommaF])

t2 = Televisore(2,"Fornitore 2","Samsung",1000,5,80,"Schermo curvo")
f1 = Frigorifero(3,"Fornitore 3","Bosch",750,12,'790x2000x600','Ultra')
f2 = Frigorifero(4,"Fornitore 4","Ariston",550,10,'590x1600x500','Medium')

ordine1=Ordine(1,"24/02/2022",'213143','Via della consegna 1')
ordine1.aggiungi_articolo(t1)
ordine1.aggiungi_articolo(t2)
ordine1.aggiungi_articolo(f1)
ordine1.aggiungi_articolo(f2)
ordine1.rimuovi_articolo(f2)
ordine1.rimuovi_articolo(f2)

#13 Risposta al Punto 1 : Per un ordine: il numero di articoli presenti e
# l'importo totale senza distinguere il tipo di articolo
ordine1.importo_ordine()
#14 Risposta punto 2.   Per un ordine: il dettaglio degli articoli, l'importo totale,
# l'importo dei televisori e l'importo dei frigoriferi.
importi=ordine1.dettaglio_ordine()
print("--------------------------")
print(f"\nImporto televisori= {importi[0]}")
print(f"\nImporto frigoriferi= {importi[1]}")
print(f"\nImporto totale= {importi[2]}")

# Controllato alle ore 10:47 dal prof. Spinarelli (funzionalità testate ma funzionanti correttamente solo aggiungi e rimuovi) ^^
# ----------------------------------------------------------------------------------------------------------------------------------------------------

class Ordini():
  def __init__(self,nome_negozio,codice_negozio): # 16 Implementa il costruttore
    self.nome = nome_negozio
    self.codice_negozio = codice_negozio
    self.lista_ordini = []

  def aggiungi_ordine(self,ordine): # 17 Implementa il metodo
    self.lista_ordini.append(ordine)
    print(f"Ordine aggiunto: codice ordine {ordine.codice} - data {ordine.data}")

  def rimuovi_ordine(self,ordine): # 18 Implementa il metodo
    if ordine in self.lista_ordini:
       self.lista_ordini.remove(ordine)
       print(f"Ordine rimosso. ")
    else:
       print("Ordine non trovato. ")    

  def totale_ordini(self): # 19 Implementa il metodo
    totT = 0 #totale televisori
    totF = 0 #totale frigoriferi
    tot = 0
    for ordine in self.lista_ordini:
      tot += 1
    importo = ordine.dettaglio_ordine()
    totT = importo[0]
    totF = importo[1]
    tot = totT + totF
    return ([self.totT,self.totF,self.tot])

ordini_negozio=Ordini("Megastore vendita ",1)
ordini_negozio.aggiungi_ordine(ordine1)
ordini_negozio.rimuovi_ordine(ordine1)
ordini_negozio.rimuovi_ordine(ordine1)
ordini_negozio.aggiungi_ordine(ordine1)


t3 = Televisore(5,"Fornitore 5","LG",600,4,70,"Schermo curvo")
f3 = Frigorifero(6,"Fornitore 6","Bosch",450,10,'490x1000x400','Small')
ordine2=Ordine(2,"25/02/2022",'213113','Via della consegna 2')
ordine2.aggiungi_articolo(t3)
ordine2.aggiungi_articolo(f3)

ordini_negozio.aggiungi_ordine(ordine2)

# 20 Riposta punto 3: Per tutti gli ordini del negozio mostra
# il dettaglio degli articoli, l'importo totale,
# l'importo dei televisori e l'importo dei frigoriferi.
importiTotali=ordini_negozio.totale_ordini()
print("--------------------------")
print(f"\nImporto totale televisori= {importiTotali[0]}")
print(f"\nImporto totale frigoriferi= {importiTotali[1]}")
print(f"\nImporto totale tutti gli ordini= {importiTotali[2]}")

# Controllato alle ore 11:01 dal prof. Spinarelli (funzionalità testate e funzionanti tranne per la risposta 20 punto 3)^^^
