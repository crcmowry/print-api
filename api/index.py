# Landing page for the print API, explaining its endpoints
from api import app
from flask import render_template

@app.route('/', methods=['GET'])
def index():
    return render_template("upload.html")
