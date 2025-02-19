import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Function to generate music using Riffusion API
def generate_music(prompt):
    url = "https://riffusion.com/api/generate"  # Replace with actual Riffusion API
    data = {"prompt": prompt}
    response = requests.post(url, json=data)
    
    if response.status_code == 200:
        return response.json().get("audio_url")  # Returns the music file URL
    else:
        return None

@app.route('/generate_music', methods=['POST'])
def create_song():
    prompt = request.json.get('prompt')
    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400
    
    music_url = generate_music(prompt)
    if music_url:
        return jsonify({'song_url': music_url})
    else:
        return jsonify({'error': 'Music generation failed'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
