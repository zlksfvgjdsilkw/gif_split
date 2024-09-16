from flask import Flask, request, jsonify
import os
import shutil
from PIL import Image, ImageSequence
import base64
import mimetypes

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
PROCESSED_FOLDER = 'processed'

# Ensure the upload and processed folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

def clear_processed_folder():
    """Remove all files and folders from the processed folder."""
    for filename in os.listdir(PROCESSED_FOLDER):
        file_path = os.path.join(PROCESSED_FOLDER, filename)
        if os.path.isfile(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)

def make_even(num):
    """Round a number to the nearest even number."""
    return num if num % 2 == 0 else num + 1

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
    rows = int(request.form.get('rows'))
    cols = int(request.form.get('cols'))

    if not file or not rows or not cols:
        return jsonify({'error': 'Missing file or dimensions'}), 400

    # Round rows and columns to the nearest even numbers
    rows = make_even(rows)
    cols = make_even(cols)

    # Clear the processed folder before processing a new GIF
    clear_processed_folder()

    # Save the uploaded file
    filename = file.filename
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(file_path)

    try:
        # Open and process the GIF
        gif = Image.open(file_path)
        frames = [frame.copy() for frame in ImageSequence.Iterator(gif)]

        # Calculate dimensions for each small GIF
        gif_width, gif_height = gif.size
        cell_width = gif_width // cols
        cell_height = gif_height // rows

        # Adjust dimensions to fit the entire GIF if needed
        last_cell_width = gif_width - (cols - 1) * cell_width
        last_cell_height = gif_height - (rows - 1) * cell_height

        small_gif_urls = []

        for row in range(rows):
            for col in range(cols):
                left = col * cell_width
                top = row * cell_height
                right = left + cell_width if col < cols - 1 else gif_width
                bottom = top + cell_height if row < rows - 1 else gif_height

                small_gif_frames = []
                for frame in frames:
                    small_frame = frame.crop((left, top, right, bottom))
                    small_gif_frames.append(small_frame)

                small_gif_path = os.path.join(PROCESSED_FOLDER, f'small_gif_{row}_{col}.gif')
                small_gif_frames[0].save(small_gif_path, save_all=True, append_images=small_gif_frames[1:], loop=0)

                # Generate URL for the small GIF
                mime_type = mimetypes.guess_type(small_gif_path)[0] or 'image/gif'
                with open(small_gif_path, 'rb') as f:
                    gif_data = f.read()
                    small_gif_urls.append('data:' + mime_type + ';base64,' + base64.b64encode(gif_data).decode('utf-8'))

        return jsonify({'files': small_gif_urls})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
