# scraping/views.py

from rest_framework import generics
from .models import Tweet
from .serializers import TweetDetailSerializer, TweetListSerializer, TweetDetailSerializerWithURL

class TweetsList(generics.ListAPIView):
    queryset = Tweet.objects.all().order_by('-publish_date')
    serializer_class = TweetListSerializer

    
class TweetsByAccountList(generics.ListAPIView):
    serializer_class = TweetListSerializer

    def get_queryset(self):
        account = self.kwargs['account']
        return Tweet.objects.filter(handle=account).order_by('-publish_date')
    
class TweetByAccountDetail(generics.ListAPIView):
    # serializer_class = TweetDetailSerializer
    serializer_class = TweetDetailSerializerWithURL

    def get_queryset(self):
        account = self.kwargs['account']
        id = self.kwargs['tweet_id']
        return Tweet.objects.filter(handle=account,tweet_id=id)