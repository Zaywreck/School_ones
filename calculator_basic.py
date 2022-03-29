print("""
      HOŞGELDİNİZ
LÜTFEN BİR İŞLEM SEÇİN
1-TOPLAMA
2-ÇIKARMA
3-BÖLME
4-ÇARPMA
""")

def toplama (s1, s2):
    print(s1 + s2)
def cikarma (s1, s2):
    print(s1 - s2)
def bolme (s1, s2):
    print(s1 / s2)
def carpma (s1, s2):
    print(s1 * s2)
i = 1
while i<3:
    secim = int(input("lütfen bir islem seciniz: "))
    s1 = float(input("birinci sayi giriniz: "))
    s2 = float(input("ikinci sayi giriniz:  "))
    
if secim == 1 :
    callable(toplama(s1, s2))
elif secim == 2 :
    callable(cikarma(s1, s2))
elif secim == 3 :
    callable(bolme(s1, s2))
elif secim == 4 :
    callable(carpma(s1, s2))    
    
