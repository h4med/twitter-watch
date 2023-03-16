from rest_framework import serializers
from .models import Tweet

class TweetDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        # fields = '__all__'
        fields = (
            'handle',            
            'publish_date',
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
            'handle',            
            'publish_date',
            'text',
            'sentiment',
            'created_at',
            'tweet_id',
        )

class TweetDetailSerializer(serializers.ModelSerializer):
    tweet_url = serializers.SerializerMethodField()

    class Meta:
        model = Tweet
        # fields = '__all__'
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
        url = "https://twitter.com/"+obj.handle[1:]+"/status/"+obj.tweet_id
        return url