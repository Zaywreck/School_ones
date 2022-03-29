print("""

Hizmet türleri için;
a : Amazon Prime
b : Netflix
c : HBO
""")






def stream_a(int1):       #int'ler cihaz sayısı
    if (int1<=2):
        price_A = 7.99*12
        return price_A
    
    else:
        price_A = 12.99*12
        return price_A

def stream_b(int2):
    if (int2<=3):
        price_N = 12.99*12
        return price_N

    else:
        price_N = 14.99*12
        return price_N


def stream_c(int3):
    if (int3<=4):
        price_H = 14.99*12
        return price_H
    
    elif (5<=int3<10):
        price_H = 24.99*12
        return price_H


    elif (int3>10):
        price_H = 34.99*12
        return price_H

def main():
    x = str(input("Hangi hizmeti istediğinizi seçin: "))

    if (x =="a"):
        int1 = int(input("Lütfen cihaz sayısı girin: "))
        print(stream_a(int1))
        
    elif(x =="b"):
        int2 = int(input("Lütfen cihaz sayısı girin: "))
        print(stream_b(int2))
        
    elif(x =="c"):
        int3 = int(input("Lütfen cihaz sayısı girin: "))
        print(stream_c(int3))

main()

quit_app = input("Çıkmak için bir tuşa basın")
            



    
    
    
