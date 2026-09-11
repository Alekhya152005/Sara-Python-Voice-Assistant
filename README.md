# Sara - Python Voice Assistant

Sara is a simple Python-based voice assistant that listens to voice commands, understands them using speech recognition, and responds using text-to-speech.

## Features

* Voice-based interaction
* Speech recognition
* Text-to-speech responses
* Play YouTube videos or songs
* Tell the current time
* Tell the current date
* Open Google
* Basic greetings and conversations
* Voice command to exit the assistant

## Technologies Used

* Python
* SpeechRecognition
* Pyttsx3
* PyWhatKit
* Web Browser
* DateTime

## How It Works

1. Sara listens to the user's voice through the microphone.
2. Speech Recognition converts the voice into text.
3. Sara checks the recognized question.
4. Based on the command, Sara performs the required action.
5. Sara responds using text-to-speech.

## Project Structure

Sara-Python-Voice-Assistant/
│
├── Sara_assistant.py
├── requirements.txt
└── README.md

## Voice Commands

| Voice Command            | Action                    |
| ------------------------ | ------------------------- |
| Sara, hi                 | Gives a greeting          |
| Sara, what are you doing | Gives a response          |
| Sara, how are you        | Gives a response          |
| Sara, good morning       | Gives a morning greeting  |
| Sara, good evening       | Gives an evening greeting |
| Sara, good night         | Gives a night greeting    |
| Sara, play [song name]   | Plays a song on YouTube   |
| Sara, what is the time   | Tells the current time    |
| Sara, what is the date   | Tells the current date    |
| Sara, open Google        | Opens Google              |
| Sara, bye                | Stops the assistant       |

## Installation

### 1. Clone the Repository

git clone https://github.com/Alekhya152005/Sara-Python-Voice-Assistant.git

### 2. Open the Project

cd Sara-Python-Voice-Assistant

### 3. Install the Required Libraries

pip install -r requirements.txt

### 4. Run the Project

python Sara_assistant.py

## Requirements

The project uses the following Python libraries:

SpeechRecognition
pyttsx3
pywhatkit
PyAudio

## Future Improvements

* Add weather information
* Add Wikipedia search
* Add more voice commands
* Add application opening commands
* Improve conversation handling

## Author

Gummalla Alekya

B.Tech Computer Science Engineering Student
Cloud & DevOps Enthusiast

