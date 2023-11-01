from flask import Flask, render_template, request
import os
import cv2
import numpy as np
from sklearn.cluster import KMeans
from collections import Counter

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the 'uploads' directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def get_most_common_colors(image_path, num_colors=10):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Flatten the image using NumPy
    img = img.reshape((-1, 3))

    k = num_colors
    clt = KMeans(n_clusters=k, n_init=10)  # Set n_init to suppress the warning
    clt.fit(img)

    counts = Counter(clt.labels_)

    most_common_labels = counts.most_common(num_colors)
    most_common_colors = [clt.cluster_centers_[label] for label, count in most_common_labels]

    most_common_hex_colors = [rgb_to_hex(color) for color in most_common_colors]

    return most_common_hex_colors


def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(int(rgb[0]), int(rgb[1]), int(rgb[2]))


@app.route('/', methods=['GET', 'POST'])
def index():
    colors = []
    if request.method == 'POST':
        if 'image' in request.files:
            image = request.files['image']
            if image.filename != '':
                try:
                    image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
                    image.save(image_path)
                    colors = get_most_common_colors(image_path)
                except Exception as e:
                    print("Error saving the image:", e)

    return render_template('index.html', colors=colors)


if __name__ == '__main__':
    app.run(debug=True)
