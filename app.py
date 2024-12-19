import gradio as gr
import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Load the pre-trained model
model = joblib.load('best_model (10).pkl')

# Load the StandardScaler used for preprocessing
scaler = joblib.load('scaler.pkl')  # Assuming the scaler was saved separately

# Define the function to predict the class
def predict_class(*features):
    # Convert the input features into a dataframe
    feature_list = list(features)
    feature_df = pd.DataFrame([feature_list], columns=["seed", "SiO2", "NaOH", "SDA", "B2O3","H2O", "seed amount", "temperature(°C)", "time (day)", "si/al(ICP-AES)", "fd"  ])  # Adjust columns to match your data
    
    # Apply scaling (use the same scaler that was used for training)
    feature_scaled = scaler.transform(feature_df)
    
    # Make the prediction using the model
    prediction = model.predict(feature_scaled)
    
    return prediction[0]

# Define the Gradio interface
inputs = [
    gr.inputs.Textbox(label="seed", type="text"),  # Adjust according to your feature names
    gr.inputs.Textbox(label="SiO2", type="text"),
    gr.inputs.Textbox(label="NaOH", type="text"),
    gr.inputs.Textbox(label="SDA", type="text"),
    gr.inputs.Textbox(label="B2O3", type="text"),
    gr.inputs.Textbox(label="H2O", type="text"),
    gr.inputs.Textbox(label="seed amount", type="text"),
    gr.inputs.Textbox(label="temperature(°C)", type="text"),
    gr.inputs.Textbox(label="time (day)", type="text"),
    gr.inputs.Textbox(label="si/al(ICP-AES)", type="text"),
    gr.inputs.Textbox(label="fd", type="text"),

    
]

outputs = gr.outputs.Textbox(label="Predicted Class")

# Launch the Gradio interface
iface = gr.Interface(fn=predict_class, inputs=inputs, outputs=outputs, live=True)

# Launch the app
iface.launch()
