# Luna - Your Helper

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
[![jQuery](https://img.shields.io/badge/jQuery-%230769AD.svg?style=for-the-badge&logo=jquery&logoColor=white)](https://jquery.com/)

Luna is a computer program that acts like your personal helper. It uses a smart brain built with Python, Flask, and TensorFlow, and a website you can easily use with HTML, CSS, and JavaScript (including jQuery to make it more interactive). This setup lets Luna understand what you say and have a conversation with you right in your web browser.

## ✨ What Luna Can Do

Luna has many helpful features that use both its smart brain and the website:

  * **🗣️ Talking to Luna with Your Voice:**
      * You can speak to Luna using your computer's microphone.
      * Luna can talk back to you in a natural-sounding voice.
      * The website will show you if Luna is "Listening..." or "Speaking...".
 
  * **🧠 Luna's Smart Brain:**
      * The Python part of Luna uses Flask to understand what you type or say.
      * It uses TensorFlow and a special model (managed by `app.py`) to understand your language and create responses.
      * Luna can answer general questions and do specific things you ask.
  * **⏰ Remembering Things for You (Reminders):**
      * You can tell Luna to remind you of things using simple language (for example, "remind me to call mom in 10 minutes").
      * The `app.py` part of Luna will remember and tell you when it's time.
      * The website will show your reminders in a special "Reminder" area and also make a sound.
  * **🎶 Playing Music You Have (Local Music + Youtube):**
      * The `app.py` part of Luna can play music files (like MP3s) that are on your computer when you ask (for example, "play some music").
      * Basic controls like play, pause, and stop are handled by Luna's brain.
      * *(Note: You can't directly control the music on the website right now, you need to use voice commands.)*
  * **🔎 Searching the Web and YouTube:**
      * Luna's brain (`app.py`) can understand when you want to search on Google or YouTube and open those searches in your browser.
  * **▶️ Playing YouTube Videos Directly:**
      * Luna's brain (`app.py`) can find the first video on YouTube that matches your search and play it in your browser.
  * **📝 Keeping Track of Your Conversations:**
      * The `app.py` part of Luna saves everything you say and what Luna replies in a file called `conversation_log.txt`.
  * **✨ Easy-to-Use Website:**
      * The website looks clean and modern, using HTML for structure and CSS for styling.
      * It uses "Open Sans" and "Poppins" fonts which are easy to read and look nice.
      * The chat area scrolls so you can see your past conversations.
      * Luna's replies look like they are being typed out to make it more interesting.
  * **🚀 Making the Website Dynamic with jQuery:**
      * Luna uses a tool called jQuery to talk to its brain in the background without reloading the whole page when you send a message or get a reply.
      * jQuery also helps update the chat area with new messages and check for new reminders to show you.

## 🚀 Getting Started - Easy Steps

Here's how to get Luna working on your computer:

### Step 1: Make Sure You Have the Right Python

1.  **Check Your Python Version:**
      * Open a terminal or command prompt (a black window where you type commands).
      * Type `python --version` and press Enter, OR type `python3 --version` and press Enter.
      * You need to see a version number that starts with 3.7 or higher.
2.  **Install Python if Needed:**
      * If your Python version is too old or if you don't have Python, go to this website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
      * Download the latest version and follow the instructions to install it on your computer.

### Step 2: Get the Luna Files

1.  **Download Luna:** Get the files for the Luna project. This might be a ZIP file you download or a folder you get from a service like Git.
2.  **Go to the Luna Folder:** Open your terminal or command prompt again. Use the `cd` command to go into the main Luna folder where you see a file named `requirements.txt`. For example, if the folder is on your Desktop and named "luna-project", you would type `cd Desktop/luna-project` and press Enter.

### Step 3: Install the Necessary Tools

1.  **Install Packages:** In the same terminal where you are in the Luna folder, type this command and press Enter:
    ```bash
    pip install -r requirements.txt
    ```
    This command will automatically download and install all the extra programs that Luna needs to work, like Flask and TensorFlow. Make sure your internet is working during this step.

### Step 4: Start Luna's Brain (`app.py`)

1.  **Run Luna:** In the same terminal, type this command and press Enter:
    ```bash
    python app.py
    ```
    This will start the Flask server, which is the main part of Luna's brain. You should see some text in the terminal that says the server is running (it will usually say something like `http://127.0.0.1:5000/`).

### Step 5: Talk to Luna

1.  **Open the Server OR run clap.py:** Open your web browser (like Chrome, Firefox, or Safari) and go to the address you saw in the terminal (usually `http://127.0.0.1:5000/`). You should see Luna's website OR simply run clap.py

2.  **See Luna's Replies:** Luna's answers will appear on the website. You might also hear Luna speak for some actions.
3.  **Try Different Things:** Try out the features like setting reminders, playing music, searching the web, and asking questions.

## 💡 How to Talk to Luna

Once the website is open in your browser:

1.  **Using Your Voice:** If your browser lets you and you give permission for the website to use your microphone, Luna will start listening. Just speak your commands or questions. The website will show "Listening..." when Luna is trying to hear you and "Speaking..." when Luna is talking back.

3.  **Seeing the Replies:** Luna's text answers will show up in the chat area, and it will look like Luna is typing. If Luna is set up to speak, you will also hear the answer.
4.  **Setting Reminders:** Say or type something like "remind me to check email in 20 minutes". The reminder will appear in the "Reminder" section when the time comes.
5.  **Playing Music:** Try saying or typing "play some music" (this assumes you have music files set up for Luna to play).
6.  **Searching the Web and YouTube:** Say or type "search Google for funny videos" or "search YouTube for cooking recipes".
7.  **Playing YouTube Videos:** Try saying or typing "play relaxing music on YouTube".

### Examples of What to Say or Type:

  * **To set a reminder:** "remind me to take a break in 15 minutes"
  * **To play local music:** "play some music"
  * **To search Google:** "Open Google and search for the weather today"
  * **To search YouTube:** "Open Youtube and search for, see you again meow meow version"
  * **To play a YouTube video:** "play Jaane na Dunga Kahin on YouTube"

### Step 6: Stopping Luna

To stop Luna from running, go back to the terminal where you typed `python app.py` and press the keys `Ctrl` and `C` at the same time. This will stop the Flask server.

## 📜 License

This project is free to use, change, and share under the [MIT License](https://opensource.org/licenses/MIT). This means you can do a lot with the code as long as you give credit to the original creators and include the license information.
