import pickle
import pandas as pd
#from requirementsIdentifier import identifyRequirements
import commentGetter
import requests

def controversyKeywordsPrediction(video_id):
    predicted_dict = []
    comments = commentGetter.getComments(video_id) 
    for comment in comments:
        print(comment)
        api_url = "https://contraversy.onrender.com/predict"
        payload = {'text': comment}
        response = requests.post(api_url, json=payload)
        if response.status_code == 200:
            data = response.json()
            print(data)
            print("data")
            predicted_label = data['label']
            if predicted_label == 'Controversial':
                print('predicted comment')
                predicted_dict.append(comment)
    return predicted_dict


def controversyKeywordsSearch(video_id, search):
    comments_matching_keywords = []  # Use a list to store comments

    comments = commentGetter.getComments(video_id)
    
    if isinstance(search, str):
        keywords = search.split(',')  # Split the input search string by commas into a list of keywords
    else:
        # Handle the case where search is not a string (e.g., a list of keywords)
        keywords = search
    
    for comment in comments:
        comment_lower = comment.lower()
        for keyword in keywords:
            keyword_lower = keyword.strip().lower()  # Strip any leading/trailing spaces from keywords
            if keyword_lower in comment_lower:
                comments_matching_keywords.append(comment)  # Append the comment to the list

    print(comments_matching_keywords)
    return comments_matching_keywords









