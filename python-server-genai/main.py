import json
from google import genai
from google.genai import types
import PIL.Image
import os



def process_image(image_path: str) -> str:
    try:
        # Open the image using PIL
        image = PIL.Image.open(image_path)

        # You can add any image processing logic here if needed
        # For example, extracting some metadata or image features
        width, height = image.size
        print(f"Processing image: {image_path}, Width: {width}, Height: {height}")

        # Initialize the Gemini AI client
        client = genai.Client(api_key="AIzaSyADYqIwkxY3EMT_tPYij1lP3YFvTlAs6ms")

        # Preparing the prompt for AI
        prompt = (
            "Find a solution\n"
            "Give me straight answer ONLY with steps and nothing else\n"
            "Use plain text in your solution (not .md)\n"
            "Use Ukrainian language\n"
            "Create json with structure like this:\n"
            "{name : <problem name>, solution {step1: <first step of solving>, step2: <second step of solving>} answer : <short answer in 1-5 words>}"
            "LITERALY follow my example in constuction aspects like name, solution and steps, answer. Don't add anything else\n"
            "Place the answer in main json body\n"
            'Type "json closed" after generating json\n'
            "If photo don't contain anyone science problem, leave solution part empty and type the advice into answer field to retake photo\n"
            "Use UNICODE table to write roots and other specific symbols"
        )

        # Send the image and the prompt to the Gemini AI model
        response = client.models.generate_content(
            model="gemini-2.0-flash-lite",
            contents=[prompt, image]
        )

        # Extract and process the JSON response from Gemini
        response_text = response.text
        print("AI Response:", response_text)

        # Extract the JSON content
        start_idx = response_text.find("json") + 10
        end_idx = response_text.find("json closed") - 4
        json_content = response_text[start_idx:end_idx]
        json_content = json_content.replace('\n', "", json_content.count("\n"))


        print("Extracted JSON:", json_content)

        # Load the JSON string into a Python dictionary
        # data = json.loads(json_content)
        # print("Parsed Data:", data)

        # Optionally, insert the data into your database (or handle as needed)
        # json_insertion(data)

        json_object = json.dumps(json_content)

        with open("result.json", "w") as outfile:
            outfile.write(json_object)

    except Exception as e:
        # Handle any errors and return a friendly message
        error_message = {"status": "error", "message": str(e)}
        print(f"Error processing image: {str(e)}")
        return json.dumps(error_message)
