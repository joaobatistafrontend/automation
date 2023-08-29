import requests

def enviar_sms():
    url = "https://api.smsdev.com.br/v1/send"
    chave_api = "H94KGYZ12YOH3SWVURMB6I73N3WUR0M12G05G62UCC0XUXBTOWBOB3F5D0F7ZM35FOMKYYQ64N91GIXC07J2416GHGCFS5ZS1NHTW20TKLPRMCHE8ZA3O9LW4YZR4QZ6"
    tipo_mensagem = "9"
    numero_destino = "558592049026"
    mensagem = "chiquita"

    parametros = {
        "key": chave_api,
        "type": tipo_mensagem,
        "number": numero_destino,
        "msg": mensagem
    }

    response = requests.get(url, params=parametros)

    if response.status_code == 200:
        resposta_json = response.json()
        return resposta_json
    else:
        print("Falha na requisição. Código de status:", response.status_code)
        return None

resultado = enviar_sms()
print(resultado)
