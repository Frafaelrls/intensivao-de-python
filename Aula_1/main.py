import time
import glob
import os

import pyautogui
import pyperclip
import pandas as pd

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

time.sleep(5)
lista_os_arquivos = glob.glob(r'E:\Arquivos\Downloads\*.xlsx')
ultimo_arquivo = max(lista_os_arquivos, key=os.path.getctime)
nome = ultimo_arquivo[-17:]
tabela = pd.read_excel(rf"E:/Arquivos/Downloads/{nome}",
                       sheet_name='Plan1')

# Passo 3.5: Apagar a base de dados
time.sleep(1)
caminho = f'E:/Arquivos/Downloads/{nome}'
os.remove(caminho)
print(tabela)

# Passo 4: Calcular os indicadores (Faturamento e quantidade de produtos
# Vendidos)

faturamento = tabela['Valor Final'].sum()
quantidade = tabela['Quantidade'].sum()

print(faturamento)
print(quantidade)

# Passo 5: Enviar um e-mail para a diretoria com os indicadores

pyautogui.hotkey('ctrl', 't')  # nova aba
pyperclip.copy('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(5)

# Clicar no botão escrever
pyautogui.click(x=79, y=207)

# Escrever o destinatário
destinatario = open('usuario/email.txt', encoding='utf-8')
destinatario = destinatario.read()
pyperclip.copy(destinatario)
pyautogui.hotkey('ctrl', 'v')

# Escrever assunto
pyautogui.press('tab')
assunto = 'Planilha com indicadores'
pyperclip.copy(assunto)
pyautogui.hotkey('ctrl', 'v')

# Escrever o corpo do email
pyautogui.press('tab')

corpo = f'''
Olá, 

Segue relatório com os indicadores mensais.

Faturamento: R$ {faturamento:,.2f}
Quantidade: {quantidade:,}

Atenciosamente
'''

pyperclip.copy(corpo)
pyautogui.hotkey('ctrl', 'v')

# Enviar o Email
pyautogui.hotkey('ctrl', 'enter')
