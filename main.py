import json
import os
from datetime import datetime

print("=" * 35)
print("💰 Finance Tracker")
print("=" * 35)
print("Proje başarıyla oluşturuldu!")

gelirler = []
giderler = []
DOSYA_ADI = "veriler.json"

def verileri_kaydet():


    veriler = {
        "gelirler": gelirler,
        "giderler": giderler
    }

    with open(DOSYA_ADI, "w", encoding="utf-8") as dosya:
        json.dump(veriler, dosya, indent=4)

def verileri_yukle():
     global gelirler, giderler

     if os.path.exists(DOSYA_ADI):
         with open(DOSYA_ADI, "r", encoding="utf-8") as dosya:
             veriler = json.load(dosya)

         gelirler = veriler["gelirler"]
         giderler = veriler["giderler"]
def menu():
    print("\n===== Finance Tracker =====")
    print("1. Gelir Ekle")
    print("2. Gider Ekle")
    print("3. İşlemleri Görüntüle")
    print("4. Bakiyeyi Göster")
    print("5. İşlem sil")
    print("6. Çıkış")


def gelir_ekle():
    miktar = float(input("Gelir miktarını girin: "))

    if miktar <= 0:
        print("❌ Geçersiz tutar. Lütfen 0'dan büyük bir sayı girin.")
        return

    kategori = input("Kategori girin: ")
    aciklama = input("Açıklama girin: ")
    tarih = datetime.now().strftime("%d.%m.%Y")

    gelir = {
        "miktar": miktar,
        "kategori": kategori,
        "aciklama": aciklama,
        "tarih": tarih
    }

    gelirler.append(gelir)
    verileri_kaydet()
    print(f"{miktar} TL gelir eklendi.")


def gider_ekle():
    miktar = float(input("Gider miktarını girin: "))

    if miktar <= 0:
        print("❌ Geçersiz tutar. Lütfen 0'dan büyük bir sayı girin.")
        return

    kategori = input("Kategori girin: ")
    aciklama = input("Açıklama girin: ")
    tarih = datetime.now().strftime("%d.%m.%Y")

    gider = {
        "miktar": miktar,
        "kategori": kategori,
        "aciklama": aciklama,
        "tarih": tarih
    }

    giderler.append(gider)
    verileri_kaydet()
    print(f"{miktar} TL gider eklendi.")


def islemleri_goster():
    print("\n📋 Gelirler")

    if len(gelirler) == 0:
        print("Henüz gelir eklenmedi.")
    else:
        for i, gelir in enumerate(gelirler, start=1):
            print(f"{i}. {gelir['kategori']} | {gelir['miktar']} TL | {gelir['aciklama']} | {gelir['tarih']}")

    print("\n📋 Giderler")

    if len(giderler) == 0:
        print("Henüz gider eklenmedi.")
    else:
        for i, gider in enumerate(giderler, start=1):
            print(f"{i}. {gider['kategori']} | {gider['miktar']} TL | {gider['aciklama']} | {gider['tarih']}")

    print("-" * 50)
    print(f"Toplam Gelir : {sum(gelir['miktar'] for gelir in gelirler)} TL")
    print(f"Toplam Gider : {sum(gider['miktar'] for gider in giderler)} TL")


def bakiyeyi_goster():
    toplam_gelir = sum(gelir["miktar"] for gelir in gelirler)
    toplam_gider = sum(gider["miktar"] for gider in giderler)
    bakiye = toplam_gelir - toplam_gider

    print("\n💰 Bakiye Bilgisi")
    print(f"Toplam Gelir : {toplam_gelir} TL")
    print(f"Toplam Gider : {toplam_gider} TL")
    print("-" * 30)
    print(f"Kalan Bakiye : {bakiye} TL")

def islem_sil():
    print("1. Gelir Sil")
    print("2. Gider Sil")

    secim = input("Seçiminiz: ")

    if secim == "1":
        print("\nGelirler:")

        for i, gelir in enumerate(gelirler, start=1):
            print(f"{i}. {gelir['kategori']} | {gelir['miktar']} TL")

        sil = int(input("Silmek istediğiniz gelir numarası: "))

        if 1 <= sil <= len(gelirler):
            silinen = gelirler.pop(sil - 1)
            verileri_kaydet()
            print(f"{silinen['miktar']} TL gelir silindi.")
        else:
            print("Geçersiz numara.")

    elif secim == "2":
        print("\nGiderler:")

        for i, gider in enumerate(giderler, start=1):
            print(f"{i}. {gider['kategori']} | {gider['miktar']} TL")

        sil = int(input("Silmek istediğiniz gider numarası: "))

        if 1 <= sil <= len(giderler):
            silinen = giderler.pop(sil - 1)
            verileri_kaydet()
            print(f"{silinen['miktar']} TL gider silindi.")
        else:
            print("Geçersiz numara.")

    else:
        print("Geçersiz seçim.")

verileri_yukle()
while True:
    menu()
    secim = input("Seçiminizi girin: ")

    if secim == "1":
        gelir_ekle()

    elif secim == "2":
        gider_ekle()

    elif secim == "3":
        islemleri_goster()

    elif secim == "4":
        bakiyeyi_goster()

    elif secim == "5":
        islem_sil()

    elif secim == "6":
        print("Program kapatılıyor...")
        break

    else:
        print("Geçersiz seçim!")