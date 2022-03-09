import time

import pyautogui
import pyperclip

# Passo 1: Entrar no sistema da empresa (Google Drive)

pyautogui.PAUSE = 1

pyautogui.hotkey('win', 'r')
pyautogui.write('chrome.exe')
pyautogui.press('enter')
pyperclip.copy('https://drive.google.com/drive/u/0/folders/1cmlvEW1YtcKRAOrw5'
                'Pc9QqZnZeskYauh')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

time.sleep(3)
# Passo 2: Navegar pelo sistema até a base de dados

pyautogui.click(x=875, y=419)
pyautogui.click(x=1712, y=193)
pyautogui.click(x=1509, y=562)
# Passo 3: Exportar a base de dados
# Passo 4: Calcular os indicadores (Faturamento e quantidade de produtos
# Vendidos)
# Passo 5: Enviar um e-mail para a diretoria com os indicadores
