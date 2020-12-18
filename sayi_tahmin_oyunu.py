#ASSIGNMENT - SAYI TAHMIN OYUNU

def sayi_tahmin_oyunu(*sayilar):
    for sayi in sayilar:
        print(sayi)
        i = 1
        c=1
        while i < sayi:                                 # deneme sayisini sinirlandirdim.
            tahmin = int(input('0 ile 100 arasindaki sayiyi tahmin edin: ')) # kullanicidan sayi tahmini aldim.
            if tahmin > 100:                            # tahmin belirtilen aralikta degilse, dongunun basina doner.
                print('belirtilen aralikta bir sayi girin lutfen...')
                c+=1
            elif tahmin < sayi:                         # tahmin sayidan kucuk ise 'YUKARI' yazdirir.
                print('YUKARI')
                i+=1
                c += 1
            elif tahmin > sayi:                         # tahmin sayidan buyuk ise 'ASAGI' yazdirir.
                print('ASAGI')
                i+=1
                c += 1
            else:                                       # sayi dogru tahmin edildi ise else calisir.
                print(f'tebrikler {c} tahminde BILDINIZ!')
                break                                   # cevap dogru ise donguden cikar.
sayi_tahmin_oyunu(43,54,33,22,67)