import streamlit as st
from googletrans import Translator

# Streamlit UI
st.title('Text Translator')

# Input text box
input_text = st.text_area("Enter text to translate", "")

# Select language to translate to
languages = ['es', 'fr', 'de', 'ar', 'en']  # Language codes: Spanish, French, German, Arabic, English
target_language = st.selectbox('Select Language', languages)

# Translate function using Google Translate API
def translate_text(text, target_lang):
    translator = Translator()
    translation = translator.translate(text, dest=target_lang)
    return translation.text

# Translate button
if st.button('Translate'):
    if input_text:
        translated_text = translate_text(input_text, target_language)
        st.success(f'Translated text ({target_language}): {translated_text}')
    else:
        st.warning("Please enter some text to translate.")
