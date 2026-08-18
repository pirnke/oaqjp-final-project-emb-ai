import requests

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json=myobj, headers=headers)
    if response.status_code == 200:
        try:
            data = response.json()
            emotion = data["emotionPredictions"][0]["emotion"]
            dominant_emotion = sorted(emotion.items(), key=lambda item: item[1], reverse=True)[0]
            return {
                "anger": emotion["anger"],
                "disgust": emotion["disgust"],
                "fear": emotion["fear"],
                "joy": emotion["joy"],
                "sadness": emotion["sadness"],
                "dominant_emotion": dominant_emotion[0]
            }
        except Exception:
            pass

    return None