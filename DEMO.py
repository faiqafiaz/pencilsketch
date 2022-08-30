import streamlit as st
def app():
    st.title('Demo')
    video_file = open('myvedio.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
