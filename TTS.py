from gtts import gTTS
import os

def text_to_speech(text, lang='en', slow=False, pitch=1.0, 
                   rate=1.0, volume=1.0, filename="speech.mp3"):
    tts = gTTS(text=text, lang=lang, slow=slow)
    
    # Adjust voice pitch
    tts.pitch = pitch
    
    # Adjust speaking rate
    tts.rate = rate
    
    # Adjust volume
    tts.volume = volume

    # Save the synthesized speech to the specified filename
    tts.save(filename)

    # Play the synthesized speech using the default media player
    os.system(f"start {filename}")

# Example usage:
if __name__ == "__main__":
    text_to_speech("Dictionary Entries Analysis (DEA). What is DEA?",
                   lang='en', slow=False, pitch=0.8, rate=1.5, volume=0.8)