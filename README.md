# CLOWNS COOL AUTO ŁOWIENIE RYBEK (SKRYPT NA RYBAKA)

1. Używasz na własną odpowiedzialność
2. Jebać zjebów z fivema a gitów szanować

## JAK TO USTAWIĆ

0. zainstaluj pythona
1. Nie chciało mi się robić requirements więc komendy masz tu

 - pip install pywin32
 - pip install pillow
 - pip install pytesseract
 - pip install pynput

jak coś tam jeszcze jest to sobie doinstaluj
   
3. Zmieniasz sciezka_tesseractocr na swoją, tutaj link do pobrania https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.1.20230401.exe - kopiujesz ścieżke tego shitu i / zamieniasz na \
UWAGA NA KONCU TEJ ACIEZKI MUSI BYC TESSERACT.EXE
4. te reset to później jak ci za szybko będzie wędke puszczało to wdupcasz na idk 2x więcej albo ile tam chcesz byle więcej
5. jezeli ci nie wykrwa to sie pobaw kordami w bbox (linia 33)

## JAK TO ODPALIĆ
1. Wchodzisz do fivema
2. Zmieniasz z fullscreena na okno
3. Zmieniasz rozdzielczość na 1600x900 i aspect ratio na auto
4. Odpalasz i masz

jak nie umiesz odpalać skryptów pythona z cmd to tu masz mini poradnik

klikasz w te czerwone zaznaczone na ss
![zdj1](https://imgur.com/EVI1GW1.png)

usuwasz tam wszystko i wpisujesz cmd i klikasz enter

![zdj2](https://imgur.com/AqNosiY.png)

w cmd wpisujesz py Skrypt.py i tak samo enter

![zdj3](https://imgur.com/W3QBc2Q.png)

jak masz m.w. tak jak na obrazku (nie wyskoczyło ci nic tylko zmieniła się nazwa okna, to oznacza że jest git i możesz zacząć łowić)

![zdj3](https://imgur.com/VlxRXPd.png)

idziesz na łowisko, klikasz e i czekasz na rybcie, ryba się łowi i jest ez ez

## UWAGA JAK MASZ TAK PRZESUNIETE TE UI
![zdj4](https://i.imgur.com/HP1Tez1.png)

TO W 33 LINIJCE ZMIEN NA TO
```image = ImageGrab.grab(bbox=((w) - 150, h + 290 + 45, (w) + 150, h + 350 + 45))```

## W3KE ON TOP
