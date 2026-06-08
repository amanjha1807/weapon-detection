

import streamlit as st
import requests
from PIL import Image
import io

st.title("Weapon Detection App")
st.write("Upload an image to detect weapons (knives, guns) using a YOLOv8 model.")

# IMPORTANT: Replace with your actual ngrok public URL from the FastAPI output
# It should look something like: 'https://xxxxxxxxxxxx.ngrok-free.app/detect_image/'
FASTAPI_ENDPOINT = "YOUR_NGROK_URL_HERE/detect_image/"

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    st.write("")

    # Prepare image for sending to FastAPI
    image_bytes = uploaded_file.getvalue()
    files = {'file': (uploaded_file.name, image_bytes, uploaded_file.type)}

    st.write("Detecting weapons...")
    
    try:
        # Make POST request to FastAPI
        response = requests.post(FASTAPI_ENDPOINT, files=files, timeout=60) # Increased timeout

        if response.status_code == 200:
            # Read the detected image from the response
            detected_image = Image.open(io.BytesIO(response.content))
            st.image(detected_image, caption="Detected Weapons", use_column_width=True)
            st.success("Detection complete!")
        else:
            st.error(f"Error from FastAPI: {response.status_code} - {response.text}")
    except requests.exceptions.ConnectionError:
        st.error("Connection Error: Could not connect to the FastAPI server. Please ensure the FastAPI cell is running and the NGROK_AUTH_TOKEN is correct and accessible.")
    except requests.exceptions.Timeout:
        st.error("Timeout Error: The request to the FastAPI server took too long. The model might be slow or the image is too large.")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
