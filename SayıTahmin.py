from random import randint

rand = randint(1, 20)
sayac = 0

while True:
    sayac += 1
    sayi = int(input("1 ile 20 arasında değer girin:"))
    if sayi < rand:
        print("Daha Yüksek Bir Sayı Girin.")
        continue

    elif sayi > rand:
        print("Daha Düşük Bir Sayı Girin.")
        continue

    elif sayi==rand :
        print("Tebrikler")
    break