import os
import sys
from datetime import datetime

class Library:
    def __init__(self):
        self.veritabani = open(os.path.join(os.getcwd(), "kitaplar.txt"), "a+")
        self.zaman = datetime.now().date()

    def menu(self):
        secenekler = ["Kitapları Listele", "Kitap Ekle", "Kitap Sil", "Veritabanını Sil (yeniden başlatma gerektirir)", "Çıkış"]
        print("\n".join(f"{i+1}) {secenek}" for i, secenek in enumerate(secenekler)))
        secim = input("Seçiminiz: ")
        getattr(self, ['listele', 'ekle', 'sil', 'veritabani_sil', 'cikis'][int(secim)-1])()

    def listele(self):
        self.veritabani.seek(0)
        for i, kitap in enumerate(self.veritabani):
            bilgi = kitap.strip().split(',')
            print(f"{i+1}) İsim: {bilgi[0]}, Yazar: {bilgi[1]}, Kayıt Zamanı: {bilgi[4]}")

    def ekle(self):
        self.veritabani.seek(0)
        kitap_bilgisi = [input(bilgi + ": ") for bilgi in ["Kitap Adı", "Yazar", "İlk Yayın Yılı", "Sayfa Sayısı"]]
        self.veritabani.write(','.join(kitap_bilgisi + [str(self.zaman)]) + "\n")

    def sil(self):
        kitap_adi = input("Silinecek kitabın adını girin: ")
        self.veritabani.seek(0)
        kitaplar = self.veritabani.readlines()
        for i, kitap in enumerate(kitaplar):
            if kitap.startswith(kitap_adi + ','):
                del kitaplar[i]
                break
        else:
            print(f"{kitap_adi} bulunamadı")
            return
        self.veritabani.seek(0)
        self.veritabani.truncate()
        self.veritabani.writelines(kitaplar)
        print(f"{kitap_adi} silindi")

    def veritabani_sil(self):
        if input("Emin misiniz? (e/h): ").lower() == "e":
            self.veritabani.close()
            os.remove(os.path.join(os.getcwd(), "kitaplar.txt"))
            self.cikis()

    def cikis(self):
        print("Kapatılıyor...")
        self.veritabani.close()
        sys.exit()

lib = Library()

while True:
    lib.menu()
