import gradio as gr
import skops.io as sio
from skops.io import get_untrusted_types

# Load the trained model with simple path
model_path = "./model/drug_pipeline.skops"
untrusted_types = get_untrusted_types(file=model_path)
pipe = sio.load(model_path, trusted=untrusted_types)

def predict_drug(age, sex, blood_pressure, cholesterol, na_to_k_ratio):
    """Predict drugs based on patient features.

    Args:
        age (int): Age of patient
        sex (str): Sex of patient 
        blood_pressure (str): Blood pressure level
        cholesterol (str): Cholesterol level
        na_to_k_ratio (float): Ratio of sodium to potassium in blood

    Returns:
        str: Predicted drug label
    """
    features = [age, sex, blood_pressure, cholesterol, na_to_k_ratio]
    predicted_drug = pipe.predict([features])[0]
    
    # Get confidence scores
    confidence = pipe.predict_proba([features])[0]
    max_confidence = max(confidence)
    
    label = f"🔬 Predicted Drug: {predicted_drug}"
    confidence_text = f"📊 Confidence: {max_confidence:.2%}"
    
    return f"{label}\n{confidence_text}"

# Define input components
inputs = [
    gr.Slider(15, 74, step=1, value=30, label="🎂 Age"),
    gr.Radio(["M", "F"], value="M", label="👤 Sex"),
    gr.Radio(["HIGH", "NORMAL", "LOW"], value="NORMAL", label="🩸 Blood Pressure"),
    gr.Radio(["HIGH", "NORMAL"], value="NORMAL", label="🧪 Cholesterol"),
    gr.Slider(6.2, 38.2, step=0.1, value=15.4, label="⚖️ Na_to_K Ratio"),
]

outputs = [gr.Textbox(label="Prediction Result", lines=3)]

# Example cases for testing
examples = [
    [30, "M", "HIGH", "NORMAL", 15.4],
    [35, "F", "LOW", "NORMAL", 20.5],
    [50, "M", "HIGH", "HIGH", 34.0],
    [25, "F", "NORMAL", "HIGH", 25.3],
    [60, "M", "LOW", "NORMAL", 12.8],
]

title = "🏥 Drug Classification - MLOps CI/CD Practice"
description = """
### 📋 How to Use:
Enter patient characteristics below to get the appropriate drug type prediction.

**Input Features:**
- **Age**: 15-74 years
- **Sex**: M (Male) or F (Female)  
- **Blood Pressure**: HIGH, NORMAL, or LOW
- **Cholesterol**: HIGH or NORMAL
- **Na_to_K Ratio**: 6.2-38.2
"""

article = """
### 🚀 About This Application
This application is an implementation of **MLOps CI/CD Pipeline** for drug classification using:
- **Machine Learning**: RandomForest Classifier
- **CI/CD**: GitHub Actions for automation
- **Deployment**: Hugging Face Spaces
- **Model Format**: scikit-learn with skops

**Automated Pipeline:**
1. 📊 Data Processing & Training
2. 🧪 Model Testing & Validation  
3. 🚀 Automatic Deployment
4. 📈 Monitoring & Updates

Created as part of **Machine Learning Operations (MLOps)** learning.
"""

# Create and launch the interface
iface = gr.Interface(
    fn=predict_drug,
    inputs=inputs,
    outputs=outputs,
    examples=examples,
    title=title,
    description=description,
    article=article,
    theme=gr.themes.Soft(),
    analytics_enabled=False,
)

if __name__ == "__main__":
    iface.launch()
