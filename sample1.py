import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Sample dataset for symptoms and diseases (toy example)
symptom_data = np.array([
    [1, 1, 0, 0, 1],  # Common Cold
    [1, 1, 1, 0, 0],  # Flu
    [1, 1, 1, 1, 0],  # COVID-19
    [0, 0, 1, 1, 0],  # Migraine
])

# Labels for diseases, one-hot encoded
disease_labels = np.array([
    [1, 0, 0, 0],  # Common Cold
    [0, 1, 0, 0],  # Flu
    [0, 0, 1, 0],  # COVID-19
    [0, 0, 0, 1],  # Migraine
])

# Build a simple neural network with TensorFlow
model = Sequential([
    Dense(8, input_shape=(5,), activation='relu'),  # Input layer with 5 features
    Dense(8, activation='relu'),                    # Hidden layer
    Dense(4, activation='softmax')                  # Output layer for 4 diseases
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(symptom_data, disease_labels, epochs=200, verbose=0)

# Function to predict disease based on user symptoms
def predict_disease(symptoms):
    symptoms = np.array([symptoms])  # Convert symptoms to a 2D array
    prediction = model.predict(symptoms)  # Get the predicted probabilities for each disease
    predicted_class = np.argmax(prediction)  # Get the index of the highest probability
    diseases = ['Common Cold', 'Flu', 'COVID-19', 'Migraine']  # Disease labels
    return diseases[predicted_class]

# Simulate user input for symptoms (1 = present, 0 = absent)
user_symptoms = [1, 1, 1, 0, 0]  # Example: fever, cough, fatigue

# Predict the disease
predicted_disease = predict_disease(user_symptoms)

# Output the predicted disease
print(f"Based on your symptoms, you might have: {predicted_disease}")
