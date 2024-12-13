telefono={
    "Anna": "321",
    "Franco": "123",
    "F": "950",
}
print("---------------------------------------------------")
#faccio vedere all'utente cosa contiene il dizionario(telefono)
print("i numeri sulla rubrica sono:")
for key, value in telefono.items():
    print(f"{key}-{value}")
print("---------------------------------------------------")
#verifica se il numero inserito dall'utente sia esistente
num=input("cerca numero sulla rubrica:")
if (num in telefono.values()):
    print("numero esiste")
else:
    print("numero non esiste")
print("---------------------------------------------------")
#faccio immettere all'utente un nuovo contato
print("aggiungiamo un nuovo contato")
nome=input("inserire nome:")
num=input("inserire la numero:")
telefono[nome]=num
print("---------------------------------------------------")
#faccio vedere all'utente cosa contiene il dizionario(telefono)
print("i numeri sulla rubrica sono:")
for key, value in telefono.items():
    print(f"{key}-{value}")
print("---------------------------------------------------")
#il riodinamento del dizionario non lo saputo fareಥ_ಥ

