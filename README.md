# Luna - Your Intelligent Personal Assistant

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
[![jQuery](https://img.shields.io/badge/jQuery-%230769AD.svg?style=for-the-badge&logo=jquery&logoColor=white)](https://jquery.com/)

Luna is a sophisticated personal assistant that combines the power of a Python backend (leveraging Flask and TensorFlow) with a dynamic and user-friendly web frontend (built with HTML, CSS, and JavaScript, including jQuery for enhanced interactivity). This architecture allows for intelligent natural language processing and a seamless conversational experience directly within your web browser.

## 🌟 Key Features

Luna offers a rich set of features powered by its integrated backend and frontend:

* **🗣️ Interactive Voice Communication:**
    * Utilizes the browser's Speech Recognition API for hands-free voice input. Simply speak to Luna through your microphone.
    * Employs the Web Speech Synthesis API to provide natural-sounding voice responses, enhancing the conversational flow.
    * Visually indicates the microphone status ("Listening...", "Speaking...") in the web interface.
* **🧠 Intelligent Backend Processing:**
    * Leverages a Python backend powered by Flask to handle user input.
    * Utilizes TensorFlow and a trained model (managed by `app.py`) for natural language understanding and response generation.
    * Supports various commands, including asking general knowledge questions and triggering specific actions.
* **⏰ Smart Reminder System (Backend & Frontend Integration):**
    * Enables you to set reminders through natural language commands (e.g., "remind me to water the plants in 5 minutes").
    * The backend (`app.py`) processes the reminder and triggers it at the specified time.
    * The frontend periodically checks for active reminders and displays them in a dedicated "Reminder" section, also providing an audible notification.
* **🎶 Local Music Playback (Backend Integration):**
    * The backend (`app.py`) can play local MP3 audio files based on your commands (e.g., "play some music").
    * Basic playback controls (play, pause, stop) are managed on the backend.
    * *(Note: The current frontend code doesn't have direct UI controls for music playback but relies on voice commands to trigger backend actions.)*
* **🔎 Web and YouTube Integration (Backend Integration):**
    * The backend (`app.py`) can interpret commands to open Google and YouTube searches in your web browser.
* **▶️ Direct YouTube Video Playback (Backend Integration):**
    * The backend (`app.py`) can directly play the first relevant YouTube video based on your search query in your browser.
* **📝 Conversation Logging (Backend Integration):**
    * The backend (`app.py`) logs all user inputs and Luna's responses to a `conversation_log.txt` file for record-keeping.
* **✨ Engaging User Interface:**
    * A clean and modern web interface built with HTML and styled with CSS.
    * Uses the "Open Sans" and "Poppins" fonts for a readable and aesthetically pleasing experience.
    * Features a scrollable chat container to display the conversation history.
    * Implements a subtle "typing" animation for Luna's responses to enhance engagement.
* **🚀 Dynamic Updates with jQuery:**
    * Utilizes the jQuery library to handle asynchronous communication with the backend (using AJAX) for sending user messages and receiving Luna's responses without page reloads.
    * jQuery is also used for dynamically updating the chat container with new messages and for periodically fetching and displaying reminders.



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


## 💡 How to Interact

Once the frontend is loaded in your browser:

1.  **Voice Input:** If your browser supports it and you grant microphone access, Luna will start listening. You can speak your commands or questions. The "Microphone Status" will indicate when Luna is listening or speaking.
2.  **Observe Responses:** Luna's text responses will appear in the chat container with a typing animation. If Luna is configured to speak, you will also hear the response.
3.  **Set Reminders:** Use natural language like "remind me to call John in 1 hour". The reminder will be displayed in the "Reminder" section when it's triggered.
4.  **Play Music:** Try commands like "play some music" (assuming you have audio files configured in the backend).
5.  **Web and YouTube Search:** Use commands like "open google and search for the weather" or "open youtube and search for funny cats".
6.  **Play YouTube Videos:** Try "play relaxing jazz on youtube".



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
