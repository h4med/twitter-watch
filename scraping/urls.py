# scraping/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from scraping import views


urlpatterns = [
    path("tweets/", views.TweetsList.as_view()),
    path("tweets/<account>", views.TweetsByAccountList.as_view()),
    path("tweets/<account>/<tweet_id>", views.TweetByAccountDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)