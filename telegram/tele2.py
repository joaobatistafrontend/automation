from telethon import TelegramClient, sync, events
import requests

tarcisio_id = '5406497183'
n = '5585987892235'
darueira = '6143598138'

api_id = '8932162'
api_hast = '62fbd8516b50af87f1c6337a91e30dba'
sessao = 'testando'
def Idgrupo():
     cliente = TelegramClient(sessao, api_id, api_hast)
     cliente.start()
     dialogs = cliente.get_dialogs()
     for dialog in dialogs:
          print('------------')
          if dialog.id > 0:
               print(f'grupo: {dialog.title}')
               print(f'Id: {dialog.id}')
               print(f'Numero: {dialog.entity.phone}')
          cliente.disconnect()


def SendMessage():
     print('------------')
     cliente = TelegramClient(sessao, api_id, api_hast)
     @cliente.on(events.NewMessage(chats = [5406497183])) #grupo resseptor
     async def evair_mensagem(events):
          await cliente.send_message(6143598138, events.raw_text)
     cliente.start()
     cliente.run_until_disconnected()


def test():
     
     bot = '6143598138:AAE0KjLOFwW7MHnyh-Wdyyl9mWxNUnTKX4E'
     bot_chat_id = '2017950373'

     api_id = '8932162'
     api_hast = '62fbd8516b50af87f1c6337a91e30dba'

     msg = 'você conhece essa pessoa\n' +'[sim] ligar imediatamente para a escola \n' + '[nao] ignora mensagem'

     url_msg = f'https://api.telegram.org/bot{bot}/sendMessage?chat_id={bot_chat_id}&text={msg}'

     img = 'https://img.freepik.com/psd-gratuitas/ilustracao-de-renderizacao-3d-isolada-do-icone-do-google_47987-9777.jpg?w=740&t=st=1686686656~exp=1686687256~hmac=0f810184718201e3f9a914664dc33e349f80ca4bf9950696d3c0eb80caa2625e'

     parametros = {
        "photo": img
     }
     url_img = f'https://api.telegram.org/bot{bot}/sendPhoto?chat_id={bot_chat_id}'
     
     
     resposta = requests.get(url_img, data=parametros)
     resposta = requests.get(url_msg)
     print(resposta.json())
test()


