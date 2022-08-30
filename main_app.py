import streamlit as st
from multiapp import MultiApp
import DEMO, image_to_sketch
app = MultiApp()

# Add all your application here
app.add_app("Home", image_to_sketch.app)
app.add_app("Demo", DEMO.app)

# The main app
#app.run()
