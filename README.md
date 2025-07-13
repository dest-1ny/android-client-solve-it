# 📡 Gemini AI Python Server

This repository contains a Python backend that processes images using Gemini AI and returns a structured response in JSON format.

## 📌 Purpose

This server is designed to work with an Android app. The client sends an image (e.g. a photo of a math or science problem), and the server detects whether the image contains a solvable problem. If so, it generates a step-by-step solution and sends it back in JSON format. Otherwise, it responds with an advice to retake the photo.

---

## ⚙️ How It Works

### 🧠 AI Processing (`main.py`):

1. The server saves the received image locally.
2. It opens the image using PIL (Python Imaging Library).
3. A carefully crafted prompt is generated to instruct the Gemini AI model on how to respond.
4. The image and the prompt are sent to the `gemini-2.0-flash-lite` model.
5. The server extracts a JSON object from the AI’s raw text response and saves it to `result.json`.

### 🌐 REST API (`server.py`):

- **Endpoint:** `POST /upload`
- **Expected input:** Form-data with a file field named `image`
- **Responses:**
  - `200 OK`: Returns the `result.json` file with the solution
  - `400`: No image uploaded
  - `500`: Processing failed or output file not found

---

## 🧪 Requirements

- Python 3.10+
- Flask
- Pillow
- Google Generative AI SDK

### Install dependencies:

```bash
pip install flask pillow google-generativeai
