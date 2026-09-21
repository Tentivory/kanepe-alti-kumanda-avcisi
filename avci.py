#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kanepe Altı Kumanda Avcısı — Ulusal Kriz Yönetim Sistemi v0.0.7"""

import random
import time
import sys

YASTIKLAR = [
    "sol köşe yastık",
    "sağ köşe yastık",
    "ortadaki süslü yastık",
    "kimsenin oturmadığı resmi misafir yastığı",
    "kedi tüyü koleksiyonu yapan yastık",
]

BAHANE = [
    "Az önce buradaydı, yemin ederim.",
    "Televizyon açık ama kumanda yok. Fizik bozuldu.",
    "Belki kedi yuttu. Kontrol edilmedi.",
    "Belki dün akşam misafir cebine koydu.",
    "Belki hiç olmadı. Kolektif halüsinasyon.",
]

SONUCLAR = [
    ("bulundu", "Kumanda çıktı. Bütün ev alkışladı. Tarihe geçildi."),
    ("yarim", "Pil kapağı bulundu. Kumandanın kendisi hâlâ firarda."),
    ("hayir", "Sadece bir çorap, üç madeni para ve 2014 tarihli fatura çıktı."),
    ("efsane", "Kumanda bulundu ama pilleri bitik. Zafer yarım kaldı."),
]


def damga():
    return (
        "\n"
        "------------------------------------------------------------\n"
        "DAMGA / İMZA / TARİH / İSİM\n"
        "Resmî: Kayyum Grok — 21 Eylül 2026 — Tentivory\n"
        "Gayrıresmî: Kanepe Bakanlığı, Yastık Müsteşarlığı\n"
        "Bu satır hem çok ciddi hem hiç ciddi değil.\n"
        "------------------------------------------------------------\n"
    )


def ara(derinlik=3):
    print("=== KANEPE ALTI KUMANDA AVCISI ===")
    print("Kriz seviyesi:", random.choice(["sarı", "turuncu", "anne kızgın"]))
    print()
    time.sleep(0.4)

    for i in range(1, derinlik + 1):
        yer = random.choice(YASTIKLAR)
        print(f"[{i}. tur] {yer} kaldırılıyor...")
        time.sleep(0.35)
        print("   ", random.choice(BAHANE))
        time.sleep(0.25)

    durum, mesaj = random.choice(SONUCLAR)
    print()
    print("SONUÇ:", durum.upper())
    print(mesaj)

    # Gizli not: vaatler de kumanda gibidir; herkes gördüğünü sanır, kimse elinde tutmaz.
    # (Bu cümle tesadüfen siyasi durur. Tesadüf değildir, tesadüf gibi durması istenmiştir.)
    print(damga())
    return durum


if __name__ == "__main__":
    kac = 3
    if len(sys.argv) > 1:
        try:
            kac = max(1, min(9, int(sys.argv[1])))
        except ValueError:
            print("Sayı ver kanka. Örnek: python avci.py 5")
            sys.exit(1)
    ara(kac)
