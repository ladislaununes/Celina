import speech_recognition as sr
import pyttsx3
import wikipedia

#Cria um reconhecedor
r = sr.Recognizer()
maquina = pyttsx3.init()

#Abrir o microfone para captura
with sr.Microphone() as source:
    print("Estou escutando...!")
    while True:
        voz = r.listen(source) #Define microfone como fonte de áudio
        comando = r.recognize_google(voz, language='pt')
        if 'procure por' in comando or 'pesquise por' in comando:
            procurar = comando.replace('procure por', '')
            procurar = comando.replace('pesquise por', '')
            wikipedia.set_lang('pt')
            resultado = wikipedia.summary(procurar, sentences=2)
            print(resultado)
            maquina.say(resultado)
            maquina.runAndWait()
        if 'Celina' in comando:
            comando = comando.replace('Celina', '')
        maquina.say(comando)
        maquina.runAndWait()

        


'''
#!/usr/bin/env python3

from vosk import Model, KaldiRecognizer
import os
import pyaudio

# Reconhecimento de fala

model = Model('model')
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

# Loop do reconhecimento de fala
while True:
    data = stream.read(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        print(rec.result)
    else:
        print(rec.PartialResult())

print(rec.FinalResult())
'''