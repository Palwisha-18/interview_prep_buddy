# Interview Prep Buddy 🎯

Interview Prep Buddy is an AI-powered interview preparation tool that helps candidates practice and improve their interview skills through real-time feedback on their responses. It uses local AI models for processing, making it free to use and privacy-focused.

## Current Features ✨

- **Speech-to-Text Conversion**: Transcribes your responses using Whisper for detailed analysis
- **AI-Powered Feedback**: Provides comprehensive feedback using Ollama on:
  - Response content and relevance
  - Answer structure
  - Overall delivery
- **Text-to-Speech Feedback**: Delivers feedback in audio format using gTTS
- **Role-based Questions**: Generates relevant interview questions based on your target role
- **Interactive UI**: User-friendly interface built with Streamlit
- **Local Processing**: All AI operations run locally on your machine

## Prerequisites 🔧

Before running the application, ensure you have:
- Python 3.7 or higher installed
- Ollama installed on your system
- A microphone for audio recording
- Sufficient system resources to run local AI models

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

3. Install Ollama:
```bash
# For macOS or Linux
curl -fsSL https://ollama.com/install.sh | sh

# For Windows
# Download from https://ollama.com/download
```

4. Pull the required Ollama model:
```bash
ollama pull mistral
```

5. Install the required Python dependencies:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## Usage 🚀

1. Start Ollama service (should be running in background)

2. Start the application:
```bash
streamlit run main.py
```

3. Use the application:
   - Enter the role you're preparing for
   - Wait for the question to be generated
   - Click the microphone icon to record your response
   - Stop the recording when finished
   - Review your transcribed response
   - Read and listen to the AI-generated feedback
   - Optionally download the feedback audio
