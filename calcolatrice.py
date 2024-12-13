def add():
    #si richiede all'utente di inserire i due numeri da addizionare
    print("Dammi il primo numero:")
    a= float(input())
    print("Dammi il secondo numero:")
    b= float(input())
    #si stampa all'utente il risutato
    print(f"ADDIZIONE:{a+b}")
    
def sott():
    #si richiede all'utente di inserire i due numeri da sottrare
    print("Dammi il primo numero:")
    a= float(input())
    print("Dammi il secondo numero:")
    b= float(input())
    #si stampa all'utente il risutato
    print(f"SOTTRAZIONE:{a-b}")
    
def molt():
    #si richiede all'utente di inserire i due numeri da moltiplicare
    print("Dammi il primo numero:")
    a= float(input())
    print("Dammi il secondo numero:")
    b= float(input())
    #si stampa all'utente il risutato
    print(f"MOLTIPLICAZIONE:{a*b}")
    
def div():
    #si richiede all'utente di inserire i due numeri da dividere
    print("Dammi il primo numero:")
    a= float(input())
    print("Dammi il secondo numero:")
    b= float(input())
    #si fa un confronto in caso in cui la b è uguale a 0 dare errore
    if (b == 0):
        print("DIVISIONE: ERROR")
    else:#se b non è 0 stampare il risultato all'utente
        tot= a/b
        print(f"DIVISIONE:{a/b}")
        
def menu():
    #qui sono tutte le operazione che l'utente puo svolgere
    print("1.Addizione")
    print("2.Sottrazione")
    print("3.Moltiplicazione")
    print("4.Divisione")
    print("5.Esci")
    
while True:
    print("-----------------------------------------------------------------")
    #richiama la funzione menu
    menu()
    #si chiede all'utente di sceglire l'operazione desiderta
    scelta = input("Inserire il numero relativo all'operatore:")
    print("-----------------------------------------------------------------")
    #in base a cosa ha scelto l'utente vine richiamata la funzione richiesta
    if scelta == '1':
        add()
        print("-----------------------------------------------------------------")
    elif scelta == '2':
        sott()
        print("-----------------------------------------------------------------")
    elif scelta == '3':
        molt()
        print("-----------------------------------------------------------------")
    elif scelta== '4':
        div()
        print("-----------------------------------------------------------------")
    #in caso l'utente scelga 5 chiedere il programma
    elif scelta== '5':
        break
        