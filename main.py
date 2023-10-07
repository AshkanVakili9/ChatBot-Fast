# uvicorn main:app --reload


# Main Imports
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config


# Custom Function Imports
from functions.openai_request import convert_audio_to_text, get_chat_response
from functions.database import store_messages, reset_messages
from functions.text_to_speeeh import convert_text_to_speech 

# Initiate App
app = FastAPI()


# CORS - Origins
origins = [
    'http://localhost:5173'
    'http://localhost:5174'
    'http://localhost:4173'
    'http://localhost:4174'
    'http://localhost:3000'
]


# CORS - Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*'],
)


# Check Health
@app.get('/health')
async def check_health():
    return {'message': 'healthy :)'}

# Reset Messages
@app.get('/reset')
async def reset_conversation():
    reset_messages()
    return {'message': 'conversation reset'}


# Get audio 
@app.get('/post-audio-get/')
async def get_audio():
    
    # Get Saved Audio
    audio_input = open('voice.mp3', 'rb')

    # Decode Audio
    message_decoded = convert_audio_to_text(audio_input)
    
    # Guard: Ensure that message_decoded
    if not message_decoded:
        return HTTPException(status_code=400, detail='Failed to decode audio')
    
    # Get ChatGPT response
    chat_response = get_chat_response(message_decoded)
    
    # Guard: Ensure that chat_response
    if not chat_response:
        return HTTPException(status_code=400, detail='Failed to get chat response')
    
    # Store Messages
    store_messages(message_decoded, chat_response)
    
    
    # Convert ChatGPT response to audio
    audio_output = convert_text_to_speech(chat_response)
    
    # Guard: Ensure that chat_response
    if not audio_output:
        return HTTPException(status_code=400, detail='Failed to get Eleven Labs audio response')
    
    
    # Create a generator that yields Chunks of data
    def iterfile():
        yield audio_output
        
    return StreamingResponse(iterfile(), media_type='audio/mpeg')

    
    
# # Post bot response
# @app.post('/post-audio/')
# async def post_audio(file:UploadFile = File(...)):
#     pass    
