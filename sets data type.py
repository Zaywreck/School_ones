#sets veri tipi

meyveler = {"üzüm","kiraz","vişne","kavun","karpuz","armut"}

sonuc = meyveler
sonuc = 'elma' in meyveler # True ya da False döner içinde var mı yok mu diğer veri tiplerinde de kullanılabilir
# sonuc = meyveler[0] indekslenemez
meyveler.add("ananas")
meyveler.update(["erik","elma"])
sonuc = len(meyveler)
meyveler.remove('karpuz')#eğer içinde yoksa hata verir
meyveler.discard('karpuz')#içinde varsa siler yoksa devam eder

print(sonuc)