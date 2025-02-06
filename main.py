import requests
import tempfile
import os

import streamlit as st
from audio_recorder_streamlit import audio_recorder
from lib.utils import *

def main():
    st.title("Interview Prep Buddy")
    st.write("Practice your interview skills with AI-powered feedback!")

    if "whisper_model" not in st.session_state:
        try:
            st.session_state.whisper_model = setup_whisper_model()
            st.success("Speech recognition model loaded successfully!")
        except Exception as e:
            st.error(f"Error loading speech recognition model: {str(e)}")
            return

    if "ollama_connected" not in st.session_state:
        try:
            requests.get('http://localhost:11434/api/tags')
            st.session_state.ollama_connected = True
            st.success("Successfully connected to Ollama!")
        except:
            st.session_state.ollama_connected = False
            st.error("""
            Unable to connect to Ollama. Please ensure:
            1. Ollama is installed
            2. Ollama service is running
            3. You have pulled the required model (e.g., 'ollama pull mistral')
            """)
            return

    role = st.text_input("Enter the role you are preparing interview for:")

    if role and "questions" not in st.session_state:
        st.session_state.questions = generate_interview_questions(role)

    if "questions" in st.session_state:
        st.write("**Interview Question:**")
        st.write(st.session_state.questions)

        recorded_audio = audio_recorder()

        if recorded_audio:
            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as audio_file:
                audio_file.write(recorded_audio)
                audio_path = audio_file.name

            st.write("**Transcribing your response...**")
            transcribed_text = transcribe_audio(audio_path, st.session_state.whisper_model)
            st.session_state.transcribed_text = transcribed_text 

            st.subheader("Your Response:")
            st.write(transcribed_text)

            st.write("**Analyzing your response...**")
            feedback = analyze_response(transcribed_text, st.session_state.questions)
            st.session_state.feedback = feedback 

            st.subheader('Buddy Feedback:')
            st.write(feedback)

            st.write("**Listen to the feedback:**")
            feedback_audio = text_to_speech(feedback)
            if feedback_audio:
                autoplay_audio(feedback_audio)
                with open(feedback_audio, "rb") as file:
                    btn = st.download_button(
                        label="Download Feedback Audio",
                        data=file,
                        file_name="interview_feedback.mp3",
                        mime="audio/mp3"
                    )
                try:
                    os.remove(feedback_audio)
                except:
                    pass

if __name__ == "__main__":
    main()
