# -*- coding: utf-8 -*-
 
while True:
    sifre = input("Bir şifre giriniz: ")
    if len(sifre) < 4 or len(sifre) > 4:
        print("4 karakterden oluşan bir şifre girmelisiniz.")
        continue
    else:
        print("Şifreniz oluşturuldu: ", sifre)
        break;
print("Şifrenizi while döngüsü içinde oluşturdunuz. ")
