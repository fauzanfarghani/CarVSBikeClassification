import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

def app():
    # Load the trained model
    model = load_model('car_bike_classifier.h5')

    # Function to preprocess the uploaded image
    def preprocess_image(img):
        img = img.resize((224, 224))  # Resize the image to match model's input shape
        img_array = image.img_to_array(img)  # Convert the image to an array
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
        img_array /= 255.0  # Normalize the image
        return img_array

    # Streamlit application
    st.title("Car vs Bike Classification")
    st.write("Upload an image of a car or a bike to see the model's prediction.")

    # File uploader for image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        img = image.load_img(uploaded_file)
        st.image(img, use_column_width=True)
        
        # Preprocess the image
        img_array = preprocess_image(img)
        
        # Make prediction
        prediction = model.predict(img_array)
        class_label = "Car" if prediction[0][0] > 0.5 else "Bike"
        
        # Display the prediction
        st.write(f"Prediction: {class_label}")