import streamlit as st
import tempfile
import os  
from model_helper import predict

# Set page config
st.set_page_config(page_title="Fruit Freshness Classifier", page_icon="🍎", layout="centered")

# Styled header
st.markdown("""
    <div style="background-color:#fff5e6; padding: 15px; border-radius: 12px;">
        <h1 style="
            color: #b34700;
            text-align: center;
            margin: 0;
            font-size: 28px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        ">
            🍎 Fruit Freshness Classifier
        </h1>
    </div>
""", unsafe_allow_html=True)

st.markdown("## 📸 Upload a fruit image:")

# File uploader block
uploaded_file = st.file_uploader("Choose a fruit image (JPG/PNG)", type=["jpg", "png"])

if uploaded_file:
    # Create a temporary file to save the image
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
        tmp.write(uploaded_file.getbuffer())
        temp_image_path = tmp.name

    # Display the uploaded image nicely
    st.image(uploaded_file, caption="Uploaded Fruit Image", use_container_width=True)

    # Horizontal line separator
    st.markdown("---")

    if st.button("🔎 Predict Freshness"):
        progress = st.progress(0, text="Analyzing image...")

        prediction = predict(temp_image_path)
        progress.progress(100, text="Prediction complete!")

        st.success(f"🍏 **Predicted Freshness:** {prediction}")

        # Clean up temporary file after prediction
        try:
            os.remove(temp_image_path)
        except Exception as e:
            st.warning(f"Could not delete temporary file: {e}")
