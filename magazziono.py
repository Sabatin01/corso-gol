#diario warehouse dove all'interno c'è l'inventario
warehouse={
    "Elettronica": {"Laptop": 10, "Smartphone": 20},
    "Abbigliamento": {"Maglietta": 50, "Jeans": 30},
    "Cibo": {"Mela": 30, "Pane": 25}
}
ordiniMat= ["prodotto"]
ordiniQua= ["quantita"] 

#visualiza i prodotti in magazzino
def visualizza():
    print("i prodotti sono:")
    #con il primo ciclo for vado a prendere le chiavi principali
    for key in warehouse.keys():
        #stampo la chiave dove si trova l'indicatore
        print(f"\n{key}:")
        #secondo for serve per vedere le sotto categorie
        for chaive,val in warehouse[key].items():
            #vado a stampare tutte le sottocategorie presenti
            print(f"-{chaive}: {val}")
        
            
#funzione serve ad aggiungere nuovi prodotti 
def aggiungi():
    ind= 0
    #con questo ciclo for faccio vedere all'utente quali sono i campi da operare
    for key in warehouse.keys():
        ind+= 1
        print(f"{ind}. {key}")
    #una vota fatto vedere sarà all'utente decidere cosa aggiungere
    categoria= input("scrivere quale è la cattegoria con cuoi lavorare(inserire una nuova se non c'è): ")
    prodotto= input("inserire il nuovo prodotto: ")
    quantita= int(input("inserire la quantita: "))
    warehouse[categoria][prodotto]=quantita
    print("---------------------------------------------------")
    print("operazione riuscità\n")
    visualizza()

#funzione serve a rimuovere i prodotti   
def rimuovi():
    ind= 0
    #con questo ciclo for faccio vedere all'utente quali sono i campi da operare
    for key in warehouse.keys():
        ind+= 1
        print(f"{ind}. {key}")
    #una vota fatto vedere sarà all'utente decidere dove operare
    categoria= input("scrivere quale è la cattegoria con cuoi lavorare: ")
    #qualora l'utente sbaglia categoria lo si manda al management()
    if(categoria not in warehouse):
        print("---------------------------------------------------")
        print("categoria non trovato\n")
        visualizza()
        return
    #con questo ciclo for faccio vedere all'utente quali sono i campi da operare
    for key in warehouse[categoria].keys():
        ind+= 1
        print(f"{ind}. {key}")
    #una vota fatto vedere sarà all'utente decidere dove operare
    prodotto= input("scrivere quale prodotto devo cancellare: ")
    print("---------------------------------------------------")
    #qualora c'è il prodotto allora questo viene cancellato
    #altrimenti se l'utente sbaglia prodotto lo si manda al management()
    if(prodotto in warehouse[categoria]):
        del warehouse[categoria][prodotto]
        print("operazione riuscità\n")
        #mostro all'utente le modifica fatte
        visualizza()
    else:
        print("prodoto non trovato\n")
    
    
#funzione serve ad aggiornare i prodotti    
def aggiorna():
    ind= 0
    #con questo ciclo for faccio vedere all'utente quali sono i campi da operare
    for key in warehouse.keys():
        ind+= 1
        print(f"{ind}. {key}")
    #una vota fatto vedere sarà all'utente decidere dove operare
    categoria= input("scrivere quale è la cattegoria con cuoi lavorare: ")
    #qualora l'utente sbaglia categoria lo si manda al management()
    if(categoria not in warehouse):
        print("---------------------------------------------------")
        print("categoria non trovato\n")
        visualizza()
        return
    #con questo ciclo for faccio vedere all'utente quali sono i campi da operare
    ind= 0
    for key in warehouse[categoria].keys():
        ind+= 1
        print(f"{ind}. {key}")
    prodotto= input("scrivere quale prodotto devo aggiornare: ")
    #qualora l'utente sbaglia prodotto lo si manda al management()
    if(prodotto  not in warehouse[categoria]):
        print("---------------------------------------------------")
        print("prodoto non trovato\n")
    #altrimenti si fa vedere all'utente la modifica
    else:
        quantita= int(print("scrivi la quantità da modificare"))
        warehouse[categoria][prodotto]=quantita
        print("---------------------------------------------------")
        print("operazione riuscità\n")
    visualizza()
    
#funzione serve per le operazioni di management
def management():
    while True:
        print("---------------------------------------------------")
        #menu per far vedere all'utente cosa puo fare
        print("MENU")
        print("1. Mostra prodotti")
        print("2. Aggiungi nuovo prodotto")
        print("3. Rimuovi prodotto")
        print("4. Aggiorna prodotto")
        print("5. Esci")
        b=int(input("Cosa vuoi fare: "))
        if (b == 1):
            print("---------------------------------------------------")
            visualizza()
        elif (b == 2):
            print("---------------------------------------------------")
            aggiungi()
        elif (b == 3):
            print("---------------------------------------------------")
            rimuovi()
        elif (b == 4):
            print("---------------------------------------------------")
            aggiorna()
        elif (b == 5):
            return()
        else:
            print("Comando sbagliato riprova")

def ordina():
    visualizza()
    categoria= input("selezionare cattegoria voluta: ")
    if(categoria not in warehouse):
        print("Errore: categoria non trovata\n")
        return
    prodotto= input("selezionare cattegoria voluta: ")
    if(prodotto not in warehouse[categoria]):
        print("Errore: prodotto non trovata\n")
        return
    quantita= int(input("quantità voluta: "))
    num= warehouse[categoria][prodotto]
    if(quantita > warehouse[categoria][prodotto]):
        print("Quantità non disponibile\n ")
    num= quantita-num
    warehouse[categoria][prodotto]= num
    print("ordine effettuato")
    
    
def order():
    while True:
        print("---------------------------------------------------")
        #menu per far vedere all'utente cosa puo fare
        print("MENU")
        print("1. Ordina prodotti")
        print("2. Cronologia")
        print("3. Esci")
        b=int(input("Cosa vuoi fare: "))
        if (b == 1):
            print("---------------------------------------------------")
            ordina()
        elif (b == 2):
            print("---------------------------------------------------")
            history()
        elif (b == 3):
            return()
        else:
            print("Comando sbagliato riprova")
    
while True:
    #scelta dell'utente
    print("---------------------------------------------------")
    print("1. Management")
    print("2. Ordinare")
    print("3. Spegni")
    a=int(input("Cosa vuoi fare: "))
    if (a == 1):
        management()
    elif (a == 2):
        order()
    elif (a == 3):
        break
    else:
        print("Comando sbagliato riprova")
