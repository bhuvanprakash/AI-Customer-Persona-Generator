from flask import Flask, request, jsonify, render_template
import openai
import time

app = Flask(__name__)

AIML_API_URL = "https://api.aimlapi.com/v1"
AIML_API_KEY = "Your-api-key"  # Your AIMLAPI key

openai.api_key = AIML_API_KEY
openai.api_base = AIML_API_URL

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_persona', methods=['POST'])
def generate_persona():
    data = request.json
    product_info = data.get('product_info', 'Default Product')
    audience_info = data.get('audience_info', 'Default Audience')
    prompt = f"Create a customer persona for a product: {product_info} targeting audience: {audience_info}"

    try:
        completion = openai.Completion.create(
            model="mistralai/Mistral-7B-Instruct-v0.2",
            prompt=prompt,
            temperature=0.7,
            max_tokens=200
        )
        print("API Response:", completion)
        persona = completion['choices'][0]['text'].strip()
        return jsonify({"persona": persona})
    
    except openai.error.RateLimitError as e:
        # Handle rate limit (HTTP 429)
        print(f"Rate limit exceeded: {e}")
        return jsonify({"error": "API rate limit exceeded. Please try again later."}), 429

    except Exception as e:
        # Log the detailed error and traceback
        print(f"Error: {e}")
        traceback.print_exc()  
        return jsonify({"error": f"Failed to generate persona: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)
