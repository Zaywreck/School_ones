dizi = "Samsun Üniversitesi Yazılım Mühendisliği"
def fonk(dizi):
    sozluk = {}
    x = dizi.lower()
    for letter in x:
        if letter in sozluk:
            sozluk[letter] += 1
        else:
            sozluk[letter] = 1
        
    print(sozluk)
        
fonk(dizi)