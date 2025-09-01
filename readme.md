<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PandaScrib - Lecture Audio Transcriber</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            color: #333;
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        h1 {
            font-size: 2.2em;
        }
        h2 {
            font-size: 1.8em;
            margin-top: 20px;
        }
        h3 {
            font-size: 1.4em;
        }
        code {
            background-color: #f4f4f4;
            padding: 2px 6px;
            border-radius: 4px;
            font-family: 'Courier New', Courier, monospace;
        }
        pre {
            background-color: #f4f4f4;
            padding: 15px;
            border-radius: 6px;
            overflow-x: auto;
        }
        ul, ol {
            margin: 10px 0;
            padding-left: 20px;
        }
        a {
            color: #0066cc;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        .emoji {
            font-size: 1.2em;
            margin-right: 5px;
        }
    </style>
</head>
<body>
    <h1><span class="emoji">🐼</span> PandaScrib – Lecture Audio Transcriber</h1>
    <p>PandaScrib is a lightweight, offline tool that converts <code>.m4a</code>, <code>.mp3</code>, or <code>.wav</code> lecture recordings into readable <code>.txt</code> transcripts using OpenAI's Whisper model. It runs entirely offline, requiring no internet connection or API key.</p>

    <h2>Table of Contents</h2>
    <ul>
        <li><a href="#folder-structure">Folder Structure</a></li>
        <li><a href="#setup-instructions">Setup Instructions (Windows)</a></li>
        <li><a href="#usage">Usage</a></li>
        <li><a href="#supported-formats">Supported Formats</a></li>
    </ul>

    <h2 id="folder-structure"><span class="emoji">📁</span> Folder Structure</h2>
    <pre>

panda_scrib/
│
├── main.py # Core transcription script
├── requirements.txt # List of required Python libraries
├── recordings/ # Directory for input audio files
├── transcripts/ # Directory for output text transcripts
└── venv/ # (Auto-generated) Python virtual environment
</pre>

    <h2 id="setup-instructions"><span class="emoji">🧰</span> Setup Instructions (Windows)</h2>
    <p>Follow these steps to set up PandaScrib on your Windows machine:</p>
    <ol>
        <li>
            <strong>Install Python</strong>
            <ul>
                <li>Download and install Python from <a href="https://www.python.org/downloads/">python.org/downloads</a>.</li>
                <li>During installation, ensure you check ✅ <strong>"Add Python to PATH"</strong>.</li>
            </ul>
        </li>
        <li>
            <strong>Set Up the Project</strong>
            <ul>
                <li>Open a Command Prompt.</li>
                <li>Navigate to the project folder:
                    <pre><code>cd path\to\panda_scrib</code></pre>
                </li>
                <li>Create a virtual environment:
                    <pre><code>python -m venv venv</code></pre>
                </li>
                <li>Activate the virtual environment:
                    <pre><code>venv\Scripts\activate</code></pre>
                </li>
                <li>Install required libraries:
                    <pre><code>pip install -r requirements.txt</code></pre>
                </li>
            </ul>
        </li>
    </ol>

    <h2 id="usage"><span class="emoji">🎙️</span> Usage</h2>
    <ol>
        <li>
            <strong>Add Audio Files</strong>
            <ul>
                <li>Place your <code>.m4a</code>, <code>.mp3</code>, or <code>.wav</code> lecture recordings in the <code>recordings/</code> folder.</li>
            </ul>
        </li>
        <li>
            <strong>Run the Transcription</strong>
            <ul>
                <li>Ensure the virtual environment is activated (see step 2 in Setup Instructions).</li>
                <li>Execute the script:
                    <pre><code>python main.py</code></pre>
                </li>
                <li>Transcribed text files will be saved in the <code>transcripts/</code> folder.</li>
            </ul>
        </li>
    </ol>

    <h2 id="supported-formats"><span class="emoji">🎵</span> Supported Formats</h2>
    <ul>
        <li><code>.m4a</code></li>
        <li><code>.mp3</code></li>
        <li><code>.wav</code></li>
    </ul>

</body>
</html>
