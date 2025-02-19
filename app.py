import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Set your Amper Music API key here
API_KEY = 'your-amper-api-key'

# Function to generate music using Amper API
def generate_music(prompt):
    url = "https://api.ampermusic.com/v1/compositions"  # Replace with actual Amper endpoint
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }
    data = {
        "prompt": prompt,  # Use the user’s input as the prompt
        "genre": "pop",  # You can change the genre based on user input
        "mood": "happy",  # Adjust mood as needed
    }

    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        return response.json()  # This would return the music data or URL
    else:
        return None

@app.route('/generate_music', methods=['POST'])
def create_song():
    prompt = request.json.get('prompt')  # Get the user's prompt
    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400
    
    # Generate music based on the prompt
    music_data = generate_music(prompt)
    if music_data:
        return jsonify({'song_url': music_data.get('song_url')})
    else:
        return jsonify({'error': 'Failed to generate music'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
