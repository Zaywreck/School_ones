def liste_yapma():
    liste1 = list()
    liste2 = list()
    for i in range(0,10):
        x = int(input("ilk liste için bir eleman giriniz: "))
        liste1.append(x)
    for j in range(0,10):
        y = int(input("ikinci liste için bir eleman giriniz: "))
        liste2.append(y)

    ortak_bulma_toplama(liste1,liste2)

    
   


def ortak_bulma_toplama(liste1,liste2):
    ortak = list()
    toplam = 0
    for a in range(len(liste1)):
        for b in range(len(liste2)):
            if liste1[a]==liste2[b]:
                ortak.append(liste1[a])


    for t in range(len(ortak)):
        toplam = toplam + ortak[t]

    print("ortak eleman: ",ortak,"toplam: ",toplam)


liste_yapma()



    

        

                

                
                
            
    
    





    
    
