from rest_framework import serializers
from .models import Tweet

class TweetListSerializer(serializers.ModelSerializer):
    tweet_url = serializers.SerializerMethodField()
    class Meta:
        model = Tweet
        fields = (
            'handle',            
            'publish_date',
            'text',
            'sentiment',
            'created_at',
            'tweet_id',
            'tweet_url',
        )

    def get_tweet_url(self, obj):
        url = "https://twitter.com/"+obj.handle[1:]+"/status/"+str(obj.tweet_id)
        return url        

class TweetDetailSerializer(serializers.ModelSerializer):
    tweet_url = serializers.SerializerMethodField()

    class Meta:
        model = Tweet
        fields = (
            'handle',            
            'publish_date',
            'text',
            'sentiment',
            'tweet_url',
            'image_url',
            'video_url',
            'created_at',
            'tweet_id',
            'likes',
            'retweets',
            'replies',
            'views',
        )
    
    def get_tweet_url(self, obj):
        url = "https://twitter.com/"+obj.handle[1:]+"/status/"+str(obj.tweet_id)
        return url