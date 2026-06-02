from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    data = request.get_json()
    if not data or 'text' not in data:
        return "Invalid request: JSON with 'text' field required", 400

    text_to_analyze = data['text']
    result = emotion_detector(text_to_analyze)

    # Check for None dominant_emotion and handle error
    if result.get('dominant_emotion') is None:
        return "Invalid text! Please try again!", 400

    response_str = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )

    return response_str

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)