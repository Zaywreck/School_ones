def fonk1():
    string = str(input("Bir metin giriniz: "))
    return string

def fonk2(fonk1):
    sesli_harf = ['a','e','ı','i','u','ü','o','ö']


    y = list()
    for harf in fonk1:
       
     
       if harf in sesli_harf :
           y.append("*")
           
       else:
           y.append(harf)
           
           
    return y      
       
print(fonk2(fonk1()))    