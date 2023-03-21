# twitter-watch
A twitter scraper using Django, Celery and Playwright.  
This has been written for a Job Enterance competition.  

## How it Works
This is the block diagram of system:   
![Twitter watcher block diagram](https://github.com/h4med/twitter-watch/blob/main/Docs/twatch_bd.png)   
   
### This is how the application works
Task1 and Task2 are the core of application. We configure these tasks in `twitterwatch\settings.py` as follows:
```
CELERY_BEAT_SCHEDULE = {
    'scraping_task': {
        'task': 'scraping.tasks.scraping_method',
        'schedule': 60 * 15,
    },
    'sentiment_detection_task': {
        'task': 'scraping.tasks.sentiment_detection',
        'schedule': 60 * 17,
    }
}
```
Task1 is the Scraper which directly scrapes data from three accounts every 15 minutes and save the results in `db.sqlite`.   
Task2 is responsible for sentiment detection using OpenAI's `text-davinci-003` model. It checks the database every 17 minutes and if a tweet does note have a sentiment in DB (` == ''`) then detects vi API and records it in the DB.   
Both tasks are defined in `scraping\tasks.py`   

## Run
You can simply run the project using docker-compose:   
```
docker-compose up --build -d
```
And head over to **url:8000/tweets** to see the results in JSON format.   
**url:8000/tweets/@handle** returns the tweets for every account and    
**url:8000/tweets/@handle/id** is for each tweet with details such as "likes", "retweets" and etc.   
```
[
    {
        "handle": "@elonmusk",
        "publish_date": "2023-03-16T17:10:48Z",
        "text": "You’re terrible & I love you",
        "sentiment": "Mixed sentiment.",
        "tweet_url": "https://twitter.com/elonmusk/status/1636414725549592576",
        "image_url": "",
        "video_url": "",
        "created_at": "2023-03-16T17:15:13.182073Z",
        "tweet_id": 1636414725549592576,
        "likes": "8,441",
        "retweets": "1,369",
        "replies": "2,120",
        "views": "274360"
    }
]
```

