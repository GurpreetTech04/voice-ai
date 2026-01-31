import streamlit as st
import os
from audio_text import transcribe_audio_with_groq
# from rag_system import rag_system

audio =  st.audio_input("Speek",  sample_rate=16000, width="stretch")

if audio:
    audio_bytes = audio.read()
    text, error = transcribe_audio_with_groq(audio_bytes)
    
    if text:
        st.markdown("**Transcription:**")
        st.write(text)
    else:
        st.error(f"Transcription Error: {error}")
