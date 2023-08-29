import requests
import cv2
import os


def SendImg():
    #endereço do bot do telegram 
    bot = '6143598138:AAE0KjLOFwW7MHnyh-Wdyyl9mWxNUnTKX4E'
    chat_id = '2017950373'

    #msg que deve aparecer 
    msg = 'você conheçe essa pessoa?'
    #enderecço para a msg ser redirecinada (parece  muito o conceico de endereçanto por url)
    #---------------------------------------(endereço do bot)
    #--------------------------------------------(a requisicao q vai ser aplicado)
    #-----------------------------------------------------------------(qual o endereço id vai ser redirecionado)
    #--------------------------------------------------------------------------------(a msg)
    url_msg = f'https://api.telegram.org/bot{bot}/sendMessage?chat_id={chat_id}&text={msg}'
    
    #aqui é onde ficara a img do desconhecido nao sei como aplicar
    parametros = {
        "photo": 'https://img.freepik.com/psd-gratuitas/ilustracao-de-renderizacao-3d-isolada-do-icone-do-google_47987-9777.jpg?w=740&t=st=1686686656~exp=1686687256~hmac=0f810184718201e3f9a914664dc33e349f80ca4bf9950696d3c0eb80caa2625e'
    }
    #msm esquema da msg so troca o SendPhoto
    url_img = f'https://api.telegram.org/bot{bot}/sendPhoto?chat_id={chat_id}'
    #----------------------------------------tem q passar esse Data para ele reocinhecer os paramentros
    resposta = requests.get(url_img, data=parametros)
    #tem q fazer 2 requeste pq ele nao suporta 2 requisicao
    resposta = requests.get(url_msg)
    print('status code:', resposta.status_code)
    print(resposta.json())
SendImg()
