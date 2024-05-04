from datetime import datetime, timedelta
simdi = datetime.now()
sonteslim_tarihi = simdi + timedelta(days=14)
sonteslim_tarihi_str = sonteslim_tarihi.strftime("%d.%m.%Y")
def kullanıcı_kayit():
    print("->ogrenci kayıt islemleri:\n")

    ogrenci_no=input("kaydı yapılacak ogrencinin ogrenci numarasini giriniz:")
    ogrenci_adi=input("kaydı yapılacak ogrencinin adınını ve soyadını giriniz:")
    sifre=input("Öğrencinin sisteme giriş yapabilmesi için bir şifre belirleyiniz:")

    with open("ogrenci.txt","a+", encoding='utf-8') as dosya:
        dosya.write(ogrenci_no+", "+ogrenci_adi.strip()+", "+sifre+"\n")
    print("öğrenci kayıt işlemi başarılı bir şekilde tamamlandı.")
def kullanıcı_sil():
    ogrenci_sil=input("lütfen kaydını silmek istediginiz ogrencinin numarasını giriniz:")
    yeni_satir = []
    dosya_ismi="ogrenci.txt"

    with open(dosya_ismi, "r", encoding='utf-8') as file:
        for satir in file:
            ogrenciNo_bul=satir.strip().split(',')
            if ogrenci_sil != ogrenciNo_bul[0]:
                yeni_satir.append(satir)
    with open(dosya_ismi, "w", encoding='utf-8') as file:
        file.writelines(yeni_satir)
    print("ogrenci kaydı basarılı bir sekilde silindi.")
def kitap_ekleme():
    print("->kitap ekleme işlemleri:\n")
    isim=input("kaydetmek istediginiz kitabin ismini giriniz:")
    yazar=input("kaydetmek istediginiz kitabin yazarini giriniz:")
    ISBN = input("kitabın ISBN numarasını giriniz:")
    konum= input("kitabın konum bilgisini giriniz:")

    with open("kitaplar.txt","a+", encoding='utf-8') as file:
        file.write(isim+", "+yazar+", "+ISBN+", "+konum+"\n")
    print("kitap başarıyla eklendi!")
def kitap_guncelleme():
    print("->Kitap güncelleme işlemleri:")
    ISBN_gir = input("Lütfen güncelleme yapmak istediğiniz kitabın ISBN numarasını giriniz:")
    yeni_durum = ""
    dosya_adi = "kitaplar.txt"
    temp_liste = []
    with open(dosya_adi, "r+", encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            Kitap_bul = line.strip().split(', ')
            if ISBN_gir == Kitap_bul[2]:
                sec = input("->1-Kitap yazarını değiştirme işlemi\n2-Kitap adını değiştirme işlemi\n3-ISBN numarasını değiştirme işlemi\n4-konum bilgisi değiştirme işlemi:")
                guncellestirilmis = input("Değiştirmek istediğiniz bilginin güncel halini yazınız:")
                if sec == '1':
                    Kitap_bul[1] = guncellestirilmis
                elif sec == '2':
                    Kitap_bul[0] = guncellestirilmis
                elif sec == '3':
                    Kitap_bul[2] = guncellestirilmis
                elif sec == '4':
                    Kitap_bul[3] = guncellestirilmis

                yeni_durum = ', '.join(Kitap_bul) + '\n'
                temp_liste.append(yeni_durum)
            else:
                temp_liste.append(line)
        file.seek(0)
        file.truncate()
        file.writelines(temp_liste)

    print("Kitap başarıyla güncellendi.")
def kitap_odunc_alma(numara):
    kitap = ""
    yazar = ""
    IBSN = ""
    sayac1=0
    sayac2=0
    kitapsayac=0
    with open("odunckitap.txt","r" ,encoding='utf-8') as file:
        for line in file:
            sayac2 += 1
            kontrol = line.split(", ")

            if kontrol[3] != numara:
                sayac1 += 1

        if sayac1 == sayac2:
            with open("ogrenci.txt", "r", encoding='utf-8') as dosya:
                for satir in dosya:
                    ogrenci_bul = satir.split(", ")

                    if ogrenci_bul[0] == numara:
                        ogrenci=ogrenci_bul[1]
                        ogrenci_no=ogrenci_bul[0]

            with open("kitaplar.txt", "r", encoding='utf-8') as dosyaK:
                kitapIBSN = input("lütfen ödünç almak istediğiniz kitabın IBSN numarasını giriniz:")
                for line in dosyaK:
                    kitap_bul=line.split(', ')
                    if kitap_bul[2].strip() == kitapIBSN:
                        kitapsayac=1
                        kitap=kitap_bul[0]
                        yazar=kitap_bul[1]
                        IBSN=kitap_bul[2]
                if kitapsayac:
                    with open("odunckitap.txt", "a", encoding='utf-8') as file:
                        file.write(IBSN+", "+kitap+", "+yazar+", "+ogrenci_no+", "+ogrenci+", "+sonteslim_tarihi_str.strip()+"\n")

                    print("işlem başarılı.İyi okumalar(NOT:kitap,alındıktan sonra 14 gün içinde teslim edilmelidir.)")
                    print("son teslim tarihi:",sonteslim_tarihi_str)
                else:
                    print("Yazdığınız ISBN numarasına ait bir kitap bulunmamaktadır!")
        else:
            print("Aynı seferde sadece 1 kitap alabilirsiniz.Yeni kitap almak için lütfen aldığınız kitabı iade ediniz.")
def odunc_iade(numara):
    temp_list = []
    sontarih = ""

    with open("odunckitap.txt", "r", encoding='utf-8') as dosya:
        dosya_satiri = dosya.readlines()
        for satir in dosya_satiri:
            kitap_bul=satir.strip().split(", ")

            if kitap_bul[3].strip() == numara:
                sontarih = kitap_bul[5]
                print("kitap adı:",kitap_bul[1])
                print("kitap yazarı:",kitap_bul[2])
            else:
                yeni_durum = ', '.join(kitap_bul)
                temp_list.append(yeni_durum)

    with open("odunckitap.txt" ,"w", encoding='utf-8') as file:
        file.write('\n'.join(temp_list))

        getirme_tarihi_obj = datetime.now()
        getirme_tarihi_str=getirme_tarihi_obj.strftime("%d.%m.%Y")
        getirme_tarihi_obj=datetime.strptime(getirme_tarihi_str,"%d.%m.%Y")

        sontarih_obj = datetime.strptime(sontarih,"%d.%m.%Y")
        iade_gunu=(sontarih_obj - getirme_tarihi_obj).days

        if (iade_gunu-1) >= 0:
            print("kitap için kalan gün sayısı:",iade_gunu-1)
            print("kitabu zamanında getirdiğiniz için teşekkür ederiz")
        else:
            print("kitabın son teslim tarihinden bu yana geçen süre:",abs(iade_gunu))
            print("geç kalınan her gün için kütüphanemize 1 TL ödeme yapma durumundasınız!(toplam:",abs(iade_gunu),"TL)")

def kitap_silme():
    ISBN_sil = input("Lütfen silmek istediğiniz kitabın ISBN numarasını giriniz: ")
    yeni_satirlar = []
    dosya_adi = "kitaplar.txt"
    kontrol =1
    with open("odunckitap.txt" ,"r" ,encoding="utf-8") as dosya:
        dosya_satiri = dosya.readlines()
        for satir in dosya_satiri:
            kitap_bul =satir.split(", ")
            if kitap_bul[0] == ISBN_sil:
                kontrol =0
        if kontrol:
            with open(dosya_adi, "r", encoding='utf-8') as dosya:
                for satir in dosya:
                    satir.replace(" " ,"")
                    ISBN_bul = satir.strip().split(', ')
                    if ISBN_sil != ISBN_bul[2]:
                        yeni_satirlar.append(satir)

            with open(dosya_adi, "w", encoding='utf-8') as dosya:
                dosya.writelines(yeni_satirlar)

            print("Kitap başarıyla silindi.")
        else:
            print("Silmek istediğiniz kitap şu anda bir kullanıcı tarafından ödünç alınmış durumda.Silme işlemini tamamlamak için lütfen kitabın teslim edilmesini bekleyiniz")
def kullanıcı_guncelleme(sifre):
    temp_list = []
    if sifre == '55434123':
        with open("ogrenci.txt", "r+", encoding='utf-8') as dosya:
            dosya_satirlari = dosya.readlines()
            ogrenci_bul=input("bilgilerini değştirmek istediğiniz öğrencinin numarasını giriniz:")
            for line in dosya_satirlari:
                ogrenci = line.strip().split(", ")
                if ogrenci[0] == ogrenci_bul:
                    sec = input("\n->1-Numara değiştirme\n2-isim değiştirme\n3-Şifre değiştirme:")
                    if sec == '1':
                        yeni_numara=input("yeni numarayı giriniz:")
                        ogrenci[0] = yeni_numara
                    elif sec == '2':
                        yeni_isim=input("yeni ismi giriniz:")
                        ogrenci[1]= yeni_isim
                    elif sec == '3':
                        yeni_sifre = input("Yeni şifreyi giriniz: ")
                        ogrenci[2]= yeni_sifre

                yeni_durum = ', '.join(ogrenci) + "\n"
                temp_list.extend(yeni_durum)
            dosya.seek(0)
            dosya.truncate()
            dosya.writelines(temp_list)
            temp_list = []
        print("güncelleme işlemi başarılı bir şekilde tamamlanmıştır!")
    else:
        with open("ogrenci.txt", "r+", encoding='utf-8') as dosya:
            dosya_satirlari = dosya.readlines()
            for satir in dosya_satirlari:
                kullanıcı_bul=satir.strip().split(", ")
                if kullanıcı_bul[0] == sifre:
                    sec=input("\n->>1-Numara değiştirme\n2-isim değiştirme\n3-Şifre değiştirme:")
                    if sec == '1':
                        yeni_numara = input("yeni numarayı giriniz:")
                        kullanıcı_bul[0] = yeni_numara
                    elif sec == '2':
                        yeni_isim = input("yeni ismi giriniz:")
                        kullanıcı_bul[1] = yeni_isim
                    elif sec == '3':
                        yeni_sifre = input("Yeni şifreyi giriniz: ")
                        kullanıcı_bul[2] =yeni_sifre
                yeni_durum = ', '.join(kullanıcı_bul) + '\n'
                temp_list.append(yeni_durum)
            dosya.seek(0)
            dosya.truncate()
            dosya.writelines(temp_list)

            temp_list = []
        print("güncelleme işlemi başarılı bir şekilde tamamlanmıştır!")
def kitap_goruntule():
   kitap_ara=input("Görüntülemek istediğiniz kitabın IBSN numrasını giriniz:")
   with open("kitaplar.txt","r",encoding='utf-8') as dosya:
       dosya_satirlari=dosya.readlines()
       for satir in dosya_satirlari:
           kitap_bul=satir.split(", ")
           if kitap_bul[2].strip() == kitap_ara:
               print("kitap adı:",kitap_bul[0])
               print("yazar adı:",kitap_bul[1])
               print("ISBN numarası:",kitap_bul[2])
               print("kitabın konumu:",kitap_bul[3])
def main():
    yonetici_sifre='3477621'
    print("->Bakırçay Üniversitesi kütüphane sistemi")
    print("Turcademy Veri tabanı 19.04.2024 tarihinden itibaren ünivetsitemiz erişimine açıldı!!")
    kontrol1 = input("->1-yönetici giriş ekranı\n2-öğrenci giriş ekranı:")
    if kontrol1 =='1':
        sifre=input("->yönetici sistemine giriş yapabilmek için lütfen yönetici şifresini giriniz:")
        if sifre == yonetici_sifre:
            while True:
                secim=input("->1-kitap ekleme\n2-kitap silme\n3-kitap guncelleme\n4-kitap görüntüleme\n5-kullanıcı kayıt islemleri\n6-kullanıcı silme islemleri\n7-kullanıcı bilgilerini güncelleme\n8-işlemi sonlandır:")
                if secim == '1':
                   kitap_ekleme()
                elif secim == '2':
                   kitap_silme()
                elif secim == '3':
                   kitap_guncelleme()
                elif secim == '4':
                   kitap_goruntule()
                elif secim == '5':
                    kullanıcı_kayit()
                elif secim == '6':
                   kullanıcı_sil()
                elif secim == '7':
                    kullanıcı_guncelleme(sifre)
                elif secim == '8':
                    break
                bitir = input("devam etmek icin herhangi bir tusa ,islemi bitirmek icin '0'a basınız:")
                if bitir == '0':
                  break
        if sifre != yonetici_sifre:
                print("yanlış şifre girdiniz,sisteme giriş engellendi!")
    if kontrol1 =='2':
        sayac1 = 0
        sayac2 = 0

        sifre2=input("->ogrenci sistemine giris yapabilmek icin ogrenci numarasını giriniz:")
        with open("ogrenci.txt" ,"r", encoding='utf-8') as dosya:
            for satir in dosya:
                sayac1 +=1
                ogrenci_no=satir.strip().split(", ")
                if sifre2 == ogrenci_no[0]:
                    kayıtlı=ogrenci_no[0]
                    sifre3 = input("->girilen öğrenci numarasına ait şifreyi giriniz:")
                    if sifre3 == ogrenci_no[2]:
                        while True:
                            secim2 = input("->1-kitap ekleme\n2-kitap silme\n3-kitap guncelleme\n4-kitap görüntüleme\n5-kitap odunc alma\n6-odunc iade etme\n7-bilgilerini güncelleme\n8-İşlemi sonlandır:")
                            if secim2 == '1':
                              kitap_ekleme()
                            elif secim2 == '2':
                              kitap_silme()
                            elif secim2 == '3':
                              kitap_guncelleme()
                            elif secim2 =='4':
                                kitap_goruntule()
                            elif secim2 == '5':
                              kitap_odunc_alma(kayıtlı)
                            elif secim2 == '6':
                                odunc_iade(kayıtlı)
                            elif secim2 == '7':
                                kullanıcı_guncelleme(kayıtlı)
                            elif secim2 == '8':
                                break

                            bitir = input("devam etmek icin herhangi bir tusa ,islemi bitirmek icin '0'a basınız:")
                            if bitir == '0':
                                break
                    else:
                        print("girdiğiniz şifre hatalıdır,lütfen tekrar deneyiniz:!")
                        break
                else:
                    sayac2 +=1
        if sayac1 == sayac2:
            print("""Aradğınız numaraya ait bir kayıt bulunmaktadır,dilerseniz bir yönetici yardımıyla kayıt yaptırabilirsiniz.""")




if __name__ =="__main__":
    main()