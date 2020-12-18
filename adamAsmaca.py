kelime = input("Kelime giriniz:")
kelime = kelime.upper()
baslik=" KELIME OYUNUNA HOSGELDINIZ!! "
print(baslik.center(120,"%"))
while True:
    harfsayisi = len(kelime)
    print(f"\n\n\nKelimeniz {harfsayisi} harflidir.")
    tahminler = []

    deneme = 4
    sekil1 = """
                                                    _________
                                                    |        O
                                                    |
                                                    |"""
    sekil2 = """
                                                    _________
                                                    |        O
                                                    |       / /
                                                    |"""
    sekil3 = """
                                                    _________
                                                    |        O
                                                    |      /| /|
                                                    |"""
    sekil4 = """
                                                    _________
                                                    |        O 
                                                    |      /| /|
                                                    |       /  \ """

    while deneme>0:
        tabela=""
        for harf in kelime:
            if harf in tahminler:
                tabela+=harf
            else:
                tabela=tabela+" _ "
        if tabela==kelime:
            print("TEBRIKLER! KELIMEYI DOGRU BILDINIZ!")
            break
        print("Kelimeyi tahmin edin: ",tabela)
        print(deneme,"canin kaldi")
        tahmin=input("Bir harf giriniz:")
        tahmin=tahmin.upper()
        if tahmin==kelime:
            print("\nBRAVO BILDINIZ!")
            break
        if tahmin in tahminler:
            print(f"\n{tahmin} DAHA ONCE SOYLENDI")
        elif tahmin in kelime:
            print("\nDOGRU")
            tahminler.append(tahmin)
        else:
            print("\nYANLIS. KELIMEDE BU HARF YOK")
            deneme=deneme-1
        if deneme==3:
            print(sekil1)
        if deneme==2:
            print(sekil2)
        if deneme==1:
            print(sekil3)
    if deneme==0:
        print(sekil4)
        print("HAKKINIZ KALMADI. BILEMEDINIZ")
        print(f">>> kelimeniz: {kelime}")
        print("Oyuna DEVAM etmek istiyor musunuz? (E/H)")
        devam = input(">>>")
        devam = devam.upper()
        if devam == "H":
            break
        else:
            continue
