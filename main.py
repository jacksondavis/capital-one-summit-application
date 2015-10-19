from flask import Flask, flash, jsonify, render_template, redirect
from flask_bootstrap import Bootstrap
import engine

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route("/posts")
def get_posts():
	posts = engine.get_insta_posts()
	print posts[0].id
	return render_template('posts.html', posts=posts)

if __name__ == "__main__":
    app.run()