import time

import pyautogui

# função para buscar coordenadas na tela
time.sleep(5)
local = pyautogui.position()
print(local)
