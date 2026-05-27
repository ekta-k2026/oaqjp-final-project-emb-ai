import json
import requests

def emotion_detector(text_to_analyze):
    """
    Runs emotion detection on the given text using Watson NLP Emotion Predict API,
    extracts emotion scores, finds the dominant emotion, and returns a formatted dictionary.

    Args:
        text_to_analyze (str): The text to analyze.

    Returns:
        dict: A dictionary containing emotion scores and the dominant emotion.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, headers=headers, json=input_json)
    response.raise_for_status()

    # Convert response text into dictionary
    response_dict = json.loads(response.text)

    # Extract emotions dictionary from response
    emotion_predictions = response_dict.get('emotionPredictions', [])
    if not emotion_predictions:
        return {}

    emotions = emotion_predictions[0].get('emotion', {})

    # Extract individual emotion scores
    anger = emotions.get('anger', 0)
    disgust = emotions.get('disgust', 0)
    fear = emotions.get('fear', 0)
    joy = emotions.get('joy', 0)
    sadness = emotions.get('sadness', 0)

    # Find dominant emotion (emotion with highest score)
    emotion_scores = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness
    }
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    # Return formatted dictionary
    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }