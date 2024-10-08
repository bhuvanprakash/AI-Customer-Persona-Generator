# AI-Customer-Persona-Generator

This is a simple AI-powered Customer Persona Generator built using Python, Flask, and OpenAI's GPT-3. 
It generates detailed customer personas based on provided product and audience information.
The tool was developed as a side project in our free time to explore the capabilities of language models in creating fictional customer profiles, which can be useful for marketing, user research, or product development teams.
It allows easy deployment as a Flask-based web API.

## Features
- Generates customer personas based on input details (product and target audience).
- Easy-to-use Flask-based web API.
- Outputs detailed personas with information like age, gender, location, and buying habits.

## Technologies Used
- Python
- Flask
- OpenAI GPT-3

## Installation Instructions

1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/AI-Customer-Persona-Generator.git
   cd AI-Customer-Persona-Generator

2. Set up a virtual environment (optional but recommended):
   ```
   python3 -m venv venv
   source venv/bin/activate
   # On Windows use `venv\Scripts\activate`

4. Install the required packages
   ```
   pip install -r requirements.txt

5. Set up your OpenAI API key
   Replace "YOUR-API-KEY" in the script with your actual OpenAI API key.

6. Run the Flask app
   ```
   python app.py


# API Usage:
Once the server is running, you can make a POST request to /generate_persona.

Example:
```
curl -X POST http://127.0.0.1:5000/generate_persona \
  -H "Content-Type: application/json" \
  -d '{"product_info": "Smartphone", "audience_info": "Tech-savvy millennials"}'
```
Expected Output:
```
   {
     "persona": "Meet Alex, a 28-year-old tech enthusiast who lives in North America..."
   }
```
# Contributions:
Feel free to open issues/ submit pull requests for feature suggestions or bug fixes. 
Contributions are welcome!
