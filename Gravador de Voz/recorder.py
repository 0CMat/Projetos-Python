#pip install sounddevice
#pip install scipy

import sounddevice
from scipy.io.wavfile import write


fs = 44100
second = int(input("Digite o tempo de gravação em segundos:"))

print('GRAVANDO...')

record_voice = sounddevice.rec(int(second*fs), samplerate=fs, channels=2)
sounddevice.wait()


write("out.wav", fs, record_voice)

print("Acabou... \n Verifique o áudio.")
