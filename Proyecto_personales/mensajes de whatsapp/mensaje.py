# python mensaje.py

import pyautogui, webbrowser
from time import sleep

numero = 977619531
numero = str(numero) # Convertir el número a cadena de texto


webbrowser.open('https://web.whatsapp.com/send?phone='+numero)

sleep(10)

for i in range(10):
    pyautogui.typewrite('prueba de mensaje')
    pyautogui.press('enter')
