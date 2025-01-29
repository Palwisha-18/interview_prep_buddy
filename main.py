import streamlit as st
from audio_recorder_streamlit import audio_recorder

from lib.utils import *


def main():
    st.sidebar.title("API_KEY_CONFIGURATION")
    api_key = st.sidebar.text_input("Enter your Open API Key", type="password")

    st.title("Interview Prep Buddy")
    st.write("Hi there! I am here to help you with preparing for your interview. Add your OPEN API KEY to start!")

    if api_key:
        client = setup_openai_client(api_key=api_key)
        
        topic = st.text_input("Enter the role for which you are trying to prepare interview:")
        if topic:
            st.write(f"Generating interview question for: {topic}")
            questions = generate_interview_questions(client, topic)
            st.subheader("Interview Question:")
            st.write(questions)

            recorded_audio = audio_recorder()
            if recorded_audio:
                audio_file = "audio.mp3"
                with open(audio_file, "wb") as f:
                    f.write(recorded_audio)

                transcribed_text = transcribe_audio(client=client, audio_path=audio_file)
                st.subheader("Interviewee Response")
                st.write(transcribed_text)

                feedback_response = analyze_response(client, transcribed_text, questions)
                with st.status("Analyzing your response..."):
                    response_audio_file = "audio_response.mp3"
                    text_to_audio(client=client, text=feedback_response, audio_path=response_audio_file)

                auto_play_audio(response_audio_file)
                st.subheader("Buddy Feedback")
                st.write(feedback_response)
                


if __name__ == "__main__":
    main()
