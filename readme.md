🐼 PandaScrib – Lecture Audio Transcriber
PandaScrib is a lightweight, offline tool that converts .m4a, .mp3, or .wav lecture recordings into readable .txt transcripts using OpenAI's Whisper model. It runs entirely offline, requiring no internet connection or API key.
📑 Table of Contents

Folder Structure
Setup Instructions (Windows)
Usage
Supported Formats

📁 Folder Structure
panda_scrib/
│
├── main.py # Core transcription script
├── requirements.txt # List of required Python libraries
├── recordings/ # Directory for input audio files
├── transcripts/ # Directory for output text transcripts
└── venv/ # (Auto-generated) Python virtual environment

🧰 Setup Instructions (Windows)
Follow these steps to set up PandaScrib on your Windows machine:

Install Python

Download and install Python from python.org/downloads.
During installation, ensure you check ✅ "Add Python to PATH".

Set Up the Project

Open a Command Prompt.
Navigate to the project folder:cd path\to\panda_scrib

Create a virtual environment:python -m venv venv

Activate the virtual environment:venv\Scripts\activate

Install required libraries:pip install -r requirements.txt

🎙️ Usage

Add Audio Files

Place your .m4a, .mp3, or .wav lecture recordings in the recordings/ folder.

Run the Transcription

Ensure the virtual environment is activated (see step 2 in Setup Instructions).
Execute the script:python main.py

Transcribed text files will be saved in the transcripts/ folder.

🎵 Supported Formats

.m4a
.mp3
.wav
