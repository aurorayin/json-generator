import json
import os
from pathlib import Path
from flask import Flask, render_template, request
from JSON import generate_json  # Import the Python function

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_json', methods=['POST'])
def generate_json_route():
    try:
        # Get user input from the form
        visual_distance = float(request.form['visual_distance'])
        visual_vertical_rotation = [int(request.form['visual_vertical_rotation'])]
        visual_horizontal_interval = int(request.form['visual_horizontal_interval'])
        num_audio_sources = int(request.form['num_audio_sources'])

        # Call your Python function to generate the JSON
        json_data = generate_json(
            visual_distance, visual_distance, visual_vertical_rotation,
            visual_horizontal_interval, num_audio_sources
        )

        output_file = 'output.json'

        # Get the home directory
        home_dir = str(Path.home())

        # Combine the home directory and "Downloads" to get the Downloads path
        destination_path = os.path.join(home_dir, 'Downloads')

        # Create the full output path
        output_path = os.path.join(destination_path, output_file)

        with open(output_path,'w') as outfile:
            json.dump(json_data, outfile, ensure_ascii=False, indent=4)

        # Save the JSON data to a file
        with open('output.json', 'w') as json_file:
            json.dump(json_data, json_file, ensure_ascii=False, indent=4)

        return 'JSON file generated successfully!'
    except Exception as e:
        return f'Error: {str(e)}'

if __name__ == '__main__':
    app.run(debug=True)