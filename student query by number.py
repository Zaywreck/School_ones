#numara ile öğrenci sorgusu
ogrenci = []
numara = []
yas = []
tumsistem = {}
while True:
    x = str(input("Öğrenci adı soyadı: "))
    y = int(input("Öğrenci numarası: "))
    z = int(input("Öğrenci yaşı: "))
    ogrenci.append(x)
    numara.append(y)
    yas.append(z)
    tumsistem[y] = [x,z]
    karar = str(input("Öğrenci eklemek için enter'a basın.Bitirmek için 'bitir yazın': "))
    if karar == 'bitir':
        tumsistem['Öğrenciler'] = ogrenci
        tumsistem['Numaralar'] = numara
        tumsistem['Yaş'] = yas
        #print(tumsistem)
        for x,y in tumsistem.items():
            print(x,y)

        break
    