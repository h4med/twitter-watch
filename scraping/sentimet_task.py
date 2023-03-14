from celery import shared_task
from .models import Tweet

import openai

openai.api_key = "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"

@shared_task
def sentiment_detection():
    print('_____________ sentimetn_detection is Running _____________')
    queryset = Tweet.objects.all()
    cntr = 0
    for tweet in queryset:
        print(tweet.tweet_id)
        cntr += 1
        if cntr == 5:
            break