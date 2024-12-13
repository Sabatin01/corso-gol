parole={
    "casa": 0,
    "albero": 0,
    "cane": 0
}
print("-------------------------------------------------")
#faccio vedere all'utente cosa contiene il dizionario(parole)
#solo chiavi
for key in parole.keys():
    print(key)
print("-------------------------------------------------")
#creo 2 for
#il primo for serve per scruttare il dizionario
for key in parole.keys():
    a=0
    #il secondo for serve a vedere quanto è lunga la parona
    for i in key:
        a+=1
    #infine viene modificata il valore della parola
    parole[key]=a
#faccio vedere il risultato
for key, value in parole.items():
    print(f"{key}-{value}")
print("-------------------------------------------------")
