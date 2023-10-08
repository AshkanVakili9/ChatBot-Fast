import requests

url = "https://play.ht/api/v2/tts"

payload = {
    "text": "Hello from the ultra-realistic voice.",
    "voice": "larry",
    "quality": "medium",
    "output_format": "mp3",
    "speed": 1,
    "sample_rate": 24000,
    "voice_engine": "PlayHT2.0"
}
headers = {
    "accept": "text/event-stream",
    "content-type": "application/json",
    "AUTHORIZATION": "Bearer 95ef65a86e4a45a694df67bb6b19fafa",
    "X-USER-ID": "BEZ9arKQ17ajyQ9ezbN7kfQhGkv2"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
