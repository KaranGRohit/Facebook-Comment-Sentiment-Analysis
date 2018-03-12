# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 15:44:49 2018

@author: UTSHA DAS
"""
from textblob import TextBlob

import json

with open('comment_data.json') as data_file:
    data = json.load(data_file)

sentiment_list = []
Total_comment=0
positive_comment=0
negative_comment=0
neutral_comment=0

for x1,y1  in data['comment'].items():
    try:
        Total_comment+=1
        sentence=TextBlob(y1)
        #print(sentence.sentiment.polarity)
        if sentence.sentiment.polarity>0:
            positive_comment+=1
        elif sentence.sentiment.polarity<0:
            negative_comment+=1
        else:
            neutral_comment+=1
        sentiment_list.append({"id": x1, "comment": y1, "sentiment_score": sentence.sentiment.polarity })
        #print ("Pass")
        
    except:
        print ("Fail")
print("Positive Comment: ",float(positive_comment/Total_comment)*100,"%")
print("Negative Comment: ",float(negative_comment/Total_comment)*100,"%")
print("Neutral Comment: ",float(neutral_comment/Total_comment)*100,"%")

with open('sentiment_comments.json', 'w') as outfile:
    json.dump(sentiment_list, outfile)