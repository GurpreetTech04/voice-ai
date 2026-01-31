import streamlit as st
import os
from audio_text import transcribe_audio_with_groq
# from rag_system import rag_system
import pyttsx3
engine = pyttsx3.init() # object creation

audio =  st.audio_input("Speek",  sample_rate=16000, width="stretch")

def speak(text):
    
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    

if audio:
    audio_bytes = audio.read()
    text, error = transcribe_audio_with_groq(audio_bytes)
    
    if text:
        st.markdown("**Transcription:**")
        st.write(text)
        speak(text)
    else:
        
        st.error(f"Transcription Error: {error}")
