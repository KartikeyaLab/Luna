# Run this after starting app.py and then clap at least twice. It will launch the Flask server in your default browser.

import pyaudio
import numpy as np
from scipy.signal import butter, lfilter, stft
import time
import webbrowser
from playsound import playsound
import threading
import edge_tts
import asyncio


# gender = input("Enter your gender (M/F):")
gender = "f" # Set your gender Male(M/m) | Female(F/f)


gender.lower()
if gender == "f":
    BEFORE_BROWSER_AUDIO = "Activating Luna. Luna is now activated. Hello mam, welcome back."
else:
    BEFORE_BROWSER_AUDIO = "Activating Luna. Luna is now activated. Hello sir, welcome back."


VOICE = "en-GB-SoniaNeural"
OUTPUT_FILE = "Static/output.mp3"

CHUNK = 1024  
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CLAP_THRESHOLD = 5500 
MIN_CLAP_INTERVAL = 0.7 
CLAP_FREQUENCY_RANGE = (500, 3000) 

last_clap_time = 0
clap_count = 0

# ------------------------ SPEAK FUNCTION ------------------------ #
async def speak_async(text):
    if not text.strip():
        print("Please provide some text for speech.")
        return
    print("Generating speech...")
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(OUTPUT_FILE)
    print("Playing audio...")
    playsound(OUTPUT_FILE)
    print("Done speaking.")

def speak(text):
    asyncio.run(speak_async(text))

# ------------------------ CLAP DETECTION UTILS ------------------------ #
def butter_bandpass(lowcut, highcut, fs, order=5):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    return b, a

def bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

def compute_spectrogram(data, fs):
    f, t, Zxx = stft(data, fs, nperseg=1024)
    return f, t, Zxx

def detect_clap(data):
    global last_clap_time, clap_count
    audio_data = np.frombuffer(data, dtype=np.int16)
    filtered_data = bandpass_filter(audio_data, CLAP_FREQUENCY_RANGE[0], CLAP_FREQUENCY_RANGE[1], RATE)
    
    amplitude = np.max(np.abs(filtered_data))
    if amplitude > CLAP_THRESHOLD:
        f, t, Zxx = compute_spectrogram(filtered_data, RATE)
        avg_freq = np.mean(f[(f > CLAP_FREQUENCY_RANGE[0]) & (f < CLAP_FREQUENCY_RANGE[1])])

        if 0 < avg_freq < CLAP_FREQUENCY_RANGE[1]:
            current_time = time.time()
            if clap_count == 0 or (current_time - last_clap_time >= MIN_CLAP_INTERVAL):
                clap_count += 1
                last_clap_time = current_time
                return True
    return False

# ------------------------ MAIN ACTION ------------------------ #
def open_browser():
    speak(BEFORE_BROWSER_AUDIO)
    print("Two claps detected! Opening browser...")
    webbrowser.open("http://127.0.0.1:5000/")

# ------------------------ MAIN LISTENER ------------------------ #
def main():
    global clap_count
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Listening for claps...")

    try:
        while clap_count < 2:
            data = stream.read(CHUNK, exception_on_overflow=False)
            if detect_clap(data):
                print(f"Clap {clap_count} detected!")
        # Start browser + speech in new thread
        threading.Thread(target=open_browser).start()

    except KeyboardInterrupt:
        print("Exiting...")

    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()

if __name__ == "__main__":
    main()