from twilio.rest import Client

def test():
     account_sid = 'AC0bd74eaff26694ed15d5c741f579b6ba'
     auth_token = 'c8c3bcb2725f68de1fb652b79d7ff8aa'
     client = Client(account_sid, auth_token)
     message = client.messages.create(
     body='test',
     from_= '14786069077',
     to='5585996511151'
     )
test()