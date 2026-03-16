from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Default detection using dataset/logs.csv
@app.route("/detect")
def detect():

    result = subprocess.check_output(["python", "model.py"]).decode("utf-8")

    lines = result.split("\n")

    total = lines[2].split(":")[1].strip()
    normal = lines[3].split(":")[1].strip()
    threat = lines[4].split(":")[1].strip()

    return render_template(
        "result.html",
        total=total,
        normal=normal,
        threat=threat
    )


# Upload new log file
@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["file"]
    filepath = "dataset/uploaded_logs.csv"
    file.save(filepath)

    result = subprocess.check_output(["python", "model.py", filepath]).decode("utf-8")

    lines = result.split("\n")

    total = lines[2].split(":")[1].strip()
    normal = lines[3].split(":")[1].strip()
    threat = lines[4].split(":")[1].strip()

    return render_template(
        "result.html",
        total=total,
        normal=normal,
        threat=threat
    )


if __name__ == "__main__":
    app.run(debug=True)