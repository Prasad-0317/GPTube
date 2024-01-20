import streamlit as st

from gptube import generate_answer, generate_summary, video_info, is_valid_openai_key, is_valid_youtube_url, get_video_duration, calculate_api_cost
from elevenlabs import generate, set_api_key

st.set_page_config(page_title="GPTube", page_icon='🎬')

set_api_key(st.secrets["ELEVENLABS_API_KEY"])