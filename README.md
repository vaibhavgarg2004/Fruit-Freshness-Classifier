# 🍎 Fruit Freshness Classifier

A smart and lightweight Streamlit-based web application that analyzes fruit images to determine their freshness. Built using a fine-tuned ResNet50 deep learning model, this tool helps vendors, quality inspectors, and consumers make quick and informed decisions about fruit quality. Simply upload a photo of a fruit, and the app will predict whether it is fresh or stale, along with the specific fruit type.

---

<!-- ## 🌐 Live Website
You can try the tool live here: **[Car Damage Detector](https://vaibhav-project-car-damage-detector.streamlit.app/)**

---

## 🎥 Presentation
Watch the full project presentation here: **[Car Damage Detector Presentation](https://vaibhav-projects.my.canva.site/car-damage-detector)**

--- -->

## 🛠 Features  
- Upload a fruit image and instantly get a freshness prediction.
- Classifies images into 16 classes (8 fruits × 2 freshness states):
   - Fresh Banana, Fresh Lemon, Fresh Lulo, Fresh Mango, Fresh Orange, Fresh Strawberry, Fresh Tamarillo, Fresh Tomato
   - Stale Banana, Stale Lemon, Stale Lulo, Stale Mango, Stale Orange, Stale Strawberry, Stale Tamarillo, Stale Tomato
- Uses ResNet50 fine-tuned on a custom curated fruit dataset.
- Works on images with different lighting, angles, and backgrounds.
- Simple, fast, and deployable with no backend server required. 
- Optimized for local or cloud usage.

---

## 📂 Project Structure

```
Fruit_Freshness_Classifier/
│
├── model/
│   ├── saved_model.pth           # Trained ResNet50 model weights
│
├── app.py                        # Streamlit application logic
├── model_helper.py               # Prediction logic using the trained model
├── LICENSE                       # Apache License file
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```

---

## 🚀 How to Run Locally  
### Prerequisites:  
- Python 3.8+

1. **Clone the repository**:
   ```bash
   git clone https://github.com/vaibhavgarg2004/Fruit-Freshness-Classifier.git
   cd Fruit-Freshness-Classifier
   ```
2. **Install dependencies**:   
   ```commandline
    pip install -r requirements.txt
   ```
3. **Run the Streamlit app**:   
   ```commandline
    streamlit run app.py
   ```

---

## 🧠 How It Works

1. **Image Upload & Display**  
   - The user uploads a fruit image (JPG/PNG) through the Streamlit interface.
   - The app saves the uploaded file temporarily and displays it in the application.

2. **Preprocessing & Model Inference**  
   - The image is resized, rotated, normalized, and converted to a tensor.
   - The fine-tuned ResNet50 model processes the image to classify it into one of 16 freshness categories.

3. **Prediction Output**  
   - The predicted fruit class is instantly shown in the app interface, allowing users to quickly understand the car’s condition.

---
   
<!-- ## 🖼️ Application Snapshot

![Application UI](car_damage_detector_ui.png)

--- -->

## 📄 License
This project is licensed under the **Apache License 2.0**. See the [LICENSE](./LICENSE) file for details.

---

*Stay fresh. Detect fruit quality instantly.*