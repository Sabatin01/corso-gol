def somma():
    print("Dammi il primo numero:")
    num1= float(input())
    print("Dammi il secondo numero:")
    num2= float(input())
    tot= num1+num2
    print("ADDIZIONE:", tot)
    
def sott():
    print("Dammi il primo numero:")
    num1= float(input())
    print("Dammi il secondo numero:")
    num2= float(input())
    tot= num1-num2
    print("SOTTRAZIONE:", tot)
    
def molt():
    print("Dammi il primo numero:")
    num1= float(input())
    print("Dammi il secondo numero:")
    num2= float(input())
    tot= num1*num2
    print("SOMOLTIPLICAZIONE:", tot)
    
def div():
    print("Dammi il primo numero:")
    num1= float(input())
    print("Dammi il secondo numero:")
    num2= float(input())
    if (num2 == 0):
        print("DIVISIONE: ERROR")
    else:
        tot= num1/num2
        print("DIVISIONE:", tot)

print("1.ADDIZIONE")
print("2.SOTTRAZIONE")
print("3.MOLTIPLICAZIONE")
print("4.DIVISIONE")
print("Scegli l'operazione che vuoi:")
i= float(input())
if i<1:
    print("Oerazione non selezionata")
else:
    if i>4:
        print("Oerazione non selezionata")
    else:
        if i==1:
            somma()
        else:
            if i==2:
                sott()
            else:
                if i==3:
                    molt()
                else:
                    div()
