tercih=[]                                                           # tercihleri tutmak icin bos bir liste olusturdum.
corbalar = ["mercimek corbasi(1)","mantar corbasi(2)","domates corbasi(3)"]    # mevcut menuleri ayri listelere yazdim.
yemekler = ["kebap(1)","kurufasulye(2)","doner(3)"]
icecekler = ["ayran(1)","salgam(2)","cola(3)"]
baslik=" SANAL RESTORAN "
print(baslik.center(120,"%"))
menu = ['%%%%%%%%%% M E N U %%%%%%%%%%',
"    Corbalar ....... (1)",
"    Yemekler ....... (2) ",
"    Icecekler ...... (3)",
"       Yazdir ......... (4)",
"       Odeme .......... (5)",
'       Cikis .......... (6)']
for i in menu:
    print ('\t'.expandtabs(44), i)
while True:
    secim = input("%%%%%%%%%%%%%%% MENU SECIMINIZ ? :( ) ")         # ana menu secimi icin kullanicidan veri aldim.
    if secim not in "1,2,3,4,5,6":                                  # veri girisini sinirlandirdim.
        print("Lutfen sizden istenen aralikta bir sayi (1,2,3,4,5 veya 6) giriniz!")
    if secim == "1":                                    # ana menude yapilacak corbalar secimi icin kosul olusturdum.
        print(corbalar)
        corba = input("CORBA SECIMINIZ ? :( ) ")
        if corba not in "1,2,3":                            # veri girisini sinirlandirdim.
            print("Lutfen sizden istenen aralikta bir sayi (1,2 veya 3) giriniz!")
        else:
            corba=int(corba)                                #input ile alinan veriyi int donusturdum.
            tercih.append(corbalar[corba-1])                # secimi tercih listesine ekledim.
    if secim == "2":
        print(yemekler)
        yemek = input("YEMEK SECIMINIZ ? :( ) ")
        if yemek not in "1,2,3":                            # veri girisini sinirlandirdim.
            print("Lutfen sizden istenen aralikta bir sayi (1,2 veya 3) giriniz!")
        else:
            yemek=int(yemek)                                # input ile alinan veriyi int donusturdum.
            tercih.append(yemekler[yemek-1])                # secimi tercih listesine ekledim.
    if secim == "3":
        print(icecekler)
        icecek = input("ICECEK SECIMINIZ ? :( ) ")
        if icecek not in "1,2,3":                           # veri girisini sinirlandirdim.
            print("Lutfen sizden istenen aralikta bir sayi (1,2 veya 3) giriniz!")
        else:
            icecek=int(icecek)                              #input ile alinan veriyi int donusturdum.
            tercih.append(icecekler[icecek-1])              # secimi tercih listesine ekledim.
    if secim == "4":
        if len(tercih)==0:                                  # tercih listesi bos ise uyari mesaji ekledim.
            print("Yazdirilacak bir menu bulunamadi..")
        else:
            for i in range(len(tercih)):                # tercih listesinin uzunlugu kadar for dongusunu calistirdim.
                print("-",tercih[i])                    # tercih listesini tek tek yazdirdim.
    if secim == "5":
        tutar = float(len(tercih) * 5)                  # tercih listesinde biriken menulerin toplam tutarini hesapladim.
        print("Toplam fiyat: ", tutar, "euro.")
        para = float(input("Musterinin odedigi para: "))    # kullanicidan verdigi para miktarini aldim.

        para_listesi = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01] # tedavuldeki p. listesi.
        fark = para - tutar                             # paraustunu hesapladim ve sonrasinda bastirdim.
        print('para ustu= ', fark)
        if fark<0:     # kullanici yetersiz miktar girerse tercihler listesinin icini bosalttim ve uyari mesaji ekledim.
            print("Yetersiz miktar! Secilen menuler siliniyor...")
            tercih=[]
        else:
            for i in para_listesi:                      # para listesinin ogelerini uzerinde for dongusu kurdum.
                toplam_para_adedi = int(float(format(fark, '.2f')) // i)   # farki para_list.deki herbir miktara boldum.
                fark = fark % i                         # i degerine bolumunden kalan para miktarini verir.
                if toplam_para_adedi == 0:              # bolum sifir ise donguye devam ettim.(continue)
                    continue
                print(f'{toplam_para_adedi} adet, {i} euro')
                if fark == 0:   # fark sifir olunca for dongusunden break ile ciktim. ve tercih list.in icini bosalttim.
                    print("Afiyet olsun.")
                    tercih=[]
                    break
    if secim == "6":                                    # while dongusunden break ile ciktim.
        print("Hoscakalin, yine bekleriz.")
        break



