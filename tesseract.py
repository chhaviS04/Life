// FOR ARCHIT(Tesseract OCR code)

from flask import Flask, request, jsonify
import pytesseract
from PIL import Image
import io

app = Flask(__name__)

def ocr_extract(image):
    try:
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        print(f"OCR failed: {e}")
        return None

@app.route('/ocr', methods=['POST'])
def ocr():
    if 'report' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['report']
    img = Image.open(file.stream)

    text = ocr_extract(img)

    if text:
        return jsonify({"message": "OCR successful", "extracted_text": text}), 200
    else:
        return jsonify({"error": "OCR failed"}), 500

@app.route('/predict-disease', methods=['POST'])
def predict_disease():
    data = request.json
    report_text = data.get('extracted_text')

    predictions = []
    diet_recommendations = []

    if 'high glucose' in report_text or 'diabetes' in report_text:
        predictions.append("Diabetes")
        diet_recommendations.append("Low sugar diet")

    if 'cholesterol' in report_text:
        predictions.append("High Cholesterol")
        diet_recommendations.append("Low-fat diet")

    if not predictions:
        predictions.append("No significant issues detected")
    
    return jsonify({"disease_predictions": predictions, "diet_recommendations": diet_recommendations}), 200

if __name__ == '__main__':
    app.run(debug=True)
