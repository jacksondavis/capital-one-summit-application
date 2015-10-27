from instagram.client import InstagramAPI
from secrets import INSTAGRAM_CODES
from alchemyapi import AlchemyAPI
from collections import defaultdict
import json
import collections
import os
import psycopg2
import urlparse

client_id = INSTAGRAM_CODES["CLIENT_ID"]
client_secret = INSTAGRAM_CODES["CLIENT_SECRET"]
access_token = INSTAGRAM_CODES["ACCESS_TOKEN"]
client_ip = INSTAGRAM_CODES["CLIENT_IP"]
api = InstagramAPI(client_id=client_id, client_secret=client_secret, client_ips= client_ip,access_token= access_token) 
alchemyapi = AlchemyAPI()

def get_insta_posts():
	data = api.tag_recent_media(tag_name='CapitalOne')
	return data[0]

def get_user_info(id):
	user = api.user(id)
	return user

def get_caption_sentiment(post):
	caption = post.caption
	response = alchemyapi.sentiment("text", caption)
	return response

def get_sentiment_frequencies(sentiments):
	freqs = defaultdict(int)
	for sentiment in sentiments:
		freqs[sentiment] += 1
	return freqs

def test_db():	

	urlparse.uses_netloc.append("postgres")
	url = urlparse.urlparse(os.environ["DATABASE_URL"])

	conn = psycopg2.connect(
	    database=url.path[1:],
	    user=url.username,
	    password=url.password,
	    host=url.hostname,
	    port=url.port
	)

	cur = conn.cursor()
	cur.execute("""SELECT * from insta_posts""")
