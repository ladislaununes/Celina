import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os

# Inicializa o reconhecimento de voz e o mecanismo de síntese de voz
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Função para falar
def falar(texto):
    engine.say(texto)
    engine.runAndWait()

# Função para capturar comandos de voz
def capturar_comando():
    with sr.Microphone() as source:
        print("Estou ouvindo...")
        audio = recognizer.listen(source)

    try:
        comando = recognizer.recognize_google(audio, language="pt-BR")
        return comando.lower()
    except sr.UnknownValueError:
        return "Não entendi o que você disse."
    except sr.RequestError:
        return "Não foi possível acessar o serviço de reconhecimento de voz."

# Função para executar comandos
def executar_comando(comando):
    # Saber as Horas
    if "diga as horas" in comando or "que horas são" in comando:
        agora = datetime.datetime.now().strftime("%H:%M")
        resposta = f"Agora são {agora}."
        print(resposta)
        falar(resposta)
    # Saber o dia da Semana
    elif "que dia é hoje" in comando:
        # Dia
        dia = datetime.datetime.now().day
        # Mês
        num_mes = datetime.datetime.now().month
        if (num_mes == 1):
            mes = "Janeiro"
        elif (num_mes == 2):
            mes = "Fevereiro"
        if (num_mes == 3):
            mes = "Março"
        elif (num_mes == 4):
            mes = "Abril"
        elif (num_mes == 5):
            mes = "Maio"
        elif (num_mes == 6):
            mes = "Junho"
        elif (num_mes == 7):
            mes = "Julho"
        elif (num_mes == 8):
            mes = "Agosto"
        elif (num_mes == 9):
            mes = "Setembro"
        elif (num_mes == 10):
            mes = "Outubro"
        elif (num_mes == 11):
            mes = "Novembro"
        else:
            mes = "Dezembro"
        # Ano
        ano = datetime.datetime.now().year
        
        resposta = f"Hoje são {dia} de {mes} de {ano}"
        print(resposta)
        falar(resposta)
    # Pesquisar na Web
    elif "pesquisar" in comando:
        falar("O que você deseja pesquisar?")
        termo = capturar_comando()
        url = f"https://www.google.com/search?q={termo}"
        webbrowser.open(url)
    # Apresentação da Assistente
    elif "se apresente assistente" in comando or "se apresenta assistente" in comando:
        falar("Eu sou a Celina, o assistente virtual criado por Ladislau Nunes. É um prazer ajudar vocês.")
    # Abrir o Google Chrome
    elif "abra o google" in comando:
        falar("Abrindo o Google Chrome")
        os.system('"C:/Program Files/Google/Chrome/Application/chrome.exe"')
    # Encerrar o Programa
    elif "encerrar" in comando or "fechar programa" in comando:
        falar("Encerrando o assistente de voz. Até a próxima")
        exit()
    else:
        falar("Comando não reconhecido.")

# Loop principal
while True:
    comando = capturar_comando()
    print("Você disse:", comando)
    executar_comando(comando)
