from flask import Flask, request, render_template, redirect, url_for
import csv
import os
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './static/'


@app.route('/', methods=['GET', 'POST'])
def index():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'dan.jpg')
    return render_template("index.html", user_image = full_filename)


if __name__ == "__main__":
    app.run(debug=True)
