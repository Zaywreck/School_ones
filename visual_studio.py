"""number = 40 / 76
x = round(number,2) # sayı yuvarlama
print(x)
"""

"""website = "https://www.MertGulle.com.tr"

sonuc = website[-6:]  #string slice

print(sonuc)"""
# ctrl + k + c => olduğu dizini yorum satırı yapma 
# ctrl + k + u => yorum dizinini normal dizin yapma


#string metodları

string = "merhaba benim adım mert!"

# sonuc = string.upper()                = tüm harfleri büyük yapma
# sonuc = string.lower()                = tüm harfleri küçük yapma
# sonuc = string.isupper()              = tüm harfler büyük mü sorgusu
# sonuc = string.islower()              = tüm harfler küçük mü sorgusu (eğer içinde 'is' varsa sorgu yapmadır!!)
# sonuc = string.title()                = tüm kelimelerin ilk harflerini büyük yapma
# sonuc = string.capitalize()           = cümlenin ilk harfini büyük yapma
# sonuc = string.isdigit()              = tüm karakterler rakam mı sorgusu
# sonuc = string.istitle()              = string ifade title mı(tüm baş harfler büyük) sorgusu
# sonuc = string.isspace()              = boşluk var mı sorgusu
# sonuc = string.strip()                = baştaki ve sondaki boşlukları silme. lstrip soldan rstrip sağdan boşluk siler
# sonuc = string.split()                = boşluklardan ayırıp liste yapma (parametre olarak ayırmak istediğimiz eleman girilebilir mesela split('.') noktaya göre ayırma yapar)
# sonuc(bir liste) = "---".join(sonuc)  = listedeki elemanların arasına 3 tane - koyarak stringe dönüştürür(- yerine istediğimizi yazabiliriz)
# index = string.index("adım")          = belirtilen kelimenin kaçıncı indisten itibaren başladığını verir
# sonuc = string.startswith("m")        = eğer dizi m ile başlıyor ise true döner herhangi bir parametre verilebilir
# sonuc = string.endsswith("m")         = eğer dizi m ile bitiyor ise true döner herhangi bir parametre verilebilir
# sonuc = string.replace('e','y')       = e eski değer y yeni değer olmak üzere stringin içindeki elemanları değiştirir.Yan yana yazılabilir .replace().replace
# sonuc = string.count("ifade")         = gönderdiğimiz ifadenin string içinde kaç defa tekrar ettiği bilgisini verir
# sonuc = string.find("ifade",0,10)     = parametre olan ifade var mı yok mu varsa kaçıncı indisten başlıyor yoksa -1 döndürür.aralık belirtebiliriz 0,10 gibi 
# sonuc = string.isalpha()              = string içindeki karakterlerin tümü alfabetik mi sorgusu
# sonuc = "şey".center(topkar,'*')      = şey ifadesini ortaya koyar ve toplam karakter sayısına uyacak şekilde sağ ve soluna yıldız ekler farklı bir şey de ekletebiliriz


print(sonuc)