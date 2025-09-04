import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    payload = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=payload, headers=header)
    resp_json = json.loads(response.text)
    emotions = resp_json["emotionPredictions"][0]["emotion"]
    
    result = {}
    highest_score = 0
    dominant_emotion = ""
    
    for emotion, score in emotions.items():
        result[emotion] = score
        if score > highest_score:
            highest_score = score
            dominant_emotion = emotion

    result['dominant_emotion'] = dominant_emotion
    
    return result

# from emotion_detection import emotion_detector
# from pprint import pprint
# text = "I am so happy doing this"
# result = emotion_detector(text)
# pprint(result)