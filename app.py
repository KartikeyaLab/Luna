# This is Luna's main brain.
# Run this program first.
# Refer to the requirements file to install necessary packages.

TF_ENABLE_ONEDNN_OPTS=0

import json
import numpy as np
from flask import Flask, render_template, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical
from playsound import playsound
from deep_translator import GoogleTranslator
import webbrowser
import string
import pygame
import time
import os
import threading
import re
import yt_dlp

pygame.mixer.init()



def play_youtube_video(search_query):
    ydl_opts = {
        'quiet': True,
        'format': 'best[ext=mp4]/best',
        'noplaylist': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch:{search_query}", download=False)

        if 'entries' in info and info['entries']:
            video = info['entries'][0]
            direct_url = video.get('url') 
            final_url = direct_url + "&autoplay=1"    
        
            if not direct_url:
                print("Couldn't extract direct video URL.")
                return
            webbrowser.open(final_url)
            print(f"Playing direct video for: '{search_query}'")
        else:
            print("No video found for that search query.")



reminder_message = ""

def set_reminder(time_value, action, time_unit):
    global reminder_message

    # Convert time_value to seconds based on the unit
    if time_unit == "seconds":
        time_in_seconds = time_value
    elif time_unit == "minute" or time_unit == "minutes":
        time_in_seconds = time_value * 60
    elif time_unit == "hour" or time_unit == "hours":
        time_in_seconds = time_value * 3600
    else:
        time_in_seconds = 0  # Default to 0 if the unit is invalid
    
    time.sleep(time_in_seconds)  # Wait for the specified time
    reminder_message = f"Sir, this is a timely reminder to {action}"  # Set the reminder message after the specified time
    print(reminder_message)  # Log the reminder

    time.sleep(5)  
    reminder_message = ""  # Clear the reminder message after 5 seconds

written_numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10
}

def get_number(value):
    if value.isdigit():  
        return int(value)
    elif value in written_numbers:  
        return written_numbers[value]
    else:
        return 0


song_path = {
    "cornfield": "Audio/Cornfield Chase Interstellar.mp3",
    "devil": "Audio/Me and the devil.mp3",
    "sad": "Audio/Loki.mp3",
    "skyfall": "Audio/Skyfall.mp3",
    "royalty": "Audio/Royalty.mp3",
    "emergency": "Audio/Danger.mp3"
}

is_playing = False

def play_song(song_path, loop=False):
    global is_playing
    if os.path.exists(song_path):  
        time.sleep(2) 
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play(-1 if loop else 0)  # -1 means infinite loop
        is_playing = True
        print(f"Now playing: {song_path}")


def stop_song():
    global is_playing
    pygame.mixer.music.stop()
    is_playing = False
    print("Playback stopped.")

def song_player():
    global is_playing
    while True:
        if is_playing and not pygame.mixer.music.get_busy():
            is_playing = False
            print("Song finished.")
        time.sleep(1)  

app = Flask(__name__)

class NeuralNetworkLuna:
    def __init__(self, data_file):
        self.data_file = data_file
        self.load_data()
        self.vectorizer = TfidfVectorizer()
        self.label_encoder = LabelEncoder()
        self.model = None

    def load_data(self):
        try:
            with open(self.data_file, 'r') as file:
                self.data = json.load(file)
            self.questions = list(self.data.keys())
            self.answers = list(self.data.values())
        except FileNotFoundError:
            print("Data file not found. Please provide a valid data.json file.")
            self.data = {}
            self.questions = []
            self.answers = []
        except json.JSONDecodeError:
            print("Error decoding JSON. Please check the data.json file format.")
            self.data = {}
            self.questions = []
            self.answers = []

    def preprocess_data(self):
        x = self.vectorizer.fit_transform(self.questions).toarray()
        y = self.label_encoder.fit_transform(self.answers)
        y = to_categorical(y)
        return x, y

    def build_model(self, input_dim, output_dim):
        model = Sequential([ 
            Dense(128, input_dim=input_dim, activation='relu'),
            Dropout(0.5),
            Dense(64, activation='relu'),
            Dropout(0.5),
            Dense(output_dim, activation='softmax')
        ])
        model.compile(optimizer=Adam(learning_rate=0.01), loss='categorical_crossentropy', metrics=['accuracy'])
        self.model = model

    def train_model(self, x, y, epochs=100):
        self.model.fit(x, y, epochs=epochs, batch_size=8, verbose=1)

    def get_response(self, user_input):
        input_vector = self.vectorizer.transform([user_input]).toarray()
        prediction = self.model.predict(input_vector)
        predicted_label = np.argmax(prediction)
        response = self.label_encoder.inverse_transform([predicted_label])
        return response[0]

data_file = "data.json"
luna = NeuralNetworkLuna(data_file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_reminder', methods=['GET'])
def get_reminder():
    if reminder_message:
        return jsonify({'reminder': reminder_message})
    else:
        return jsonify({'reminder': ''})  # Return empty if no reminder is active


@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form.get('user_input')
    print(f"User Input: {user_input}")  # Debug line

    reminder_match = re.search(r'(set a reminder to|remind me to|can you set a reminder|reminder to) (.*?) (in|after) (\d+|one|two|three|four|five|six|seven|eight|nine|ten) (seconds|minute|minutes|hour|hours)', user_input.lower())

    if reminder_match:
        action = reminder_match.group(2).strip()  # Get the action
        time_value = reminder_match.group(4).strip()  # Get the time value (number or word)
        time_unit = reminder_match.group(5)  # Get the time unit

        # Convert time_value (which could be a number or word) to integer
        time_value = get_number(time_value)

        # Pass all three arguments (time_value, action, time_unit) to set_reminder
        threading.Thread(target=set_reminder, args=(time_value, action, time_unit)).start()

        return jsonify({'response': f"Reminder set to '{action}' in {time_value} {time_unit}."})

    if reminder_message:
        return jsonify({'response': reminder_message})
    

    if is_playing:
        if 'pause' in user_input.lower() or 'stop' in user_input.lower():
            threading.Thread(target=stop_song).start()
            return jsonify({'response': f"Ceased playing the music"})
        else:
            # Ignore other commands if music is playing
            return jsonify({'response': "I can only pause or stop the music while it's playing."})
        
   
    elif 'pause' in user_input.lower() or 'stop' in user_input.lower():
        # Ignore pause/stop if no music is playing
        return jsonify({'response': "No music is playing to pause or stop."})

    # Continue with the usual commands when music is not playing
    if 'open google and search for' in user_input.lower():
        search_query = user_input.lower().split('open google and search for', 1)[1].strip()

        if search_query:
            search_query = ''.join(char for char in search_query if char not in string.punctuation)

            search_url = f'https://www.google.com/search?q={search_query}'
            webbrowser.open(search_url, new=2)
            return jsonify({'response': f"Opening Google and searching for: {search_query}"})

    elif 'open youtube and search for' in user_input.lower():
        search_query = user_input.lower().split('open youtube and search for', 1)[1].strip()

        if search_query:
            search_query = ''.join(char for char in search_query if char not in string.punctuation)

            search_url = f'https://www.youtube.com/results?search_query={search_query}'
            webbrowser.open(search_url, new=2)
            return jsonify({'response': f"Opening YouTube and searching for: {search_query}"})

    elif 'play some music' in user_input.lower():
        threading.Thread(target=play_song, args=(song_path["cornfield"],)).start()
        return jsonify({'response': f"Playing Cornfield Chase from Interstellar."})

    elif 'play me and the devil' in user_input.lower() or 'devil' in user_input.lower():
        threading.Thread(target=play_song, args=(song_path["devil"],)).start()
        return jsonify({'response': f"Playing, Me and the Devil now"})
    
    elif 'play skyfall' in user_input.lower() or 'skyfall' in user_input.lower():
        threading.Thread(target=play_song, args=(song_path["skyfall"],)).start()
        return jsonify({'response': f"Now playing, Skyfall"})
    
    elif 'play emergency' in user_input.lower() or 'emergency' in user_input.lower():
        threading.Thread(target=play_song, args=(song_path["emergency"], True)).start()
        return jsonify({'response': f"Alert! Emergency sound activated."})
    
    elif 'play royalty' in user_input.lower() or 'royalty' in user_input.lower():
        threading.Thread(target=play_song, args=(song_path["royalty"],)).start()
        return jsonify({'response': f"Now playing Royalty."})
    
    elif 'sad' in user_input.lower() or 'sad' in user_input.lower()  or 'sad' in user_input.lower():
        threading.Thread(target=play_song, args=(song_path["sad"],)).start()
        return jsonify({'response': f"Playing instrumental music."})
    

    elif 'play' in user_input.lower() and 'on youtube' in user_input.lower():
        search_query = user_input.lower().split('play', 1)[1].split('on youtube')[0].strip()

        if search_query:
          response = play_youtube_video(search_query)
          return jsonify({'response': f"Opening Youtube and playing {search_query}."})
   
    else:
        # Translate input and process as normal if no music is playing
        translated_input = GoogleTranslator(source='auto', target='en').translate(user_input)
        response = luna.get_response(translated_input)
        return jsonify({'response': response})


@app.route('/log_conversation', methods=['POST'])
def log_conversation():
    user_message = request.form.get('user_message')
    luna_response = request.form.get('luna_response')
    
    print(f"You: {user_message}")
    print(f"Luna: {luna_response}")

    with open('conversation_log.txt', 'a') as log_file:
        log_file.write(f"You: {user_message}\nLuna: {luna_response}\n\n")
    
    return jsonify({'status': 'success'})

def train_model_on_start(): 
    x, y = luna.preprocess_data()
    input_dim = x.shape[1]
    output_dim = y.shape[1]

    audio_file_training = 'Audio/Training.mp3'  
    playsound(audio_file_training)

    luna.build_model(input_dim, output_dim)
    luna.train_model(x, y, epochs=100)

    audio_file_trained = 'Audio/Trained.mp3' 
    playsound(audio_file_trained)

if __name__ == "__main__":
    
    train_model_on_start()
    threading.Thread(target=song_player, daemon=True).start()  
    app.run(debug=True, use_reloader=False)
