'''  Emotion Detector based on Flask
'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def detect_emotion():
    ''' Receives text from main page for analysis, runs emotion detection
        and sends back the result as message.
    '''
    text_to_analyze = request.args.get("textToAnalyze")
    res = emotion_detector(text_to_analyze)

    if res["dominant_emotion"] is None:
        return "<b>Invalid text! Please try again!</b>"

    vals = (
        f"'anger': {res['anger']}, "
        f"'disgust': {res['disgust']}, "
        f"'fear': {res['fear']}, "
        f"'joy': {res['joy']} and "
        f"'sadness': {res['sadness']}"
    )

    return (
        f"For the given statement, the system response is {vals}. "
        f"The dominant emotion is <b>{res['dominant_emotion']}</b>"
    )

@app.route("/")
def render_index_page():
    ''' Renders main page.
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
