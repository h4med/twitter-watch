# scraping/views.py

from rest_framework import generics
from .models import Tweet
from .serializers import TweetDetailSerializer, TweetListSerializer

class TweetsList(generics.ListAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetListSerializer

    
class TweetsByAccountList(generics.ListAPIView):
    serializer_class = TweetListSerializer

    def get_queryset(self):
        account = self.kwargs['account']
        return Tweet.objects.filter(handle=account)
    
class TweetByAccountDetail(generics.ListAPIView):
    serializer_class = TweetDetailSerializer

    def get_queryset(self):
        account = self.kwargs['account']
        id = self.kwargs['tweet_id']
        return Tweet.objects.filter(handle=account,tweet_id=id)