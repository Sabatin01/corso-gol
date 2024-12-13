import array as vet

#v= arr.array('i')
#for i in range (1, 11):
#    v.append(i)
#print (v)
#print ("\n")    
#for i in range (0, len(v)):
#    print(v[i])  
#print(f"{v[-1]}") 
#print ("\n") 
#print (f"{v[1:3]}")

def sommaTot():
    v= vet.array('i',[1,20,30,50])
    tot= 0
    for i in range (0, len(v)):
        tot+= v[i]
    print(f"il risultato dei numeri dentro il vettore(1, 20, 30, 50) è: {tot}")
    
#sommaTot()

def aggiungiVal():
    v= vet.array('i', [1, 5])
    print("i valori dento al sono: 1, 5")
    a= int(input("\n inderire elemneto da mettere nel vettore:"))
    v.append(a)
    print("\n i valori dento al sono:")
    for i in (0, len(v)):
        print(v[i])
        
aggiungiVal()

