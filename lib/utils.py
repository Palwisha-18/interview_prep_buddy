import base64
import requests
import whisper 

import streamlit as st
from gtts import gTTS


def setup_whisper_model():
    return whisper.load_model("base")

def generate_interview_questions(topic):
    """Generate interview questions using Ollama"""
    prompt = f"Generate 1 interview question for the topic: {topic}. Provide detailed and relevant questions."
    
    response = requests.post('http://localhost:11434/api/generate',
        json={
            'model': 'mistral',
            'prompt': prompt,
            'stream': False
        }
    )
    
    if response.status_code == 200:
        return response.json()['response']
    return "Error generating question"

def analyze_response(response_text, question):
    """Analyze interview response using Ollama"""
    analysis_prompt = f"""Evaluate the following interview response:
Question: {question}
Response: {response_text}

Please provide feedback on:
1. Content quality and relevance
2. Structure and clarity

Format the feedback in a constructive and encouraging way."""
    
    response = requests.post('http://localhost:11434/api/generate',
        json={
            'model': 'mistral',
            'prompt': analysis_prompt,
            'stream': False
        }
    )
    
    if response.status_code == 200:
        return response.json()['response']
    return "Error analyzing response"

def transcribe_audio(audio_path, whisper_model):
    """Transcribe audio using Whisper"""
    result = whisper_model.transcribe(audio_path)
    return result["text"]


def text_to_speech(text, filename="feedback.mp3"):
    """Convert text to speech using gTTS"""
    try:
        tts = gTTS(text=text, lang='en')
        tts.save(filename)
        return filename
    except Exception as e:
        st.error(f"Error generating speech: {str(e)}")
        return None

def autoplay_audio(file_path):
    """Autoplay audio file in Streamlit"""
    with open(file_path, "rb") as f:
        audio_bytes = f.read()
    audio_base64 = base64.b64encode(audio_bytes).decode()
    audio_tag = f'<audio autoplay="true" src="data:audio/mp3;base64,{audio_base64}">'
    st.markdown(audio_tag, unsafe_allow_html=True)
