def incrementa():
    a= 1
    c= 0
    while True:
        print ("------------------------------------------------------------")
        print (f"Il tuo numero è arrivato a: {a}")
        print ("Inserire numeri per continuare (con 0 termini):")
        b= int(input())
        a+= a
        print ("------------------------------------------------------------")
        if b == 0:
            break
        else:
            c+=1
            print("Ripetizione n°", c)
                   
def condronta():
    print ("Inserire numero (a):")
    a= float(input())
    print ("Inserire numero (b):")
    b= float(input())
    somma(a)
    if a>b:
        print (1)
    else:
        print (0)
        
def somma(num1):
    sum = num1 + 50
    print(f"somma: {sum}")

x= 'mela'
lettere= 0
for i in x:
    lettere+=1
print (f"le lettere sono:{lettere}")