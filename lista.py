#liste
lista= ['uno', 'due','tre']
lista.append ('quattro')
print(lista[-1])
print(lista[1:2])


#dizionario
dizionario={"nome":"luca", "età":"20"}
dizionario["occhi"]="due"
print(dizionario)
print(dizionario["nome"])

for key in dizionario.keys():
    print(key)

for items in dizionario.items():
    print(items)
    
for value in dizionario.values():
    print(value)
    
for key, value in dizionario.items():
    print(key +"-"+ value)