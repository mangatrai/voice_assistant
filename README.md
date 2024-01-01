# Voice Assistant
Astra Voice Assistnat is a simple voice assistant developed using Python. It uses OpenAI's GPT-3 API for language understanding and response generation, SoundDevice for recording audio, and gtts/playsound for text-to-speech conversion.

## Features
- **Voice Recognition**: Listens to user's voice commands and transcribes them to text.
- **AI Conversation**: Communicates with users in natural language using OpenAI's GPT-3 model.
- **Text-to-Speech**: Converts the assistant's text responses into voice and speaks them out.

## Requirements
To run this application, you will need:  

Python 3.10. (I tested with this version)
streamlit
openai
astrapy
numpy
sounddevice
scripy
gTTS
playsound
langchain
tiktoken
pypdf
pandas
langchain

## Usage
You can start the assistant by running the app.py script. It uses Streamlit to render the UI:

```
streamlit run app.py
```

The assistant will start listening for your commands. You can speak your commands, and the assistant will respond. 

To stop the assistant, say "goodbye".

## Demo Video
Go to assets/video1854402426.mp4 and watch video

## Contribution
Feel free to fork this project, make some changes, and submit a pull request. All contributions are welcome!

## Disclaimer
Remember to keep your OpenAI API keys secret and secure, and never expose them in your code or version control system.
