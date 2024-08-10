import pyautogui
import pyperclip
import webbrowser
import time
import yfinance

ticker = input("Digite o codigo da ação desejada: ")

dados = yfinance.Ticker(ticker).history(start="2020-01-01", end="2020-12-31")
fechamento = dados.Close

maxima = round(fechamento.max(), 2)
minimo = round(fechamento.min(), 2)
valor_medio = round(fechamento.mean(), 2)

destinatario = "fabriscorretordeimoveis@gmail.com"
assunto = "Análise do Projeto02"

# usando """ para abrir """ para fechar ele ira fazer a quebra de pagina no texto.
# usando f na frente das aspas para concatenar e colocar chaves as variaveis {}.
 
mensagem = f"""
Prezado gestor,

Seguem as análises solicitadas da ação {ticker}:

Cotação máxima: R$ {maxima}
Cotação mínima: R$ {minimo}
Valor médio: R$ {valor_medio}

Qualquer dúvida, estou a disposição!

Atte.
"""  

# abrir o navegador e ir para o gmail

webbrowser.open("www.gmail.com")
time.sleep(3) 

# configurando uma pausa de 3 segundos
pyautogui.PAUSE = 3

# clicar no botão escrever
pyautogui.click(x=112, y=269)    

# digitar o e-mail do destinatario e teclar TAB
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# digitar o assunto no e-mail
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# digitar a mensagem
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")

# clicar no botão enviar
pyautogui.click(x=1068, y=947)

pyautogui.click("ctrl", "f4")

print("E-mail enviado com sucesso!")