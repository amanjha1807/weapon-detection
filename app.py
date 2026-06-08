from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from ultralytics import YOLO
from PIL import Image
import io
import cv2
import numpy as np
import torch

app = FastAPI()

# Load the best model once globally
BEST_WEIGHTS = '/content/runs/weapon_det/weights/best.pt'
# Use the already loaded infer_model to avoid reloading
# infer_model is expected to be loaded from cell BRb9ODPUE6LP
# If infer_model is not globally available, uncomment the line below:
# infer_model = YOLO(BEST_WEIGHTS)

# Ensure infer_model is available; if not, load it.
# This check is for robustness in case previous cells were not run in order.
if 'infer_model' not in locals() and 'infer_model' not in globals():
    print("Loading YOLO model...")
    infer_model = YOLO(BEST_WEIGHTS)
    print("YOLO model loaded.")


@app.get("/")
async def read_root():
    return {"message": "Weapon Detection API is running! Send an image to /detect_image"}

@app.post("/detect_image/")
async def detect_image(file: UploadFile = File(...)):
    # Read image data
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")
    img_np = np.array(image)

    # Perform inference
    # device is already defined in j3iodJgcUAF0, use it.
    global device
    results = infer_model.predict(
        source=img_np,
        conf=0.40,
        iou=0.50,
        imgsz=IMG_SIZE,
        device=device,
        verbose=False,
    )

    # Draw bounding boxes on the image
    for r in results:
        annotated_image = r.plot() # YOLOv8's plot method draws boxes and labels

    # Convert annotated image (numpy array) back to PIL Image then to bytes
    annotated_image_pil = Image.fromarray(annotated_image)
    byte_arr = io.BytesIO()
    annotated_image_pil.save(byte_arr, format='JPEG')
    byte_arr.seek(0)

    return StreamingResponse(byte_arr, media_type="image/jpeg")

