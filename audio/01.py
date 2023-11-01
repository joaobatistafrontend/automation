import speech_recognition as sr
import pyaudio
import pyttsx3
import datetime
import wikipedia
import pywhatkit




audio = sr.Recognizer()
maquina = pyttsx3.init()

def iniciar():
     try:
          with sr.Microphone() as micro:
                    print('ouvindo')
                    #pegar apenas as ondulaçoes autas
                    audio.adjust_for_ambient_noise(micro)
                    voz = audio.listen(micro)
                    comando = audio.recognize_google(voz,language='pt-BR')
                    comando = comando.lower() 
                    if 'chico' in comando:
                         comando = comando.replace('chico', '')
                         maquina.say(comando)
                         maquina.runAndWait()
     except:
          print('sem audio')
     return comando


def usuario():
     comando = iniciar()
     if 'horas' in comando:
          hora = datetime.datetime.now().strftime('%H:%M')
          maquina.say(f'Agora são: {hora}')
          maquina.runAndWait()
     elif 'procure por' in comando:
          procurar = comando.replace('procure por', '')
          wikipedia.set_lang('pt')
          resultado = wikipedia.summary(procurar,2)
          print(resultado )
          maquina.say(resultado)
          maquina.runAndWait()
     elif 'toque' in comando:
          print('vou procurar')
          musica = comando.replace('toque', 'toque')
          print('procurando')
          resultado = pywhatkit.playonyt(musica)
          maquina.say('tocando musica')
          maquina.runAndWait()

usuario()