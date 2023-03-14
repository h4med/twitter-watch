from rest_framework import serializers
from .models import Tweet

class TweetDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        # fields = '__all__'
        fields = (
            'publish_date',            
            'user_name',
            'handle',
            'text',
            'sentiment',
            'image_url',
            'video_url',
            'created_at',
            'tweet_id',
            'likes',
            'retweets',
            'replies',
            'views',
        )

class TweetListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        # fields = '__all__'
        fields = (
            'publish_date',
            'user_name',
            'handle',
            'text',
            'sentiment',
            'created_at',
            'tweet_id',
        )