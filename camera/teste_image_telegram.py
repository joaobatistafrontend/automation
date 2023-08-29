import cv2
import requests

video_capture = cv2.VideoCapture(0)
ret, frame = video_capture.read()

_, buffer = cv2.imencode('.jpg', frame)

files = {'photo':buffer}

#coloca o id do chat aqui
tarcisio_id = '5406497183'

def test():
    bot_chat_id = '2017950373'
    bot = '6143598138:AAE0KjLOFwW7MHnyh-Wdyyl9mWxNUnTKX4E'

    msg = 'você conhece essa pessoa\n' +'[sim] ligar imediatamente para a escola \n' + '[nao] ignora mensagem'
    
    #url da mensagem
    url_msg = f'https://api.telegram.org/bot{bot}/sendMessage?chat_id={bot_chat_id}&text={msg}'

    #url da imagem
    url_img = f'https://api.telegram.org/bot{bot}/sendPhoto?chat_id={bot_chat_id}'
    
    #manda a imagem
    resposta1 = requests.get(url_img, files=files)

    #manda a mensagem
    resposta2 = requests.get(url_msg)
    
    print(resposta1.status_code)
    print(resposta2.status_code)

test()