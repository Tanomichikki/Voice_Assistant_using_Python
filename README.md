# Python Voice Assistant

A simple and interactive voice assistant built using Python. This assistant can perform a variety of tasks such as setting reminders, checking the weather, playing music, answering questions, and more. It is built using libraries such as `speech_recognition`, `pyttsx3`, and `wikipedia`.

## Features

- **Speech Recognition**: Convert spoken language into text using the `speech_recognition` library.
- **Text-to-Speech**: The assistant can speak responses using `pyttsx3`.
- **Wikipedia Search**: Search Wikipedia and provide brief information about topics.
- **Weather Forecast**: Get real-time weather updates using an API.
- **Task Management**: Set reminders or notes.
- **Music Control**: Play songs from a local collection or an online music service.

## Requirements

Make sure you have the following dependencies installed:

- Python 3.6 or above
- `speech_recognition`
- `pyttsx3`
- `wikipedia`
- `requests`
- `pyaudio` (optional, for microphone support)
- `datetime`
- `os`

You can install these libraries using `pip`:

```bash
pip install speechrecognition pyttsx3 wikipedia requests pyaudio

```


## How It Works
- The assistant listens to your command using the microphone.
- It processes the command using speech_recognition and converts it to text.
- The assistant processes the text command and returns a response (spoken out loud or displayed on the screen).
- The assistant can interact with web APIs (for example, Wikipedia or weather services) and local services (e.g., playing music, reminders).

## Commands
Here are a few example commands you can give to the assistant:
- "What's the weather like today?"
- "Tell me about [topic]."
- "Play music."
- "Set a reminder for 3 PM."
- "What time is it?"
- "Open Instagram."


## Acknowledgements
- Thanks to the developers of speech_recognition, pyttsx3, and wikipedia for their amazing libraries.
- Inspiration for this project comes from various voice assistant projects across the web.


## "The best way to predict the future is to invent it." - Alan Kay
