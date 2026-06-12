<img width="528" height="790" alt="demo4" src="https://github.com/user-attachments/assets/304ecb38-d203-455e-af8a-899233acefa8" /># 🔪 Weapon Detection System using YOLOv8

![Weapon Detection Demo](.png)

## 📌 Overview

A real-time Weapon Detection System built using **YOLOv8** and **PyTorch** to identify weapons such as guns and knives in surveillance footage and images.

The system detects:

* 🔫 Guns
* 🔪 Knives
* 👤 Persons

The project includes dataset preprocessing, model training, evaluation, FastAPI deployment, and a Streamlit-based user interface for easy interaction.

---

## 🚀 Key Features

* Real-time weapon detection
* Gun and knife identification with confidence scores
* Person detection and localization
* YOLOv8 custom training pipeline
* Image inference support
* Video inference support
* FastAPI REST API backend
* Streamlit frontend
* Public deployment using ngrok
* Bounding box visualization

---

## 🖼️ Project Demonstration

### Training Dataset Samples

![Dataset Samples](screenshots/dataset_samples.png)

The model was trained on a custom annotated dataset containing persons, guns, and knives. Bounding boxes were generated in YOLO format and verified before training.

### Gun Detection Example

![Gun Detection](screenshots/demo_detection_gun.png)

The model successfully detects both the person and firearm with high confidence scores.

### Knife Detection Example

![Knife Detection](screenshots/demo_detection_knife.png)

The model accurately identifies knives carried by individuals in surveillance-style environments.

---

## 🛠️ Tech Stack

### Machine Learning

* Python
* YOLOv8
* PyTorch
* Ultralytics
* OpenCV

### Backend

* FastAPI
* Uvicorn

### Frontend

* Streamlit

### Deployment

* ngrok
* Google Colab

### Data Processing

* NumPy
* Pillow
* YAML

---

## 📂 Dataset

The dataset contains three object classes:

| Class  | Description            |
| ------ | ---------------------- |
| Person | Human Detection        |
| Gun    | Firearm Detection      |
| Knife  | Sharp Weapon Detection |

Dataset annotations were prepared in YOLO format and split into training and validation sets.

---

## 🧠 Model Training

The project uses YOLOv8 for object detection.

Training configuration:

```python
Model: YOLOv8
Image Size: 640x640
Classes: 3
Epochs: 100
```

Class Mapping:

```python
0 → Person
1 → Knife
2 → Gun
```

---

## 📈 Results

The trained model successfully detects weapons in diverse scenarios:

* Outdoor surveillance footage
* Parking lots
* Public spaces
* CCTV-style camera feeds
* Low-angle security cameras

The model predicts:

* Object class
* Confidence score
* Bounding box coordinates

---

## 🔌 API Deployment

FastAPI backend provides:

* Health Check Endpoint
* Image Detection Endpoint
* Video Detection Endpoint
* JSON Prediction Output

Example response:

```json
{
  "class": "gun",
  "confidence": 0.87
}
```

---

## 💻 Streamlit Interface

The Streamlit application allows users to:

* Upload images
* Upload videos
* View detection results
* Interact with the model without coding

Run locally:

```bash
streamlit run app.py
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/amanjha1807/weapon-detection-system.git
cd weapon-detection-system
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Detection

### Image Detection

```bash
yolo predict model=best.pt source=image.jpg
```

### Video Detection

```bash
yolo predict model=best.pt source=video.mp4
```

### Webcam Detection

```bash
yolo predict model=best.pt source=0
```

---

## 🌍 Real-World Applications

* Smart CCTV Surveillance
* Airport Security
* Railway Stations
* Public Event Monitoring
* Shopping Mall Security
* School & College Safety
* Smart City Surveillance
* Defense Applications

---

## 🔮 Future Improvements

* Real-time alert notifications
* Multi-camera monitoring
* Face recognition integration
* Edge deployment on Jetson Nano
* AWS cloud deployment
* Threat severity scoring

---

## 👨‍💻 Author

**Aman Jha**

B.Tech Student | Machine Learning Enthusiast | AI Developer

GitHub: https://github.com/amanjha1807

LinkedIn: https://linkedin.com/in/aman-jha-348277291

---

## 📜 License

This project is licensed under the MIT License.


