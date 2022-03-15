import time

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
tabela = pd.read_excel(r"E:/Arquivos/Downloads/Vendas - Dez.xlsx")
print(tabela)

faturamento = tabela['Valor Final'].sum()
quantidade = tabela['Quantidade'].sum()


# Passo 4: Calcular os indicadores (Faturamento e quantidade de produtos
# Vendidos)

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
pyautogui.click(x=1317, y=466)
assunto = 'Planilha com indicadores'
pyperclip.copy(assunto)
pyautogui.hotkey('ctrl', 'v')

# Escrever o corpo do email
pyautogui.click(x=1363, y=525)
corpo = f'Olá, segue relatório com os indicadores mensais.\n\nFaturamento: ' \
        f'R$ {faturamento}\nQuantidade: {quantidade}\nAtenciosamente.'
pyperclip.copy(corpo)
pyautogui.hotkey('ctrl', 'v')



# Enviar o Email
