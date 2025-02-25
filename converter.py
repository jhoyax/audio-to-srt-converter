import os
import whisper

# Configuration
AUDIO_FILE = "assets/audio.mp3"  # Input audio file
CAPTIONS_FILE = "assets/captions.srt"  # Captions file

# Step 1: Transcribe Audio to Generate Captions
def transcribe_audio(audio_file):
    print("Transcribing audio...")
    model = whisper.load_model("base")  # Load the Whisper model
    result = model.transcribe(audio_file)

    # Create an SRT file for segment-based captions
    with open(CAPTIONS_FILE, "w", encoding="utf-8") as srt_file:
        for index, segment in enumerate(result["segments"], start=1):
            start_time = format_timestamp(segment["start"])
            end_time = format_timestamp(segment["end"])
            text = segment["text"]
            
            srt_file.write(f"{index}\n{start_time} --> {end_time}\n{text}\n\n")
    
    print(f"Captions saved to {CAPTIONS_FILE}")
    return CAPTIONS_FILE

# Helper: Format timestamp for SRT
def format_timestamp(seconds):
    millis = int((seconds % 1) * 1000)
    seconds = int(seconds)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02},{millis:03}"

# Main Function
def main():
    if not os.path.exists(AUDIO_FILE):
        print(f"Audio file '{AUDIO_FILE}' not found!")
        return
    
    # Transcribe the audio and generate captions
    transcribe_audio(AUDIO_FILE)

    print("Process complete!")

if __name__ == "__main__":
    main()
