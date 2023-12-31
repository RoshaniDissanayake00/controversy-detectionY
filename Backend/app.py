from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
#from dotenv import load_dotenv
import os
#from requirementsIdentifier import identifyRequirements
import controversyKeywords_controller 
import json
import requests
from fastapi import FastAPI, Query

app = FastAPI()

# # Load environment variables from .env file
# load_dotenv()

# # Access the API key
# api_key = os.getenv("USER_REQUIREMENTS_YOUTUBE_API_KEY")

# Set up CORS to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/controversyKeywords/')
async def controversyKeywords_prediction(video_id):
    predicted_comments = controversyKeywords_controller.controversyKeywordsPrediction(video_id)
    print(predicted_comments)
    print("ava")
    predicted_json = json.dumps(predicted_comments)
    obj = {
        'predictions':predicted_json,
    }
    return obj

@app.get('/controversyKeywordsSearch/')
async def controversyKeywordsSearch_prediction(
    video_id: str = Query(..., description="YouTube video ID"),
    search: str = Query(..., description="Search keywords (comma-separated)")
):
    keywords = search.split(",")  # Split the input search string by commas to get a list of keywords
    print(keywords)
    
    # Modify your controversyKeywordsSearch function to search comments for any of the keywords
    result_comments = controversyKeywords_controller.controversyKeywordsSearch(video_id, keywords)
    print(result_comments)
    
    predicted_json = json.dumps(result_comments)
    obj = {
        'predictions': predicted_json,
    }
    return obj

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='localhost', port=5000)











