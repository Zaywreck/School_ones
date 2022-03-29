"""def faktoriyel(x):
    if x == 0:
        return 1

    else:
        return x * faktoriyel(x-1)


print(faktoriyel(0))    



def liste_ters_dondurme(liste):
    if liste == []:
        return []
    else:
        return [liste[-1]]+liste_ters_dondurme(liste[:-1])


print(liste_ters_dondurme([1,2,3,4,5]))   """ 


sayi = int(input("sayı gir: "))
i =1
carpim = 1
while i <= sayi:
    carpim = i * carpim
    
    i = i + 1


print(carpim)    
