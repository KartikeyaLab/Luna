# Luna

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Luna is a versatile assistant built using a powerful combination of technologies, including Python, Flask, TensorFlow, and various specialized libraries. It offers a range of functionalities to enhance your interaction with technology.

## ✨ Features

Here's a glimpse of what Luna can do:

* **🧠 Natural Language Processing (NLP):** Leverages the power of TensorFlow and scikit-learn for understanding and processing human language.
* **🌐 Flask Web Interface:** Provides a user-friendly web interface built with Flask for seamless interaction.
* **🗣️ Speech Playback:** Utilizes `playsound` and `edge-tts` for clear and natural-sounding voice output.
* **🌍 Translation Support:** Offers multilingual translation capabilities powered by `deep-translator`.
* **🎧 Audio Input/Output:** Handles audio input and output using `PyAudio` and `pygame` for voice commands and sound processing.
* **🎬 YouTube Downloading:** Enables you to download videos from YouTube using the efficient `yt-dlp` library.

## 🛠️ Installation

Follow these steps to get Luna up and running on your system:

### 1. Prerequisites

* **Python:** Ensure you have Python 3.7 or higher installed on your machine.
    * Download the latest version from the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

### 2. Install Dependencies

* **Navigate to the Project Directory:** Open your terminal or command prompt and navigate to the directory where you have saved the Luna project files.
* **Install Requirements:** Execute the following command to install all the necessary Python libraries:

    ```bash
    pip install -r requirements.txt
    ```

    *(Make sure the `requirements.txt` file is present in the current directory.)*

### 3. Running Luna

* **Start the Flask Application:** Run the main Flask application using the following command:

    ```bash
    python app.py
    ```

### 4. Usage

1.  **Launch `app.py`:** Execute the command mentioned in the previous step (`python app.py`). This will start the Flask web server.
2.  **Run `clap.py`:** In a separate terminal or command prompt, run the `clap.py` script:

    ```bash
    python clap.py
    ```

3.  **Interact via Web Browser:** A web interface should automatically launch in your default web browser. Follow the on-screen instructions to interact with Luna.
4.  **Utilize Features:** You can now use various features such as voice commands, text input for NLP tasks, initiate translations, and even download YouTube videos through the web interface.

## 📄 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). Feel free to use and modify the code as per the terms of the license.
