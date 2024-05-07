import os

from dotenv import load_dotenv

load_dotenv()
EDEN_SECRET_KEY=os.getenv("EDEN_AI_API_KEY")
import base64
from io import BytesIO

from langchain_community.llms import EdenAI
from PIL import Image


def print_base64_image(base64_string):
    # Decode the based string into binary data 
    decoded_data=base64.b64decode(base64_string)
    # Create an in-memory string to read the binary data 
    image_stream = BytesIO(decoded_data)
    # Open the image using PIL 
    image = Image.open(image_stream)
    # Display the image 
    image.show() 
text2image=EdenAI(edenai_api_key=EDEN_SECRET_KEY, feature="image", provider="openai", resolution="512x512")
image_output = text2image.invoke('A dog riding a motorcycle')
print_base64_image(image_output)