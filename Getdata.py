# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 15:40:01 2018

@author: UTSHA DAS
"""

import requests 
import pandas as pd
import os
token="EAACEdEose0cBABXBRIgtpp6CFjGZBc8SN9SSZAtCda7UyJKSDTYbGpD7yPZA5ZAOmMIpPvPGuiabA2ctQg1z8rYTQMdsD95tN35IZCL2izrajUGWCqg5R79jBx8bQOdYzIMUXALh1fmRnVSdQz6OhHVUMB2rNO8xSFDkViug2ZC8qIQKzo4UhIV1l0E1RV4A8cqmTwODRftWN2mQUW0siheh211ZCGnwa7wUfb5hw4kcy8keApH0NWb"
try:
    token = os.environ['FB_TOKEN']
except:
    print ("Set FB_TOKEN variable")
    #sys.exit(-1)
    exit

#fb_pageid = "228735667216"
fb_pageid="153080620724"
#fb_postid = "10154922624762217"
fb_postid="10160602131430725"
commentlst = []
datelst = []

url = "https://graph.facebook.com/v2.12/"+ fb_pageid +"_"+ fb_postid +"/comments?limit=100&access_token="+token

while(True):
    posts = requests.get(url)
    posts_json = posts.json()
    for x1 in posts_json['data']:
        commentlst.append(x1.get('message').encode('utf-8').strip())
        datelst.append(x1.get('created_time'))
    next_page = ""
    try:
        next_page = posts_json['paging']['next']
        url = next_page
    except:
        break
    if not next_page: break
    print ("Count: %s,  Next Page: %s" % ( len(commentlst), url))

print ("\nGenerating JSON File")

df = pd.DataFrame({'comment': commentlst, 'dates': datelst})
df['dates'] = pd.to_datetime(df['dates'])
df['day_of_week'] = df['dates'].dt.weekday_name
df['year'] = df['dates'].dt.year
df['month'] = df['dates'].dt.month
df['count'] = 1 

df.to_json('comment_data.json')