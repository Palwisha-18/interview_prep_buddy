# Interview Prep Buddy 🎯

Interview Prep Buddy is an AI-powered interview preparation tool that helps candidates practice and improve their interview skills through real-time feedback on their responses.

## Current Features ✨

- **Speech-to-Text Conversion**: Transcribes your responses for detailed analysis
- **AI-Powered Feedback**: Provides comprehensive feedback on:
  - Response content and relevance
  - Answer structure
  - Overall delivery
- **Text-to-Speech Feedback**: Delivers feedback in audio format for easy consumption
- **Topic-based Questions**: Generates relevant interview questions based on your chosen topic
- **Interactive UI**: User-friendly interface built with Streamlit

## Prerequisites 🔧

Before running the application, ensure you have:
- Python 3.7 or higher installed
- An OpenAI API key
- A microphone for audio recording

## Installation 📦

1. Clone the repository:
```bash
git clone https://github.com/Palwisha-18/interview_prep_buddy.git
cd interview_prep_buddy
```

2. Create and activate a virtual environment:
```bash
python -m venv interview_env
# On Windows
interview_env\Scripts\activate
# On macOS/Linux
source interview_env/bin/activate
```

3. Install the required dependencies:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## Usage 🚀

1. Start the application:
```bash
streamlit run main.py
```

2. Enter your OpenAI API key in the sidebar

3. Use the application:
   - Enter an interview topic
   - Click the microphone icon to record your response
   - Stop the recording when finished
   - Review the AI-generated feedback on your performance
   - Listen to the audio feedback
