from flask import Flask, flash, jsonify, render_template, redirect
from flask_bootstrap import Bootstrap
import os
import pprint
import json
import engine

app = Flask(__name__)

# Home Page
@app.route('/home')
@app.route('/')
def index():
    return render_template('index.html')

# Retrieves posts and runs sentiment analysis
@app.route("/posts")
def get_posts():
	posts = engine.get_insta_posts()
	sentiments = []
	for post in posts:
		sentiments.append(engine.get_caption_sentiment(post))
	return render_template('posts.html', data=zip(posts, sentiments))

# Retrieves user information
@app.route("/user/<id>")
def get_user(id):
	user = engine.get_user_info(id)
	print type(user.counts)
	print user.counts['media']
	return render_template('user.html', user=user)

# Charts sentiment frequencies
@app.route("/analysis")
def get_analysis():
	sentData = engine.get_sentiment_frequencies()
	sentimentFreqs = sentData[0]
	total = sentData[1]
	jsonData = json.dumps(sentimentFreqs)
	print jsonData
	return render_template('analysis.html', data=jsonData, total=total)

if __name__ == "__main__":
    app.run()