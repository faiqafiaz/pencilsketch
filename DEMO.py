import streamlit as st
def app():
    st.title('Data Stats')
    video_file = open('myvedio.mp4', 'rb')
    video_bytes = video_file.read()
    vedio=st.video(vedio_bytes)
    return(vedio)
