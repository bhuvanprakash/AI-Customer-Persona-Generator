from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Setting up the API Key
openai.api_key = "YOUR-API-KEY"

# Route to generate customer personas
@app.route('/generate_persona', methods=['POST'])
def generate_persona():
    data = request.json
    product_info = data.get('product_info', 'Default Product')
    audience_info = data.get('audience_info', 'Default Audience')

    # OpenAI GPT prompt
    prompt = f"Create a customer persona for a product: {product_info} targeting audience: {audience_info}"

    # Call GPT API
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200
    )

    persona = response.choices[0].text.strip()

    return jsonify({"persona": persona})

# Run the app
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
