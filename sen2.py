import numpy as np
import sounddevice as sd
import threading
import multiprocessing
import time
import sys
def wave():
    sd.default.samplerate = 44100

    time = 2.0
    frequency = 1000

    # Generate time of samples between 0 and two seconds
    samples = np.arange(44100 * time) / 44100.0
    # Recall that a sinusoidal wave of frequency f has formula w(t) = A*sin(2*pi*f*t)
    wave = 10000 * np.sin(2 * np.pi * frequency * samples)
    # Convert it to wav format (16 bits)
    wav_wave = np.array(wave, dtype=np.int16)
    sd.play(wav_wave, blocking=True)



t1 = threading.Thread(target=wave)
t2 = threading.Thread(target=wave)
t1.start()
print("onda uno")
time.sleep(0.5)
t2.start()
print("onda dos")
