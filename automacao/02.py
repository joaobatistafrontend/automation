import pygetwindow as gw
import pyautogui
import pywhatkit as kit


# blibliotecas utilizadas

import pygetwindow as gw
import pyautogui
import pywhatkit as kit
import time
import schedule
import keyboard



def envio():
     #mensagem q vai junto a img
     msg = 'grafico  atualizado'
     
     #contato para que vai a msg
     contatos = '+5585992801602'
     
     #grupo para que vai a msg
     grupo = 'EhkJ7tJX4Iz4xTS7l3DI3w'
     
     # acesso aos sistema do windos (acessando o Power Bi)
     power_bi_window = gw.getWindowsWithTitle("Power BI")[0]
     
     # ativando a janela do Power BI, ou seja, traz a janela para a frente.
     power_bi_window.activate()
     
     #capturar uma captura de tela da janela do Power BI.
     screenshot = pyautogui.screenshot(region=(power_bi_window.left, power_bi_window.top, power_bi_window.width, power_bi_window.height))
     
     #Salva a captura de tela como um arquivo de imagem chamado 'screenshot.jpg'.
     screenshot.save('screenshot.jpg')
     
     #enviar a imagem ('screenshot.jpg') para o grupo especificado (grupo) no WhatsApp, junto com a mensagem de texto (msg).
     kit.sendwhats_image(grupo, 'screenshot.jpg',msg)
     print('Mensagem enviada com sucesso!')
     
     #esperar 15 segundos ele feixa a aba pra economizar memoria 
     
     time.sleep(5)
     keyboard.press_and_release('ctrl + w')

envio()


# Agende a função para ser executada a cada 30 minutos
schedule.every(10).seconds.do(envio)

# Loop para manter o programa em execução
while True:
    schedule.run_pending()
    time.sleep(1)  # Aguarde 1 segundo antes de verificar novamente

# O programa continuará em execução, e a função envio será chamada a cada 30 segundos.





# Encontre a janela do Power BI pelo título
#power_bi_window = gw.getWindowsWithTitle("Power BI")[0]

# Traga a janela do Power BI para o foco
#power_bi_window.activate()

# Capture a tela da janela do Power BI
#screenshot = pyautogui.screenshot(region=(power_bi_window.left, power_bi_window.top, power_bi_window.width, power_bi_window.height))

# Salve a captura de tela em um arquivo
#screenshot.save('screenshot.png')

# Envie a imagem pelo WhatsApp (certifique-se de ter o WhatsApp Web aberto)
#kit.sendfile('Seu_Número_de_Telefone', 'screenshot.png')



