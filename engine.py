from instagram.client import InstagramAPI

client_id = secrets.INSTAGRAM_CODES[0]
client_secret = secrets.INSTAGRAM_CODES[1]
access_token = secrets.INSTAGRAM_CODES[2]
client_ip = secrets.INSTAGRAM_CODES[3]
api = InstagramAPI(client_id=client_id, client_secret=client_secret,client_ips= client_ip,access_token= access_token)