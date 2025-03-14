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

kelime_uzunlugu = kelime_uzunlugu_al()

with open("data.json", 'r', encoding='utf-8') as dosya:
    kelimeler = json.load(dosya)[str(kelime_uzunlugu)+"_letters"]
    # Oyunun geri kalanı buraya yazılacak
