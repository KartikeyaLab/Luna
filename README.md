# Luna

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Luna is a versatile assistant powered by Python, Flask, TensorFlow, and a collection of specialized libraries. This core module (`app.py`) forms the central brain of Luna, handling natural language processing, web interface interactions, and various other functionalities.

## ✨ Key Features Implemented in `app.py`

This central module enables Luna to perform the following actions:

* **🧠 Advanced Natural Language Processing:** Utilizes TensorFlow and scikit-learn for intent recognition and response generation based on a trained model (`data.json`).
* **🌐 User-Friendly Web Interface:** Provides a web interface built with Flask (`index.html`) for easy interaction.
* **🗣️ Text-to-Speech Playback:** Integrates with `playsound` to play audio prompts and feedback.
* **🌍 Real-time Translation:** Leverages `deep-translator` (Google Translate) to understand and respond in multiple languages.
* **⏰ Reminder Setting:** Allows users to set reminders for specific actions with customizable timeframes (in seconds, minutes, or hours).
* **<0xF0><0x9F><0x8E><0x9E> Local Music Playback:** Can play local audio files (MP3 format) with controls for play, pause, and stop using `pygame`. Supports looping for continuous playback.
* **🔎 Web Browsing Integration:** Enables opening Google searches and YouTube searches directly from user commands.
* **▶️ YouTube Video Playback:** Can directly play YouTube videos in your web browser based on search queries using `yt-dlp`.
* **📝 Conversation Logging:** Records user inputs and Luna's responses to a `conversation_log.txt` file for review and debugging.
* **⚙️ Initial Model Training:** Automatically trains the NLP model on startup using the data provided in `data.json`.

## 🛠️ Installation

Before running `app.py`, ensure you have followed the general installation steps outlined in the main README to set up the prerequisites and install the necessary dependencies from `requirements.txt`.

## 🚀 Running the Core Brain

1.  **Navigate to the Project Directory:** Open your terminal or command prompt and go to the Luna project directory.
2.  **Run `app.py`:** Execute the following command to start the main Luna application:

    ```bash
    python app.py
    ```

    This will launch the Flask development server, and Luna's web interface should be accessible in your web browser (typically at `http://127.0.0.1:5000/`).

## 💡 Usage

Interact with Luna through the web interface that appears in your browser. You can use the input field to type commands. Here are some examples of what you can do:

* **Ask Questions:** Luna will try to understand your questions based on its trained NLP model.
* **Set Reminders:** Try commands like "set a reminder to water the plants in 5 minutes" or "remind me to call John after 1 hour".
* **Play Local Music:** Say "play some music" to play a default song, or try specific commands like "play me and the devil", "play skyfall", etc. You can also "pause" or "stop" the currently playing music.
* **Search the Web:** Use commands like "open google and search for the weather today".
* **Search YouTube:** Try "open youtube and search for funny cat videos".
* **Play YouTube Videos:** Say "play [video title] on youtube" (e.g., "play relaxing jazz music on youtube").

Luna will process your input, and the response will be displayed on the web interface. Interactions are also logged in the `conversation_log.txt` file.

## 📄 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
