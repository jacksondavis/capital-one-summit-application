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

#I debated using a database to hold the sentiments and data for each post,
#However after running into issues with Heroku's PostgreSQL integration
#And realizing the issues the actual database use would be light,
#I opted to simply create a dictionary.
post_data = {}

def get_insta_posts():
	data = api.tag_recent_media(tag_name='CapitalOne')
	return data[0]

def get_user_info(id):
	user = api.user(id)
	return user

def get_caption_sentiment(post):
	response = ""
	caption = post.caption
	if post.link in post_data:
		response = post_data[post.link]
	else:
		response = alchemyapi.sentiment("text", caption)
    	post_data[post.link] = response

	return response

def get_sentiment_frequencies(sentiments):
	freqs = defaultdict(int)
	for sentiment in sentiments:
		freqs[sentiment] += 1
	return freqs