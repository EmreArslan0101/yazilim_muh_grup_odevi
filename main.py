import json
import random

def kelime_uzunlugu_al():
    while True:
        uzunluk = input("Kelime uzunluğunu seçin (3, 4, 5, 6): ")
        if uzunluk in {"3", "4", "5", "6"}:
            return int(uzunluk)
        print("Geçersiz giriş! Lütfen 3, 4, 5 veya 6 girin.")

def rastgele_sec(dizi):
    if not dizi:  # Eğer dizi boşsa hata döndür
        raise ValueError("Dizi boş olamaz!")
    return random.choice(dizi)

def oyun_sonu(kazandi, kelime):
    if kazandi:
        print(f"Tebrikler! Kelimeyi doğru tahmin ettiniz: {kelime}")
    else:
        print(f"Oyunu kaybettiniz! Doğru kelime: {kelime}")
    exit()

def kelime_tahmin_oyunu():
    uzunluk = kelime_uzunlugu_al()
    kelime = input(f"Lütfen {uzunluk} harfli bir kelime girin: ").strip().lower()

    if len(kelime) != uzunluk:
        print(f"Hata! Kelime tam olarak {uzunluk} harfli olmalı.")
        return

    gizli_kelime = ["_"] * uzunluk
    tahmin_hakki = uzunluk
    acilan_harf_sayisi = 0

    while tahmin_hakki > 0:
        print(" ".join(gizli_kelime))
        tahmin = input("Tahmininizi girin: ").strip().lower()

        if tahmin == kelime:
            oyun_sonu(True, kelime)
        
        tahmin_hakki -= 1

        if acilan_harf_sayisi < uzunluk:
            gizli_kelime[acilan_harf_sayisi] = kelime[acilan_harf_sayisi]
            acilan_harf_sayisi += 1

    oyun_sonu(False, kelime)

kelime_uzunlugu = kelime_uzunlugu_al()

with open("data.json", 'r', encoding='utf-8') as dosya:
    kelimeler = json.load(dosya)[str(kelime_uzunlugu)+"_letters"]
    kelime = rastgele_sec(kelimeler)
    
    # Oyunun geri kalanı buraya yazılacak
