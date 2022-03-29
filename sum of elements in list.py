liste = []
n = int(input("sayı gir: "))

for i in range(1,n+1):
    g = int(input(" değeri gir: "))
    liste.append(g)
print(liste)    
toplam = 0
for i in range(n):
   
    toplam = toplam + liste[i]
    
print(toplam)    
    
tekrar = []
a = 0
for i in range(a,n):
    counter = 0
    for j in range(a+1,n):
        if liste[i]==liste[j]:
            counter +=1
            if counter>1:
                tekrar.append(liste[i])
        
        
        
print(tekrar)        

