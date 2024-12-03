kullanicilar = {}
arkadaslar = {}
mesajlar = {}

def kayit_ol():
    kullanici_adi = input("Kullanıcı adı giriniz: ")
    sifre = input("Şifre giriniz: ")
    
    if kullanici_adi in kullanicilar:
        print("Bu kullanıcı adı zaten mevcut!")
    else:
        kullanicilar[kullanici_adi] = sifre
        arkadaslar[kullanici_adi] = []
        mesajlar[kullanici_adi] = []
        print(f"{kullanici_adi} başarıyla kaydoldu!")

def giris_yap():
    kullanici_adi = input("Kullanıcı adı: ")
    sifre = input("Şifre: ")
    
    if kullanici_adi in kullanicilar and kullanicilar[kullanici_adi] == sifre:
        print(f"Hoş geldin, {kullanici_adi}!")
        return kullanici_adi
    else:
        print("Kullanıcı adı veya şifre yanlış!")
        return None

def arkadas_ekle(kullanici):
    yeni_arkadas = input("Eklemek istediğiniz arkadaşın adı: ")
    
    if yeni_arkadas in kullanicilar and yeni_arkadas != kullanici:
        if yeni_arkadas not in arkadaslar[kullanici]:
            arkadaslar[kullanici].append(yeni_arkadas)
            arkadaslar[yeni_arkadas].append(kullanici)
            print(f"{yeni_arkadas} arkadaş listenize eklendi!")
        else:
            print(f"{yeni_arkadas} zaten arkadaş listenizde.")
    elif yeni_arkadas == kullanici:
        print("Kendinizi ekleyemezsiniz!")
    else:
        print("Bu kullanıcı mevcut değil")

def mesaj_gonder(kullanici):
    alici = input("Mesaj göndermek istediğiniz kişi: ")
    
    if alici in arkadaslar[kullanici]:
        mesaj = input("Mesajınızı yazın: ")
        mesajlar[alici].append((kullanici, mesaj))
        print("Mesaj gönderildi!")
    elif alici == kullanici:
        print("kendinize mesaj gönderemezsiniz!")
    else:
        print(f"{alici} sizin arkadaşınız değil.")

def mesajlari_gor(kullanici):
    print(f"{kullanici} için gelen mesajlar:")
    for gonderen, mesaj in mesajlar[kullanici]:
        print(f"{gonderen}: {mesaj}")

def sosyal_medya():
    while True:
        print("\n1. Kayıt ol\n2. Giriş yap\n3. Çıkış")
        secim = input("Bir seçenek seçiniz: ")
        
        if secim == "1":
            kayit_ol()
        elif secim == "2":
            kullanici = giris_yap()
            if kullanici:
                while True:
                    print("\n1. Arkadaş ekle\n2. Mesaj gönder\n3. Gelen mesajları gör\n4. Çıkış yap")
                    secim2 = input("Bir seçenek seçiniz: ")
                    
                    if secim2 == "1":
                        arkadas_ekle(kullanici)
                    elif secim2 == "2":
                        mesaj_gonder(kullanici)
                    elif secim2 == "3":
                        mesajlari_gor(kullanici)
                    elif secim2 == "4":
                        break
                    else:
                        print("Geçersiz seçenek!")
        elif secim == "3":
            print("Çıkış yapıldı.")
            break
        else:
            print("Geçersiz seçenek!")

sosyal_medya()



