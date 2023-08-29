import keyboard
import pywhatkit as pt
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


contatos = ['+5585986654154']
mensagem_alerta = 'test'


def envio():
     options = Options()
     #
     # options.add_argument('--headless=new')
     options.page_load_strategy = 'none'
     drive =webdriver.Chrome(options=options)
     #drive.get('https://wa.me//+5585986654154?text=Tenho%20interesse%20em%20comprar%20seu%20carro')
     drive.get(f"https://wa.me//{contatos}?text=Tenho%20interesse%20em%20comprar%20seu%20carro")
     drive.close()
     
envio()