
from clarifai.client.model import Model
import numpy as np
import cv2
import matplotlib.pyplot as plt
import discord
import io

def use_gpt(prompt: str):
    # You can set the model using model URL or model ID.
    model_url="https://clarifai.com/openai/chat-completion/models/GPT-4"

    # Model Predict
    model_prediction = Model(url=model_url,pat="8e193e505d494f1b8ded423376f6833b").predict_by_bytes(prompt.encode(), input_type="text")

    return model_prediction.outputs[0].data.text.raw



def use_stable_diffusion(prompt: str):
    input_text = prompt.encode()
    model_url = "https://clarifai.com/stability-ai/stable-diffusion-2/models/stable-diffusion-xl"

    model_prediction = Model(url=model_url, pat="8e193e505d494f1b8ded423376f6833b").predict_by_bytes(
        input_text, input_type="text"
    )

    # Base64 image to numpy array
    im_b = model_prediction.outputs[0].data.image.base64
    image_np = np.frombuffer(im_b, np.uint8)
    img_np = cv2.imdecode(image_np, cv2.IMREAD_COLOR)

    _, img_encoded = cv2.imencode('.png', img_np)
    image_bytes = io.BytesIO(img_encoded.tobytes())
    file = discord.File(image_bytes, filename="image.png")

    return file

def use_dall_e(image_url: str):
    model_url = (
        "https://clarifai.com/salesforce/blip/models/general-english-image-caption-blip"
    )

    model_prediction = Model(url=model_url, pat="8e193e505d494f1b8ded423376f6833b").predict_by_url(
        image_url, input_type="image"
    )
    # print(image_url)
    # print(model_prediction.outputs[0].data.text.raw)
    return model_prediction.outputs[0].data.text.raw
