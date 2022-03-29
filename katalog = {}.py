katalog = {}
while True:
    urun_id = str(input("ürün id girin: "))
    urun_ad = str(input("ürün adı: "))
    urun_fiyat = float(input("ürün fiyatı: ")) 
    katalog[urun_id] = {'ad':urun_ad,'fiyat':urun_fiyat}
    karar = str(input("ürün eklemek için enter'a basın bitirmek için bitir yazın: "))
    if karar == 'bitir':
        print(katalog)
        break


# ürün arama 
id = input("aramak istediğiniz ürün: ")
urun = katalog[id]

print(f"id: {id} {katalog[id]} ")

