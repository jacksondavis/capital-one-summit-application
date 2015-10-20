from flask import Flask, flash, jsonify, render_template, redirect
from flask_bootstrap import Bootstrap
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
	return render_template('posts.html', data = zip(posts, sentiments))

@app.route("/user/<id>")
def get_user(id):
	user = engine.get_user_info(id)
	print type(user.counts)
	print user.counts['media']
	return render_template('user.html', user=user)

if __name__ == "__main__":
    app.run()