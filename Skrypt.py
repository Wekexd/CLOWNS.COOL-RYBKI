import time
from pynput.keyboard import Key, Controller

import win32gui
from PIL import ImageGrab
import pytesseract

import configparser
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("CLOWNS.COOL | W3KE | HITS: 0 | MONEY: 0")

Config = configparser.ConfigParser()
Config.read("settings.ini")

pytesseract.pytesseract.tesseract_cmd = Config.get('Ustawienia', 'Sciezka_tesseractocr')

klikin = False
ile_klikniec = 0
fished = 0
jd = 0

keyboard = Controller()

while True:
    window = win32gui.GetForegroundWindow()
    if (window):
        title = win32gui.GetWindowText(window)
        if ("FiveM" in title):
            x0, y0, x1, y1 = win32gui.GetWindowRect(window)
            w = (x0 + x1) / 2
            h = (y1 + y0) / 2
            image = ImageGrab.grab(bbox=((w) - 150, h + 290 + 95, (w) + 150, h + 350 + 65))
            # image.show()
            tesstr = pytesseract.image_to_string(image, lang='eng')
            ile_klikniec = 0
            # for line in tesstr:
            line = tesstr
            if "-" in line:
                parts = line.split("-")
                if len(parts) > 1:
                    after_hyphen = parts[1].strip()
                    if after_hyphen:
                        first_character = after_hyphen[0]
                        print("[-] Char: " + str(first_character))
                        if first_character.isdigit():
                            ile_klikniec = int(first_character)
                        else:
                            if first_character == 'T' or first_character == 'i' or first_character == 'I':
                                ile_klikniec = 1
                            elif first_character == 's' or first_character == 'S':
                                ile_klikniec = 5
            else:
                jd = jd + 1
                if jd == Config.get('Ustawienia', 'Reset'):
                    keyboard.press('e')
                    time.sleep(0.05)
                    keyboard.release('e')
                    jd = 0
                    print("[-] Reset Fishing")
            # print(numbers)
            if ile_klikniec != 0:
                if klikin == False:
                    print("[+] Clicking SPACE (" + str(ile_klikniec) + ")")
                    klikin = True
                    while klikin:
                        keyboard.press(Key.space)
                        time.sleep(0.1)
                        keyboard.release(Key.space)
                        time.sleep(0.4)
                        ile_klikniec = ile_klikniec - 1
                        if (ile_klikniec <= 0):
                            klikin = False
                            fished = fished + 1
                            print("[=] Finished working, fished " + str(fished))
                            ctypes.windll.kernel32.SetConsoleTitleW("CLOWNS.COOL | W3KE | HITS: "+str(fished)+" | MONEY: ~" + str(fished*5000) + "-" + str(fished*8000))
                            time.sleep(4.5)
                            keyboard.press('e')
                            time.sleep(0.05)
                            keyboard.release('e')
                            jd = 0
