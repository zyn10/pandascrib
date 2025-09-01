# 🐼 PandaScrib – Lecture Audio Transcriber

PandaScrib is a simple, offline tool to convert `.m4a` or `.mp3` lecture recordings into readable `.txt` transcripts using OpenAI's Whisper model. Works fully offline — no internet or API key required.

---

## 📁 Folder Structure

panda_scrib/
│
├── main.py # Transcription script
├── requirements.txt # Required Python libraries
├── recordings/ # Put your audio files here
├── transcripts/ # Transcribed text files will be saved here
└── venv/ # (auto-generated) Python virtual environment

---

## 🧰 Setup Instructions (Windows)

1. **Install Python**
   - Download & install from [https://www.python.org/downloads/](https://www.python.org/downloads/)
   - During installation, make sure to check ✅ **"Add Python to PATH"**

---

2. **Open Command Prompt**

   Navigate to the project folder:

   ```bash
   cd path\to\panda_scrib
   ```

Create a virtual environment

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

Add your lecture recordings

Place .m4a, .mp3, or .wav files into the recordings/ folder.

python main.py
