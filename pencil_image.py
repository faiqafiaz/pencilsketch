def pencil_image(inp_image):
    image_gray = cv2.cvtColor(inp_image, cv2.COLOR_BGR2GRAY)
    image_invert = cv2.bitwise_not(image_gray)
    image_smoothing = cv2.GaussianBlur(image_invert, (21, 21),sigmaX=0, sigmaY=0)
    final_image = dodgeV2(image_gray, image_smoothing)
    return(final_image)
