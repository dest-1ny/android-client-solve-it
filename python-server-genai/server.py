from flask import Flask, request, send_file, jsonify
from werkzeug.utils import secure_filename
import os

from main import process_image

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image = request.files['image']
    original_filename = secure_filename(image.filename)  
    image_path = os.path.join(os.getcwd(), original_filename)
    image.save(image_path)

    try:
        process_image(image_path)
    except Exception as e:
        return jsonify({"error": f"Processing failed: {str(e)}"}), 500
    finally:
        if os.path.exists(image_path):
            os.remove(image_path)

    if os.path.exists("result.json"):
        return send_file("result.json", as_attachment=True)
    else:
        return jsonify({"error": "result.json not found after processing"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)