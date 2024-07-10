# Translation Applications

This repository contains two applications built with Streamlit:

1. **Text Translation App**: Translates text into a selected language.
2. **Voice Translation App**: Takes voice input, translates it to the selected language, and outputs the result in both text and audio.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Text Translation App](#text-translation-app)
  - [Voice Translation App](#voice-translation-app)
- [Features](#features)
- [Technologies](#technologies)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Malkyounis71/Voice-Recognition-and-Translation.git
   cd translation-apps
   
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt


## Usage
### Text Translation App

1. Navigate to the text translation app directory:
   ```bash
   cd app
   
2. Run the Streamlit app:
   ```bash
   streamlit run app.py

3. Open your browser and go to " http://localhost:8501 " to use the app.

### Voice Translation App
 1. Navigate to the voice translation app directory:
    ```bash
    cd app2

2. Run the Streamlit app:
     ```bash
   streamlit run app2.py

3. Open your browser and go to " http://localhost:8501 " to use the app.


## Features

### Text Translation App

- Input text in the source language.
- Select the target language.
- Translates and displays the text in the target language.

### Voice Translation App

- Record voice input.
- Select the target language.
- Translates and displays the text in the target language.
- Converts and plays the translated text as audio.

## Technologies

- **Python**: Programming language used.
- **Streamlit**: Framework for building the apps.
- **Google Cloud Translation API**: For text translation.
- **SpeechRecognition**: For capturing voice input.
- **gTTS (Google Text-to-Speech)**: For converting text to audio.

## Contributing

Contributions are welcome! Please fork this repository and submit pull requests for any improvements.


   
   

    
   
   
   
      
