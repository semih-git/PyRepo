tutar = float(input("urunlerin toplam tutari: "))
para = float(input("musterinin verdigi para miktari: "))
para_listesi = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
fark = para - tutar
if fark < 0:
    print("yetersiz miktar!")
else:
    print('para ustu= ', fark)
    for i in para_listesi:
        toplam_para_adedi = int(float(format(fark, '.2f')) // i)
        fark = fark % i  # i degerine bolumunden kalan para miktarini verir.
        if toplam_para_adedi == 0:
            continue
        print(f'{toplam_para_adedi} adet, {i} euro')
        if fark == 0:
            break
