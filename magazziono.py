#diario di un magazzino
magazzino={
    "sale":5,
    "pane":2,
    "olio":6
}
print("---------------------------------------------------")
#faccio vedere cosa contiene il dizionario(magazzino)
print("i prodotti sono:")
for key, value in magazzino.items():
    print(f"{key}-{value}")
print("---------------------------------------------------")
#chiedo all'utente l'aggiunta di un nuovo prodotto e la sua quantita
print("aggiungiamo un nuovo prodotto")
prod=input("inserire prodotto:")
num=input("inserire la quantità:")
magazzino[prod]=num
print("---------------------------------------------------")
#faccio vedere le modifiche fatte
print("i prodotti sono:")
for key, value in magazzino.items():
    print(f"{key}-{value}")
print("---------------------------------------------------")
#chiedo all'utente la modifica di quantita del pane
print("modifichiamo la quantità di un prodotto prodotto (pane)")
num=input("aggiungi la nuova quantità:")
magazzino["pane"]=num
print("---------------------------------------------------")
#faccio vedere le modifiche fatte
print("i prodotti sono:")
for key, value in magazzino.items():
    print(f"{key}-{value}")
print("---------------------------------------------------")
#cancella tutti i prodotti con valore 0 (non funziona)
print("ora rimoviamo i prodotti con valore 0")
for key, value in magazzino.items():
    if value == '0':
        del magazzino[key]
print("---------------------------------------------------")
#faccio vedere le modifiche fatte
print("i prodotti sono:")
for key, value in magazzino.items():
    print(f"{key}-{value}")