import win32com.client as win32

outlook = win32.Dispatch("Outlook.Application")

email = outlook.CreateItem(0)
email.To = 'jbbuno007@gmail.com' 
email.Subject = 'testando'
email.Body ='test'
email.Send()