from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Hugging Face API Key (তোমার API Key এখানে বসাও)
HUGGINGFACE_API_KEY = "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"
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"


headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate_image():
    data = request.json
    prompt = data.get("text")

    try:
        response = requests.post(API_URL, headers=headers, json={"inputs": prompt})

        if response.status_code == 200:
            # API থেকে ইমেজ URL রিটার্ন করবে
            image_data = response.content  # ইমেজ বাইনারি ডাটা
            with open("static/generated_image.png", "wb") as f:
                f.write(image_data)

            return jsonify({"image_url": "/static/generated_image.png"})
        else:
            return jsonify({"error": f"API Error: {response.status_code}, {response.text}"})

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == '__main__':
    app.run(debug=True)
