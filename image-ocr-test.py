import os
import logging
from flask import Flask, request, jsonify, render_template, session, redirect, url_for
from flask_cors import CORS
import cv2
import numpy as np
from gtts import gTTS
import pytesseract
from PIL import Image

print("os imported")
logging.basicConfig(level=logging.DEBUG)
os.environ["CUDA_VISIBLE_DEVICES"] = ""  # Deactivates GPU

app = Flask(__name__)
CORS(app)  # Enable CORS for all paths

app.secret_key = os.environ.get('SECRET_KEY', 'default_key_for_dev')
UPLOAD_FOLDER = './upload/'
PROCESSED_FOLDER = './process/'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)
os.makedirs('./static', exist_ok=True)

# Function to process a single image
def process_image(image_path):
    print("Entered process_image function")
    image = cv2.imread(image_path)
    print("Image read")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    print("Image converted to grayscale")

    processed_image_path = os.path.join(PROCESSED_FOLDER, "processed_image.jpg")
    cv2.imwrite(processed_image_path, gray)
    print("Processed image saved")

    return processed_image_path

# Route for the main page
@app.route('/')
def index():
    extracted_text = session.get('extracted_text', '')
    audio_url = session.get('audio_url', '')  # Fetch the audio URL from session
    return render_template('index.html', extracted_text=extracted_text, audio_url=audio_url)

# Route to process the image
@app.route('/process', methods=['POST'])
def process():
    if 'image' not in request.files:
        return jsonify({'error': 'No image found'}), 400

    file = request.files['image']
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # Process the uploaded image
    processed_image_path = process_image(file_path)

    try:
        # Run OCR using pytesseract on the processed image
        image = Image.open(processed_image_path)
        extracted_text = pytesseract.image_to_string(image)
        print(f"Extracted text: {extracted_text}")

        session['extracted_text'] = extracted_text  # Store the extracted text in the session

        return redirect(url_for('index'))
    except Exception as e:
        print(f"Error during OCR: {e}")
        return jsonify({'error': 'Error during OCR processing'}), 500

# Route to generate audio
@app.route('/generate_audio', methods=['POST'])
def generate_audio():
    extracted_text = session.get('extracted_text', '')

    if not extracted_text:
        return jsonify({'error': 'No extracted text to convert to audio'}), 400

    text = extracted_text

    try:
        # Generate audio with Google Text-to-Speech
        static_audio_path = os.path.join('./static', 'output_audio.mp3')
        
        tts = gTTS(text, lang='en')
        tts.save(static_audio_path)

        # Store the audio URL in session
        session['audio_url'] = f'/static/output_audio.mp3'

        return redirect(url_for('index'))

    except Exception as e:
        print(f"Error generating or saving the audio: {e}")
        return jsonify({'error': f'Error generating or saving the audio: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, debug=True, use_reloader=False)