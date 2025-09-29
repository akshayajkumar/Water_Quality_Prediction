import streamlit as st
import pandas as pd
import joblib

# Load trained model pipeline
@st.cache_resource
def load_model():
    return joblib.load('final_model.joblib')

model = load_model()

# Set custom threshold
THRESHOLD = 0.4

# Add background image and custom styling
st.markdown("""
<style>
.stApp {
    background-image: linear-gradient(rgba(0, 20, 40, 0.75), rgba(0, 30, 60, 0.8)), 
                      url("https://www.weizmann.ac.il/WeizmannCompass/sites/WeizmannCompass/files/styles/main_image/public/compass_water_952x460px.jpg?itok=yyYkx34J");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

.main .block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    background-color: rgba(255, 255, 255, 0.05);
    border-radius: 15px;
    backdrop-filter: blur(10px);
    margin-top: 1rem;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
}

h1 {
    color: #ffffff !important;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
    text-align: center;
    font-size: 3rem !important;
    margin-bottom: 2rem !important;
}

h2, h3 {
    color: #e6f3ff !important;
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
}

.stSelectbox label, .stNumberInput label, .stSlider label {
    color: #ffffff !important;
    font-weight: 500 !important;
}

.stButton > button {
    background: linear-gradient(45deg, #4a90e2, #357abd) !important;
    color: white !important;
    border: none !important;
    border-radius: 25px !important;
    padding: 0.75rem 2rem !important;
    font-size: 1.1rem !important;
    font-weight: 600 !important;
    box-shadow: 0 4px 15px rgba(74, 144, 226, 0.4) !important;
    transition: all 0.3s ease !important;
}

.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(74, 144, 226, 0.6) !important;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("Water Potability Predictor")

# Styled "What is Water Potability?" section
st.markdown("""
<div style="background: linear-gradient(135deg, rgba(30, 58, 95, 0.9), rgba(74, 144, 226, 0.8)); 
           padding: 20px; border-radius: 15px; border-left: 4px solid #4a90e2; margin: 20px 0;
           backdrop-filter: blur(10px); box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);">
    <h4 style="color: #ffffff; margin: 0 0 15px 0; text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);">💧 What is Water Potability?</h4>
    <p style="color: #e6f3ff; margin: 0; line-height: 1.7; font-size: 1.05rem;">
        Water potability refers to how <strong style="color: #87ceeb;">safe water is for drinking and cooking</strong>. 
        <strong style="color: #87ceeb;">Potable water</strong> is free from harmful chemicals, heavy metals, and microorganisms that can affect health.
    </p>
</div>
""", unsafe_allow_html=True)

from PIL import Image

# Show water quality guidelines image
st.markdown("### 🧾 Safe Water Range Guidelines")
st.markdown("Below is a reference table outlining the **safe ranges for various water quality parameters**:")
image = Image.open("Screenshot 2025-08-05 205916.png")
st.image(image, caption="💧 Safe Ranges for Potable Water", use_container_width=True)



# Input fields
st.header("Enter Water Sample Details")

col1, col2 = st.columns(2)

with col1:
    ph = st.number_input("pH", min_value=0.0, max_value=14.0, value=7.0)
    iron = st.number_input("Iron", min_value=0.0, value=0.01)
    nitrate = st.number_input("Nitrate", min_value=0.0, value=5.0)
    chloride = st.number_input("Chloride", min_value=0.0, value=100.0)
    lead = st.number_input("Lead", min_value=0.0, step=0.001, value=0.01, format="%.5f")
    zinc = st.number_input("Zinc", min_value=0.0, value=0.01)
    color = st.selectbox("Color", ["Colorless", "Near Colorless", "Faint Yellow", "Light Yellow", "Yellow"])

with col2:
    turbidity = st.number_input("Turbidity", min_value=0.0, value=1.0)
    fluoride = st.number_input("Fluoride", min_value=0.0, value=0.5)
    conductivity = st.number_input("Conductivity", min_value=0.0, value=300.0)
    chlorine = st.number_input("Chlorine", min_value=0.0, value=1.0)
    manganese = st.number_input("Manganese", min_value=0.0, value=0.01)
    tds = st.number_input("Total Dissolved Solids", min_value=0.0, value=150.0)
    source = st.selectbox("Source", ["Well", "Aquifer", "Stream", "Ground", "River", "Lake", "Reservoir", "Spring"])

# Additional features
temp_water = st.slider("Water Temperature (°C)", min_value=0.0, max_value=100.0, value=25.0)
temp_air = st.slider("Air Temperature (°C)", min_value=0.0, max_value=100.0, value=30.0)
month = st.selectbox("Month", ["January", "February", "March", "April", "May", "June",
                                "July", "August", "September", "October", "November", "December"])
day = st.number_input("Day of Month", min_value=1, max_value=31, value=1)

# Centered predict button
st.markdown("<br>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    predict_button = st.button("🔍 Predict Potability", use_container_width=True)

# Full-width prediction results
if predict_button:
    input_data = pd.DataFrame([{
        'pH': ph,
        'Iron': iron,
        'Nitrate': nitrate,
        'Chloride': chloride,
        'Lead': lead,
        'Zinc': zinc,
        'Color': color,
        'Turbidity': turbidity,
        'Fluoride': fluoride,
        'Conductivity': conductivity,
        'Chlorine': chlorine,
        'Manganese': manganese,
        'Total Dissolved Solids': tds,
        'Source': source,
        'Water Temperature': temp_water,
        'Air Temperature': temp_air,
        'Month': month,
        'Day': day
    }])

    prob = model.predict_proba(input_data)[0]
    prob_safe = prob[0]
    prob_not_safe = prob[1]
    custom_pred = 1 if prob_not_safe > THRESHOLD else 0

    st.markdown("<br>", unsafe_allow_html=True)
    
    if custom_pred == 0:
        st.success(f"✅ **Prediction Result:** SAFE for consumption")
        st.info(f"🔢 **Model Confidence:** Safe: {prob_safe*100:.2f}% | Not Safe: {prob_not_safe*100:.2f}%")
        st.markdown("""
        <div style="background: linear-gradient(135deg, rgba(212, 237, 218, 0.95), rgba(195, 230, 203, 0.9)); 
                   padding: 20px; border-radius: 15px; border-left: 4px solid #28a745;
                   backdrop-filter: blur(5px); box-shadow: 0 6px 20px rgba(40, 167, 69, 0.2);">
            <p style="color: #155724; margin: 0; font-weight: 600; font-size: 1.1rem; text-align: center;">
                ✅ This water sample appears to be <strong>POTABLE</strong> and safe for drinking based on the analyzed parameters.
            </p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.error(f"⚠️ **Prediction Result:** NOT SAFE for consumption")
        st.info(f"🔢 **Model Confidence:** Safe: {prob_safe*100:.2f}% | Not Safe: {prob_not_safe*100:.2f}%")
        st.markdown("""
        <div style="background: linear-gradient(135deg, rgba(248, 215, 218, 0.95), rgba(241, 169, 175, 0.9)); 
                   padding: 20px; border-radius: 15px; border-left: 4px solid #dc3545;
                   backdrop-filter: blur(5px); box-shadow: 0 6px 20px rgba(220, 53, 69, 0.2);">
            <p style="color: #721c24; margin: 0; font-weight: 600; font-size: 1.1rem; text-align: center;">
                ⚠️ This water sample appears to be <strong>NON-POTABLE</strong> and may not be safe for drinking. Consider water treatment or alternative sources.
            </p>
        </div>
        """, unsafe_allow_html=True)
