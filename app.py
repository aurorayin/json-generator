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
        # Define default values for the parameters
        default_visual_distance = 2.0
        default_visual_vertical_rotation = [30]
        default_visual_horizontal_interval = 45
        default_num_audio_sources = 8
        default_file_name = 'output'

        # Get user input from the form
        visual_distance = request.form.get('visual_distance')
        visual_vertical_rotation = request.form.get('visual_vertical_rotation')
        visual_horizontal_interval = request.form.get('visual_horizontal_interval')
        num_audio_sources = request.form.get('num_audio_sources')
        file_name = request.form.get('file_name')

        # Check if fields are empty and set default values if necessary
        visual_distance = float(visual_distance) if visual_distance else default_visual_distance
        visual_vertical_rotation = [int(visual_vertical_rotation)] if visual_vertical_rotation else default_visual_vertical_rotation
        visual_horizontal_interval = int(visual_horizontal_interval) if visual_horizontal_interval else default_visual_horizontal_interval
        num_audio_sources = int(num_audio_sources) if num_audio_sources else default_num_audio_sources
        file_name = file_name if file_name else default_file_name
        
        # Call your Python function to generate the JSON
        json_data = generate_json(
            visual_distance, visual_distance, visual_vertical_rotation,
            visual_horizontal_interval, num_audio_sources
        )

        output_file = file_name + '.json'

        # Get the home directory
        home_dir = str(Path.home())

        # Combine the home directory and "Downloads" to get the Downloads path
        destination_path = os.path.join(home_dir, 'Downloads')

        # Create the full output path
        output_path = os.path.join(destination_path, output_file)

        with open(output_path,'w') as outfile:
            json.dump(json_data, outfile, ensure_ascii=False, indent=4)

        # Save the JSON data to a file
        with open(output_file, 'w') as json_file:
            json.dump(json_data, json_file, ensure_ascii=False, indent=4)

        return 'JSON file generated successfully!'
    except Exception as e:
        return f'Error: {str(e)}'

if __name__ == '__main__':
    app.run(debug=True)