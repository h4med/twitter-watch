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
        'schedule': 60 * 5,
    },
    'sentiment_detection_task': {
        'task': 'scraping.tasks.sentiment_detection',
        'schedule': 60 * 7,
    }
}
```
Task1 is the Scraper which directly scrapes data from three accounts every 5 minutes and save the results in `db.sqlite`.   
Task2 is responsible for sentiment detection using OpenAI's `text-davinci-003` Model. It checks the databse every 7 minutes and if a tweet does note have sentiment (` == ''`) then detect and record it in DB.   
Both tasks are defined in `scraping\task.py`   

## Run
You can simply run the project using docker-compose:   
```
docker-compose up --build -d
```