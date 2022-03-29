#coding=utf-8
duzyazi = input("Lütfen cümle veya kelime giriniz: ")
tersyazi = ""
def tersalma(yazi, ters):
    for i in range(len(yazi) - 1, -1, -1):
        ters = ters + yazi[i]
    return ters
terscevrilmisversiyonu = tersalma(duzyazi, tersyazi)
print("Ters Çevrilmiş Hali: {} ".format(terscevrilmisversiyonu))

