import streamlit as st
video_file = open('myvedio.mp4', 'rb')
video_bytes = video_file.read()

st.video(vedio_bytes)