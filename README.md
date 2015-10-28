## Capital One Summit for Software Engineers Submissions ##

[https://summit-application.herokuapp.com/](https://summit-application.herokuapp.com/)

This repository contains my submisison for [Capital One's Summit for Software Engineers](https://campus.capitalone.com/campus-events). As part of the final round application for this program, applicants were instructed to complete a [coding challenge](https://www.mindsumo.com/contests/meerkat-api) in which data tagged with #CapitalOne on Instagram would be pulled and analyzed.

In order to complete this challenge, I decided to use the Python Flask framework and create a web application to visualize all the necessary data. The Flask application makes use of several dependencies, including: 
* [AlchemyAPI](http://www.alchemyapi.com/) for sentiment analysis,
* [InstagramAPI](https://instagram.com/developer/) for gathering post data,
* [Bootstrap](http://getbootstrap.com/) for front-end simplification, and
* [d3.js](http://d3js.org/)

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
`secrets.py` holds as many [AlchemyAPI keys](http://www.alchemyapi.com/api/register.html) as you want to use, and one [InstgramAPI key](https://instagram.com/developer/) in order to access the necessary API's in the application. 
4. Finally, type `python main.py` in order to host the application locally.

## Author ## 
This application was created by Jackson Davis. If you have any questions or suggestions for improvement, feel free to email me at jaxtdavis@gmail.com.
