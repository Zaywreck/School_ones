ogrenci = []
numara = []
yas = []
ortalama =[]
tumsistem = {}
while True:
    x = str(input("Öğrenci adı soyadı: "))
    y = int(input("Öğrenci numarası: "))
    z = int(input("Öğrenci yaşı: "))
    t = float(input("Öğrenci ortalaması: "))
    ogrenci.append(x)
    numara.append(y)
    yas.append(z)
    ortalama.append(t)
    karar = str(input("Öğrenci eklemek için enter'a basın.Bitirmek için 'bitir yazın': "))
    if karar == 'bitir':
        tumsistem['Öğrenciler'] = ogrenci
        tumsistem['Numaralar'] = numara
        tumsistem['Yaş'] = (yas)
        tumsistem['Ortalamalar'] = (ortalama)
        print(tumsistem)
        break
    