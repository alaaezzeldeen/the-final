import streamlit as st
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import tempfile
import os

# Initialize Speech Recognition and Translator
recognizer = sr.Recognizer()
translator = Translator()

# Function to recognize speech
def recognize_speech(language):
    with sr.Microphone() as source:
        st.write("Recording...")
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            st.write("You said:", text)
            translated_text = translate_text(text, language)
            st.write("Translated Text:", translated_text)
            return text, translated_text

        except sr.UnknownValueError:
            st.write("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            st.write(f"Could not request results from Google Speech Recognition service; {e}")
    
    return None, None

# Function to translate text
def translate_text(text, target_language):
    translation = translator.translate(text, dest=target_language)
    return translation.text

# Function to save audio locally
def save_audio(text, language):
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        tts = gTTS(text=text, lang=language)
        tts.save(temp_file.name)
        return temp_file.name

# Streamlit UI
st.title("Voice Recognition and Translation with Audio Playback")

language = st.selectbox("Select target language", ["en", "fr", "es" , "ar"])  # Add more languages as needed

if st.button("Start Recording"):
    original_text, translated_text = recognize_speech(language)
    
    if original_text and translated_text:
        st.write("Translated Text:", translated_text)
        
        # Save translated text to audio file
        audio_file = save_audio(translated_text, language)
        
        # Display audio playback option
        st.audio(audio_file, format='audio/wav', start_time=0)
        
        # Delete temporary audio file after displaying
        os.remove(audio_file)
