headers = {'Authorization': 'Bearer AAAAAA**B' }


from django.http import HttpResponse, JsonResponse
import requests
import datetime
import json
from django.shortcuts import render



def getRecentTweets(category):
    current = datetime.datetime.utcnow()
    span = datetime.timedelta(minutes=5)
    recent = current - span
    # print();
    payload = {
        'query': str(category), 
        'max_results': 50, 
        'start_time': recent.strftime('%Y-%m-%dT%H:%M:%S.000Z'),
        "expansions": "author_id",
        'user.fields': 'name,username,public_metrics'
    }
    tweets = requests.get("https://api.twitter.com/2/tweets/search/recent", headers=headers, params=payload)
    # print(tweets)
    
    #data = tweets.json()["data"]
    print(tweets.json())
    # text_data = []
    # for i in range(len(data)):
    #     text = data[i]["text"]
    #     text_data.append(text)
    return getRecentTweets(tweets.json())
getRecentTweets('sports')
