def tabellina(n):
    for i in range(11):
        print(f"{n}*{i}={n*i}")
    print("----------------------------------------")

        
print("Che tabbelina vuoi sapere:\t")
n= int(input())
print("----------------------------------------")
tabellina(n)

def area_rettangolo(lung, larg):
    print("area del rettangolo è di:", lung*larg)
    
print("Calcoliamo l'area del rettangolo")
print("Dammi la base:\t")
b= float(input())
print("Dammi la alterza:\t")
h= float(input())
area_rettangolo(b, h)

def sommi():
    sum= 0
    for i in range(1, 101):
        sum+= i
    print(f"la somma di tutti i numeri da 1 a 100 è:{sum}")

sommi()

def is_pari():
    for i in range(1, 11):
        if i%2==0:
            print(f"il numero {i} è pari")
        else:
            print(f"il numero {i} è dispari")


#is_pari()