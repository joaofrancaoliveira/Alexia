import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

engine.say('Eu sou a Maria')
engine.say('Em que posso ajudar?')
engine.runAndWait()

def falar(texto):
    engine.say(texto)
    engine.runAndWait()

def esperando_comando():
    try:
        with sr.Microphone() as source:
            print('Escutando...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language='pt-BR')
            print(command)
            command = command.lower()
            if 'maria' in command:
                command = command.replace('maria', '')

    except:
        pass

    return command

def rodar_alexia():
    command = esperando_comando()
    if 'tocar' in command:
        musica = command.replace('tocar', '')
        falar('Eu vou tocar' + musica)
        pywhatkit.playonyt(musica)
    elif 'horas' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        falar('A hora atual é ' + time)
    elif 'wiki' in command:
        person = command.replace('wiki', '')
        wikipedia.set_lang('pt')
        info = wikipedia.summary(person, 1)
        print(info)
        falar(info)
    elif 'pesquisar no google' in command:
        pesquisa = command.replace('pesquisar no google', '')
        pesquisar = 'https://www.google.com/search?q=' + pesquisa
        webbrowser.open(pesquisar) 
    elif 'limitado' in command:
        falar('Limitado Check!')       

while True:
    rodar_alexia()