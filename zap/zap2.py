import time
import keyboard
import pywhatkit as pt
from datetime import datetime 





contatos = ['+5585986654154']
mensagem_alerta = '*Assunto: Alerta de identificação de pessoa não autorizada acompanhando seu filho(a)* ' +'\n'+'\n' 'Prezados pais/responsáveis, ' +'\n'+'\n' 'Esperamos que esta mensagem os encontre bem. Gostaríamos de informar que nosso sistema de reconhecimento facial para controle escolar identificou recentemente uma situação em que seu filho(a), foi visto saindo com uma pessoa desconhecida, não autorizada previamente por vocês. \n'+'Gostaríamos de solicitar sua colaboração para esclarecermos essa situação. Pedimos que, por favor, verifiquem se conhecem a pessoa retratada na imagem anexa a esta mensagem. Caso vocês a conheçam ou possuam informações relevantes sobre ela, solicitamos que nos informem o mais breve possível, para que possamos investigar o ocorrido de maneira adequada. \n' +'\n'+'\n'+ 'Agradecemos antecipadamente pela sua cooperação e compreensão. Ficamos à disposição para qualquer esclarecimento adicional ou para discutir quaisquer preocupações que possam surgir.'

def envio():
    pt.sendwhatmsg_instantly(contatos,mensagem_alerta)
    keyboard.press_and_release('ctrl + w')
img = 'img/tarcisio.jpg'
def envioImg():
    while len(contatos)>= 1:
        pt.sendwhats_image(contatos[0],img,mensagem_alerta)
        del contatos[0]   
        time.sleep(15)
        keyboard.press_and_release('ctrl + w')
    else:
        pt.sendwhats_image(contatos,img,mensagem_alerta)
        keyboard.press_and_release('ctrl + w')
envioImg()

'''while len(contatos)>= 1:
    pywhatkit.sendwhatmsg(contatos[0],f'{test}',datetime.now().hour,datetime.now().minute + 1)
    del contatos[0]
    time.sleep(15)
    keyboard.press_and_release('ctrl + w')'''