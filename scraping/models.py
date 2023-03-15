from django.db import models

class Tweet(models.Model):
    publish_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    tweet_id = models.PositiveBigIntegerField(unique=True)
    user_name = models.CharField(max_length=256)
    image_url = models.CharField(max_length=256, default="")
    video_url = models.CharField(max_length=256, default="")
    text = models.TextField(max_length=4000)
    handle = models.CharField(max_length=16)
    likes = models.CharField(max_length=16)
    retweets = models.CharField(max_length=16)
    replies = models.CharField(max_length=16)
    views = models.CharField(max_length=16)
    sentiment = models.CharField(max_length=256, default="")

class Meta:
    ordering = ['-publish_date']

def __str__(self):
    return self.url




