# Luna - Your Intelligent Personal Assistant

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)

Luna is a sophisticated personal assistant built with the power of Python, the flexibility of Flask for its web interface, and the intelligence of TensorFlow for natural language understanding. It integrates various specialized libraries to offer a rich and interactive user experience.

## 🌟 Core Capabilities

At its heart, Luna is designed to understand and respond to your needs effectively. Here's a detailed breakdown of its capabilities, primarily driven by the `app.py` module:

* **🧠 Intelligent Natural Language Processing (NLP):**
    * Leverages TensorFlow and the scikit-learn library (`TfidfVectorizer`) to analyze and understand the intent behind your text-based commands.
    * Trained on a structured dataset (`data.json`) to recognize patterns and provide relevant responses.
    * Continuously learns and improves its understanding through the training process initiated upon startup.
* **🌐 Intuitive Web Interface:**
    * Built using the Flask microframework, providing a clean and accessible web-based interface (`index.html`) for seamless interaction.
    * Allows you to communicate with Luna through text input directly in your web browser.
* **🗣️ Natural Text-to-Speech Feedback:**
    * Utilizes the `playsound` library to deliver clear and audible responses, enhancing the interaction beyond just text.
* **🌍 Real-time Multilingual Translation:**
    * Incorporates the `deep-translator` library (specifically using Google Translate) to understand your commands in various languages and respond in English. This makes Luna accessible to a broader user base.
* **⏰ Smart Reminder System:**
    * Enables you to set timely reminders for important tasks. You can specify the action and the time duration (in seconds, minutes, or hours) after which the reminder should be triggered.
    * Provides an audible notification (through the console) and displays the reminder message on the web interface.
* **🎶 Integrated Local Music Player:**
    * Features the ability to play local MP3 audio files using the `pygame` library.
    * Supports basic playback controls such as play, pause, and stop.
    * Offers the option to loop certain audio tracks for continuous playback (e.g., for ambient sounds or alerts).
* **🔎 Seamless Web and YouTube Integration:**
    * Allows you to initiate Google searches directly through voice or text commands, opening the search results in your default web browser.
    * Similarly, you can search for videos on YouTube, and Luna will open the YouTube search results in your browser.
* **▶️ Direct YouTube Video Playback:**
    * Goes beyond just searching; Luna can directly play the first relevant YouTube video based on your search query within your web browser using the powerful `yt-dlp` library.
* **📝 Comprehensive Conversation Logging:**
    * Maintains a detailed record of your interactions with Luna in a `conversation_log.txt` file. This log includes both your input and Luna's responses, which can be helpful for reviewing past interactions or debugging.
* **⚙️ Automated Initial Model Training:**
    * Upon the first run of `app.py`, Luna automatically preprocesses the training data from `data.json`, builds its neural network model using TensorFlow, and trains the model. This ensures that Luna is ready to understand and respond to your queries from the outset.

## 🚀 Getting Started - Step-by-Step Guide

Follow these detailed instructions to install and run Luna on your system:

### Step 1: Installing Prerequisites

1.  **Python Installation:**
    * Luna requires Python version 3.7 or higher.
    * **Check your Python version:** Open your terminal or command prompt and run:
        ```bash
        python --version
        ```
        or
        ```bash
        python3 --version
        ```
    * If your Python version is below 3.7 or if Python is not installed, download the latest version from the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/) and follow the installation instructions for your operating system.

### Step 2: Setting Up the Project Files

1.  **Download or Clone the Luna Project:** Obtain the Luna project files (e.g., by downloading a ZIP archive or cloning a Git repository if available).
2.  **Navigate to the Project Directory:** Open your terminal or command prompt and use the `cd` command to navigate to the main directory of the Luna project where the `requirements.txt` file is located.

### Step 3: Installing Dependencies

1.  **Install Required Python Packages:** Execute the following command in your terminal to install all the necessary Python libraries listed in the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```
    This command will automatically download and install packages like Flask, TensorFlow, scikit-learn, playsound, deep-translator, PyAudio, pygame, and yt-dlp. Ensure your internet connection is stable during this process.

### Step 4: Running Luna's Core Brain (`app.py`)

1.  **Execute the Main Application:** In the same terminal where you navigated to the project directory, run the `app.py` script using the Python interpreter:
    ```bash
    python app.py
    ```
    This command will start the Flask development server. You should see output in your terminal indicating that the server is running (typically on `http://127.0.0.1:5000/`).

### Step 5: Interacting with Luna

1.  **Open the Web Interface:** Once the Flask server is running, open your preferred web browser and navigate to the address provided in your terminal (usually `http://127.0.0.1:5000/`). You should see Luna's web interface.
2.  **Send Commands:** Use the text input field on the web page to type your commands or questions for Luna.
3.  **Observe Responses:** Luna's responses will be displayed on the web interface. You might also hear audio feedback for certain actions.
4.  **Explore Features:** Try out the various features mentioned earlier, such as setting reminders, playing music, initiating web searches, and asking questions.

### Example Interactions:

* **Setting a reminder:** Type "remind me to drink water in 30 minutes" and press Enter.
* **Playing local music:** Type "play some music" and press Enter.
* **Searching Google:** Type "open google and search for the latest news" and press Enter.
* **Searching YouTube:** Type "open youtube and search for funny dog videos" and press Enter.
* **Playing a YouTube video:** Type "play relaxing piano music on youtube" and press Enter.

### Step 6: Stopping Luna

To stop the Luna application, simply go back to the terminal where you ran `python app.py` and press `Ctrl + C`. This will shut down the Flask development server.

## 📜 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). This permissive license allows you to use, modify, and distribute the code freely, as long as you include the original copyright and license notice in any copies of the software.
