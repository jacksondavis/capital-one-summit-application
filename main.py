from flask import Flask, flash, jsonify, render_template, redirect
from flask_bootstrap import Bootstrap
import os
import pprint
import json
import engine


app = Flask(__name__)

@app.route('/home')
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/posts")
def get_posts():
	posts = engine.get_insta_posts()
	sentiments = []
	for post in posts:
		sentiments.append(engine.get_caption_sentiment(post)["docSentiment"]["type"])
	print sentiments
	print json.dumps(sentiments)
	sentimentFreqs = engine.get_sentiment_frequencies(sentiments)
	print sentimentFreqs
	return render_template('posts.html', data = zip(posts, sentiments))

@app.route("/user/<id>")
def get_user(id):
	user = engine.get_user_info(id)
	print type(user.counts)
	print user.counts['media']
	return render_template('user.html', user=user)

@app.route('/test')
def test():
	engine.test_db()
	return 'hi'


@app.route("/analytics")
def get_analysis():
	posts = engine.get_insta_posts()
	sentiments = []
	for post in posts:
		sentiments.append(engine.get_caption_sentiment(post)["docSentiment"]["type"])
	sentimentFreqs = json.dumps(engine.get_sentiment_frequencies(sentiments))
	pp = pprint.PrettyPrinter(depth=6)
	print type(sentimentFreqs)
	pp.pprint(sentimentFreqs)
	return render_template('analysis.html', data = sentimentFreqs)

if __name__ == "__main__":
    app.run()