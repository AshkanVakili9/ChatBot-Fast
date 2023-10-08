import requests
from decouple import config

ELEVEN_LABS_API_KEY = config('ELEVEN_LABS_API_KEY')
PLAY_HT_API_KEY = config('PLAY_HT_API_KEY')



# Eleven Labs
# Convert Text to Speech
def convert_text_to_speech(message):

    # Define data (body)
    body = {
        # 'text': message,
        # 'voice_settings':{
        #     "stability": 0,
        #     "similarity_boost": 0,
        #     "style": 0,
        #     "use_speaker_boost": True
        # }
        
        
        # 'Text':message,
        # 'Speaker':'Female1',
        # 'PitchLevel':5,
        # 'PunctuationLevel':0,
        # 'SpeechSpeedLevel':6,
        # 'ToneLevel':0,
        # 'GainLevel':0,
        # 'BeginningSilence':0,
        # 'EndingSilence':0,
        # 'Format':'mp3',
        # 'Base64Encode':0,
        # 'Quality':'low',
        # 'APIKey':'GDLOHOP1KGTHR0D'
        
        
                
        
        "text": message,
        "voice": "Abigail",
        "quality": "medium",
        # "output_format": "mp3",
        "speed": 1,
        "sample_rate": 24000,
        "voice_engine": "PlayHT2.0"

    }

    # Define Voice
    voice_rachel = '21m00Tcm4TlvDq8ikWAM'


    # Contracting headers and Endpoint
    headers = {
        # 'xi-api-key': PLAY_HT_API_KEY,
        # 'Content-Type': 'application/json',
        'accept': 'audio/mpeg',
        
        # "accept": "text/event-stream",
        "content-type": "application/json",
        "AUTHORIZATION": "Bearer 95ef65a86e4a45a694df67bb6b19fafa",
        "X-USER-ID": "BEZ9arKQ17ajyQ9ezbN7kfQhGkv2"
    }
    # endpoint = 'http://api.farsireader.com/ArianaCloudService/ReadText'
    endpoint = 'https://play.ht/api/v2/tts'
    # endpoint = f'https://api.elevenlabs.io/v1/text-to-speech/{voice_rachel}'

    # Send request
    try:
       response =  requests.post(endpoint, json=body, headers=headers)
       print (response.content) 
    except Exception as e:
        print(e)
        return 

    # Handle response
    if response.status_code == 200:
        return response.content
    else:
        return 
