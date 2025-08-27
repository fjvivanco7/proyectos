import os
from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = "1726463548"
app._static_folder = os.path.abspath("templates/static/")


@app.route("/", methods=["GET"])
def index():
    title = "Create the input image"
    return render_template("index.html", title=title)

if __name__ == "__main__":
    app.run(debug=True)