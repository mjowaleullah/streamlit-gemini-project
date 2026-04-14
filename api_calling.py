from google import genai
from dotenv import load_dotenv
import os
from gtts import gTTS
import io
load_dotenv()

api = os.environ.get("GEMINI_API_KEY")

clinet = genai.Client(api_key=api)

# Note Generator

def note_generate(image):
    
    prompt = """Summarize the Picture in note formate at max 100 words,
    make sure to add necessary markdown to differentiate different section"""

    response = clinet.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[image, prompt]
    )

    return response.text

def audio_transcription(text):
    speech = gTTS(text,lang="en", slow=False)
    audio_buffer = io.BytesIO()
    speech.write_to_fp(audio_buffer)
    return audio_buffer

def quiz_generate(image, deficulty):
    prompt = f"Generate 3 Quizzes based on the {deficulty}. Make sure to add markdown to diffrentiat the option. and give the right answer at the last point on this quizzes."

    response = clinet.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[image, prompt]
    )

    return response.text




