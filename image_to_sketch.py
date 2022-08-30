

#Image to Pencil sketch app
import streamlit as st
import numpy as np
from PIL import Image
import cv2
import dodgeV2
import pencil_image
st.set_option('deprecation.showfileUploaderEncoding', False)


#convert into sketch
def app():
    st.title("Convert Image To Pencil Sketch")
    st.set_page_config(page_title="Image to Pencil Sketch",page_icon="👋")
    st.write("This Web App is to help convert your images to realistic Pencil Sketches")
    file_image = st.sidebar.file_uploader("Upload the image", type=['jpeg','jpg','png'])
     if file_image is None:
            st.write("Please Upload the image!!")
      else:
        input_image = Image.open(file_image)
        final_sketch = pencil_image(np.array(input_image))
        st.write("**Your Image**")
        st.image(input_image, use_column_width=True)
        st.write("**Output Pencil Sketch**")
        st.image(final_sketch, use_column_width=True)



