import os
import whisper
import time

# ========== CONFIG ==========
INPUT_DIR = "recordings"
OUTPUT_DIR = "transcripts"
SUPPORTED_FORMATS = (".m4a", ".mp3", ".wav")
MODEL_SIZE = "base"  # Options: tiny, base, small, medium, large
# ============================

def ensure_directories():
    os.makedirs(INPUT_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

def get_audio_files():
    return [f for f in os.listdir(INPUT_DIR) if f.lower().endswith(SUPPORTED_FORMATS)]

def transcribe_file(model, filepath):
    print(f"🔄 Transcribing: {os.path.basename(filepath)} ...")
    try:
        result = model.transcribe(filepath)
        return result["text"]
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def save_transcript(text, filename):
    output_path = os.path.join(OUTPUT_DIR, filename)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"✅ Saved: {output_path}")

def main():
    print("🐼 PandaScrib is starting...\n")
    ensure_directories()
    audio_files = get_audio_files()

    if not audio_files:
        print(f"📂 No audio files found in '{INPUT_DIR}/'. Please add .m4a, .mp3, or .wav files.")
        return

    print(f"📁 Found {len(audio_files)} file(s) in '{INPUT_DIR}/'.\n")
    print(f"🧠 Loading Whisper model: {MODEL_SIZE} (please wait)...\n")
    model = whisper.load_model(MODEL_SIZE)
    print("✅ Model loaded successfully!\n")

    processed = 0
    for idx, audio_file in enumerate(audio_files, 1):
        input_path = os.path.join(INPUT_DIR, audio_file)
        output_name = os.path.splitext(audio_file)[0] + ".txt"
        output_path = os.path.join(OUTPUT_DIR, output_name)

        if os.path.exists(output_path):
            print(f"⚠️  Skipping (already transcribed): {audio_file}")
            continue

        print(f"[{idx}/{len(audio_files)}] 📥 Processing: {audio_file}")
        text = transcribe_file(model, input_path)

        if text:
            save_transcript(text, output_name)
            processed += 1

        time.sleep(0.5)  # Smooth logging, prevent overheating

    print("\n🏁 Done!")
    print(f"📄 Total processed files: {processed}")
    print(f"📁 Transcripts saved in: '{OUTPUT_DIR}/'\n")

if __name__ == "__main__":
    main()
