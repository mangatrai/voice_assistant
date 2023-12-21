from openai import OpenAI
import sounddevice as sd
import numpy as np
from scipy.io import wavfile
import tempfile, os
from dotenv import load_dotenv, find_dotenv
from astrapy.db import AstraDB
from gtts import gTTS
from playsound import playsound

# Load the .env file
if not load_dotenv(find_dotenv(),override=True):
    raise Exception("Couldn't load .env file")

client = OpenAI(
  api_key=os.getenv('OPENAI_API_KEY')
)

class VoiceAssistant:
    """
    This class represents a voice assistant.
    
    Attributes:
        history (list): A list of dictionaries representing the assistant's history.
        
    Methods:
        listen: Records audio from the user and transcribes it.
        think: Generates a response to the user's input.
        speak: Converts text to speech and plays it.
    """
    def __init__(self):
        # Initialize the assistant's history
        self.history = [
                {"role": "system", "content": "You are a helpful assistant. The user is english. Only speak english."}
            ]
        
    def listen(self):
        """
        Records audio from the user and transcribes it.
        """
        print("Listening...")
        # Record the audio
        duration = 3  # Record for 3 seconds
        fs = 44100  # Sample rate

        audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype=np.int16)
        sd.wait()

        # Save the NumPy array to a temporary wav file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_wav_file:
            wavfile.write(temp_wav_file.name, fs, audio)

            # Use the temporary wav file in the OpenAI API
            #transcript = openai.audio.transcriptions.create("whisper-1", temp_wav_file)
            transcript = client.audio.transcriptions.create(
                model="whisper-1", 
                file=temp_wav_file.file
            )

        #print(f"User: {transcript['text']}")
        print(transcript.text)
        return transcript.text

    def think(self, text):
        """
        Generates a response to the user's input.
        """
        # Add the user's input to the assistant's history
        self.history.append({"role": "user", "content": text})
        # Send the conversation to the GPT API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=self.history,
            temperature=0.5
        )
        # Extract the assistant's response from the API response
        message = response.choices[0].message.content
        self.history.append({"role": "system", "content": message})
        print('Assistant: ', message)
        return message
    
    def text_to_speech(self, text, lang='en'):
        tts = gTTS(text=text, lang=lang)
        tts.save("output.mp3")
        playsound("output.mp3")


if __name__ == "__main__":
    assistant = VoiceAssistant()

    while True:
        text = assistant.listen()

        if "goodbye" in text.strip().lower():
            print("Assistant: Goodbye! Have a great day!")
            assistant.text_to_speech("Goodbye! Have a great day!")
            break
        
        response = assistant.think(text)
        assistant.text_to_speech(response)
