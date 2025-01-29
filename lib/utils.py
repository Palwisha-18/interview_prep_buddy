import openai
import base64
import streamlit as st
from audio_recorder_streamlit import audio_recorder


def setup_openai_client(api_key):
    return openai.OpenAI(api_key=api_key)

# Convert Speech to Text
def transcribe_audio(client, audio_path):
    with open(audio_path, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(model="whisper-1", file=audio_file)
        return transcript.text
    
# Convert Text to Speech
def text_to_audio(client, text, audio_path):
    response = client.audio.speech.create(
        model="tts-1",
        voice="echo",
        input=text,
    )
    return response.stream_to_file(audio_path)

# Generate Interview Question based on topic
def generate_interview_questions(client, topic):
    prompt = f"Generate 1 interview question for the topic: {topic}. Provide detailed and relevant questions."
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[{"role": "system", "content": "You are a helpful interview assistant."},
                  {"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# Generate Feedback for User Response to Question
def analyze_response(client, response, question):
    feedback_prompt = f"Evaluate the following response to the question '{question}':\nResponse: {response}\nProvide constructive feedback."
    feedback = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[{"role": "system", "content": "You are a constructive and helpful evaluator."},
                  {"role": "user", "content": feedback_prompt}]
    )
    return feedback.choices[0].message.content

# Enable Auto Play Audio 
def auto_play_audio(audio_file):
    with open(audio_file, "rb") as audio_file:
        audio_bytes = audio_file.read()
    base64_audio = base64.b64encode(audio_bytes).decode("utf-8")
    audio_html = f'<audio src="data:audio/mp3;base64,{base64_audio}" controls autoplay>'
    st.markdown(audio_html, unsafe_allow_html=True)
