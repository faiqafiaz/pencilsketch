

#Image to Pencil sketch app
import streamlit as st
import numpy as np
from PIL import Image
import cv2
st.set_option('deprecation.showfileUploaderEncoding', False)
def dodgeV2(x, y):
    return cv2.divide(x, 255 - y, scale=256)

def pencilsketch(inp_img):
    img_gray = cv2.cvtColor(inp_img, cv2.COLOR_BGR2GRAY)
    img_invert = cv2.bitwise_not(img_gray)
    img_smoothing = cv2.GaussianBlur(img_invert, (21, 21),sigmaX=0, sigmaY=0)
    final_img = dodgeV2(img_gray, img_smoothing)
    return(final_img)
#image = Image.open('sir.jpeg')
#st.image(image, width=30, use_column_width="auto", output_format="auto")
#image1 = Image.open('pencil.jpeg')
#st.image(image1, width=50, use_column_width="auto", output_format="auto")
st.title("Convert Image To Pencil Sketch")
st.write("This Web App is to help convert your images to realistic Pencil Sketches")
st.markdown("*Demo*")
file_image = st.sidebar.file_uploader("Upload the image", type=['jpeg','jpg','png'])
if file_image is None:
    st.write("Please Upload the image!!")
else:
    input_img = Image.open(file_image)
    final_sketch = pencilsketch(np.array(input_img))
    st.write("**Your Image**")
    st.image(input_img, use_column_width=True)
    st.write("**Output Pencil Sketch**")
    st.image(final_sketch, use_column_width=True)


# In[ ]:




