from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def detect_emotion():
    text_to_analyze = request.args.get("textToAnalyze")
    res = emotion_detector(text_to_analyze)

    if res["dominant_emotion"] is None:
        return "<b>Invalid text! Please try again!</b>"

    vals = f"'anger': {res['anger']}, 'disgust': {res['disgust']}, 'fear': {res['fear']}, 'joy': {res['joy']} and 'sadness': {res['sadness']}"
    return f"For the given statement, the system response is {vals}. The dominant emotion is <b>{res['dominant_emotion']}</b>"

@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)