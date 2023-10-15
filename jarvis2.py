import os
import time
import webbrowser
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia

# Configurar o mecanismo TTS (Text-to-Speech)
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Velocidade de fala

# Configurar o reconhecimento de voz
recognizer = sr.Recognizer()
microphone = sr.Microphone()

# Diretório do modelo Vosk
vosk_model_path = "caminho/para/o/modelo/vosk/model"

# Função para falar uma resposta
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Função para obter a hora atual
def get_time():
    current_time = datetime.datetime.now().strftime("%H:%M")
    speak(f"A hora atual é {current_time}")

# Função para realizar uma pesquisa na web
def web_search(query):
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)
    speak(f"Aqui estão os resultados da pesquisa para {query}")

# Inicialização do Vosk
if os.path.exists(vosk_model_path):
    import vosk
    vosk.SetLogLevel(-1)
    model = vosk.Model(vosk_model_path)
else:
    print("O modelo Vosk não foi encontrado. Certifique-se de definir o caminho correto.")
    exit()

with microphone as source:
    recognizer.adjust_for_ambient_noise(source)

speak("Olá! Como posso ajudar você?")

while True:
    with microphone as source:
        try:
            audio = recognizer.listen(source, timeout=10)
            text = recognizer.recognize_google(audio, show_all=False)
            text = text.lower()

            if "hora" in text:
                get_time()
            elif "pesquisar" in text:
                speak("O que você gostaria de pesquisar?")
                audio = recognizer.listen(source, timeout=10)
                search_query = recognizer.recognize_google(audio, show_all=False)
                web_search(search_query)
            elif "parar" in text:
                speak("Até mais!")
                break
            else:
                speak("Desculpe, não entendi. Você pode repetir?")
        except sr.WaitTimeoutError:
            speak("Desculpe, não ouvi nada. Você pode repetir?")
        except sr.RequestError:
            speak("Desculpe, ocorreu um erro na minha capacidade de fala.")
