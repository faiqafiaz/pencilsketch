import streamlit as st
from multiapp import MultiApp
import image_to_sketch, DEMO

app = MultiApp()

# Add all your application here
app.add_app("Home", image_to_sketch.app)
app.add_app("Demo", DEMO.app)

# The main app
app.run()
