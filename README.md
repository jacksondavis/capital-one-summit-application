## Capital One Summit for Software Engineers Submissions ##

[https://summit-application.herokuapp.com/](https://summit-application.herokuapp.com/)

This repository contains my submisison for [Capital One's Summit for Software Engineers](https://campus.capitalone.com/campus-events). As part of the final round application for this program, applicants were instructed to complete a [coding challenge](https://www.mindsumo.com/contests/meerkat-api) in which data tagged with #CapitalOne on Instagram would be pulled and analyzed.

In order to complete this challenge, I decided to use the Python Flask framework and create a web application to visualize all the necessary data. The Flask application makes use of several dependencies, including: 
* [AlchemyAPI](http://www.alchemyapi.com/) for sentiment analysis,
* [InstagramAPI](https://instagram.com/developer/) for gathering post data,
* [Bootstrap](http://getbootstrap.com/) for front-end simplification, and
* [d3.js](http://d3js.org/)

## Design and Reasoning ##
I am relatively new to both Python, Flask, and web applications in general, and because of this I had to make many design decisions regarding problems I had never faced before. The following is the basic flow of operation for the application and some explanation as to why I chose to do this:

* **Instagram Photos:**

   The Python-Instagram wrapper was used to pull photos from the InstagramAPI. Calling the `/posts` route runs a function which returns the 20 most recent posts tagged with #CapitalOne, renders the `posts.html` template and passes the list of 20 posts to be displayed on the site. For each post, the InstagramAPI let's us simply call `post.like_count`, `post.caption`, or a number of other methods in order to retrieve the necessary information. I also set up a `/user` route which takes the userID for a post and runs a separate InstagramAPI call to retrieve that user's information. It was at this point that I had to determine when I wanted to run AlchemyAPI in order to retrieve the post caption's sentiment values which leads me to the next design choice.
* **Sentiment Analysis:**
	
	The Capital One Challenge requirements stated that we must analyze the sentiment for each post, which quickly lead to me to using AlchemyAPI, an IBM API used for Natural Language Processing. I set up a function which runs AlchemyAPI on a single post's caption and returns the sentiment type, "Positive", "Negative", or "Neutral". During the call to `/posts`, I send each post from the list of 20 into the method, and compile these values into a list to be displayed. While this worked well, and allowed me to get a sentiment returned for each post, I quickly discovered that this process was time intensive, and furthermore, by running AlchemyAPI 20 times per visit to `/post`, the 1,000 daily transactions allowed on the Free version of AlchemyAPI were all used extremely quickly. I was able to determine a solution which fixed multiple issues I was having.
* **Post_data Dictionary vs Database:** 

	I determined that the best solution to the long sentiment loading times and quick use of my 1,000 AlchemyAPI transactions would be to only run the AlchemyAPI analysis if it had not been done before for a post. I knew that I would eventually be using Heroku to host my project, so I decided to try a Heroku Postgres database, however I quickly ran into issues with local testing as well as frequent app crashes. This led me to my most questionable design decision, using a Python dictionary over a Postgres database. While there are many benefits to using a database, I concluded that as I only needed to store an image identifier and its sentiment per post, Postgres would be overkill. I decided to set up the **post_data** dictionary in `engine.py`, which would use the instagram post url as a unique key, and store the sentiment as its value. This allowed me to do two major things. First, I only need to run AlchemyAPI if a post and its sentiment did not already exist in the dictionary, in which case I would pull the value locally. And second, I now had a way to store more than 20 posts, which was beneficial for my data visualization.
* **d3.js:**

	The last step in this project was visualizing the sentiment data I retrieved in a meaningful way. This portion of the challenge was the most difficult for me, as I am extremely knew to javascript and **d3.js**. After writing a method to calculate the frequencies of "positive", "negative", and "neutral" sentiments in **post_data**, I decided to visualize these values in a pie-chart made with **d3.js**.  I ran into a lot of problems finding the best and easiest way to get my Python frequency dictionary into a form easy to graph with **d3.js**. After finally determining a way to turn my dictionary into an easily accesible Javascript Object, I read [this tutorial](http://bl.ocks.org/mbostock/3887235) on how to graph my values into a pie chart. These are the main components of this application, and as I am knew to a lot of this, feel free to reach out with suggestions of areas in which I could improve.

## Installation ##
There is a currently a live link to this application [here](https://summit-application.herokuapp.com/), however this application can be run locally by doing the following on Linux or Mac:

1. Clone this repository.
2. Install pip and virtualenv, activate your virtualenv, and run the command `pip install -r  requirements.txt` to install dependencies.
3. Create a Python file called `secrets.py` which is structured as follows:

	```python
	ALCHEMY_CODES = [
		'[API Key from AlchemyAPI Website]',
	    '[Optional API Key from AlchemyAPI Website]',
	    '[Optional API Key from AlchemyAPI Website]'
	]

	INSTAGRAM_CODES = {
			'CLIENT_ID': '[Your ID from InstagramAPI Website]',
			'CLIENT_SECRET': '[Your Secret from InstagramAPI Website]',
			'ACCESS_TOKEN': '[Your Token from InstagramAPI Website]',
			'CLIENT_IP': '[Your Client_IP from InstagramAPI Website]'
	}
	```
	`secrets.py` holds as many [AlchemyAPI keys](http://www.alchemyapi.com/api/register.html) as you want to use, 		and one [InstgramAPI key](https://instagram.com/developer/) in order to access the necessary API's in the application. 
4. Finally, type `python main.py` in order to host the application locally.

## Author ## 
This application was created by Jackson Davis. If you have any questions or suggestions for improvement, feel free to email me at jaxtdavis@gmail.com.