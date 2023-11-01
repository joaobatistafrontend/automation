import pygetwindow as gw
import pyautogui
import pywhatkit as kit
import time
import keyboard

# Envie a imagem pelo WhatsApp (certifique-se de ter o WhatsApp Web aberto)
#kit.sendfile('+5585992801602', 'screenshot.png')


contatos = ['+5585992801602']

import pyautogui
import time

def envioImg():
    # Inicialize o objeto do teclado


    # Encontre a janela do Power BI pelo título
    power_bi_window = gw.getWindowsWithTitle("Power BI")[0]

    # Traga a janela do Power BI para o foco
    power_bi_window.activate()

    # Tirar um screenshot da tela
    keyboard.press_and_release('alt+print_screen')

    # Aguarde um momento para garantir que a captura de tela seja processada
    time.sleep(1)

    # Cole a captura de tela no Power BI
    keyboard.on_press_key(keyboard.control_l_key)
    keyboard.tap_key('v')
    keyboard.release_key(keyboard.control_l_key)

    # Clique na área de escrita de mensagens (ajuste as coordenadas conforme necessário)
    pyautogui.click(x=500, y=900)

    # Pressione Ctrl+W para fechar a janela
    keyboard.press_key(keyboard.control_l_key)
    keyboard.tap_key('w')
    keyboard.release_key(keyboard.control_l_key)

envioImg()
