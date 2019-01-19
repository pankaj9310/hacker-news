import requests
import datetime
from news.models import News

def get_list():
	try:
		return requests.get('https://hacker-news.firebaseio.com/v0/topstories.json').json()
	except Exception as e:
		raise e

def get_item(id):
	try:
		return requests.get('https://hacker-news.firebaseio.com/v0/item/'+str(id)+'.json').json()
	except Exception as e:
		raise e


def get_sentiment(title):
	title = '+'.join(title.split())
	return requests.get("https://twinword-sentiment-analysis.p.rapidapi.com/analyze/?text="+title, headers={"X-RapidAPI-Key": "8d2851a147msh8d0f37e19e73346p15153ejsn5e44003eba62"}).json()

def save_news():
	data = get_list()
	news = News.objects.last()
	last_news_id = 0
	if news is not None:
		last_news_id = news.hacker_news_id
	data.sort()
	for item in data:
		if item > last_news_id:
			story = get_item(item)
			sentiment_score = 0.0
			sentiment = get_sentiment(story.get('title'))
			if sentiment is not None:
				sentiment_score = sentiment['score']
			if story is not None:
				try:
					obj = News(hacker_news_id= item, username= str(story.get('by')), title= str(story.get('title')), url= str(story.get('url')), upvote= str(story.get('score')), story_type= str(story.get('type')), description= "",  sentiment_score= sentiment_score, posted_at= datetime.datetime.fromtimestamp(story.get('time')))
					obj.save()
				except Exception as e:
					raise e