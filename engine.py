from instagram.client import InstagramAPI
from secrets import INSTAGRAM_CODES
import json
import collections

client_id = INSTAGRAM_CODES["CLIENT_ID"]
client_secret = INSTAGRAM_CODES["CLIENT_SECRET"]
access_token = INSTAGRAM_CODES["ACCESS_TOKEN"]
client_ip = INSTAGRAM_CODES["CLIENT_IP"]
api = InstagramAPI(client_id=client_id, client_secret=client_secret, client_ips= client_ip,access_token= access_token) 

def get_insta_posts():
	data = api.tag_recent_media(tag_name='CapitalOne')
	return data[0]

#Post = collections.namedtuple("Post", "likes", "caption")

def get_media_info():
	return get_insta_posts()

