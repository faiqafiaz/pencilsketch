import streamlit as st
from multiapp import MultiApp
import image_to_sketch, DEMO

app = MultiApp()

# Add all your application here
app.add_app("Home", image_to_sketch.app)
app.add_app("Demo", DEMO.app)
st.write("This Web App is to help convert your images to realistic Pencil Sketches")

# The main app
app.run()
