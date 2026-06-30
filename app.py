from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

classifier = pipeline("sentiment-analysis")

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    text = ""

    if request.method == "POST":
        text = request.form["text"]
        if text.strip():
            prediction = classifier(text)[0]
            result = {
                "label": prediction["label"],
                "score": round(prediction["score"] * 100, 2)
            }

    return render_template("index.html", result=result, text=text)

if __name__ == "__main__":
    app.run(debug=True)