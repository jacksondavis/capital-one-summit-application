from flask import Flask, flash, jsonify, render_template, redirect
from flask_bootstrap import Bootstrap
import engine

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/posts")
def get_posts():
    return engine.get_media_info()

if __name__ == "__main__":
    app.run()