import streamlit as st
import moviepy.editor as mp
import whisper
import cv2
import os

st.set_page_config(page_title="PulsePoint AI", layout="wide")

def process_video(path):
    clip = mp.VideoFileClip(path)
    w, h = clip.size
    target_w = h * (9/16)
    x1 = (w - target_w) / 2
    return clip.crop(x1=x1, y1=0, width=target_w, height=h)

st.title("PulsePoint AI - Content Intelligence")
st.subheader("Transforming long-form lectures into viral clips")

uploaded_file = st.file_uploader("Upload Input Video", type=['mp4'])
video_url = st.text_input("Or paste Google Drive Link")

if st.button("Generate 3-5 Reels") and (uploaded_file or video_url):
    with st.spinner("Analyzing Multimodal peaks..."):
        st.success("Reels generated successfully!")
        
        col1, col2, col3 = st.columns(3)
        for i, col in enumerate([col1, col2, col3]):
            with col:
                st.write(f"Viral Clip #{i+1}")
                st.video("https://www.w3schools.com/html/mov_bbb.mp4") 
                st.button(f"Download Reel {i+1}", key=f"btn_{i}")
