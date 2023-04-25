import streamlit as st
import pandas as pd
import requests
import io
from PIL import Image
import json



API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
headers = {"Authorization": "Bearer xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}


def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content
    

def main():
    st.title('Text to Image Genration')
    in_put=st.text_input("*Enter your text to genrate the Image*")

    if st.button("Genrate the Image"):
        payload=({
	"inputs": in_put,
})
        
        image_bytes = query(payload)
        i_mage = Image.open(io.BytesIO(image_bytes))
        st.image(i_mage)
    
    
if __name__=='__main__':
    main()      