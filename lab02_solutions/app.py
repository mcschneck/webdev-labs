from flask import Flask
from flask import render_template
import random
import requests
from helpers import CurrentUser
import json
from pprint import pprint

# initializes flask app:
app = Flask(__name__)

#########################
# some global variables #
#########################
current_user = CurrentUser(first_name='Erick', last_name='Rubi', email='erub03@gmail.com', username='erub03')

quotes = [
    '“We May Encounter Many Defeats But We Must Not Be Defeated.” – Maya Angelou',
    '“The Way Get Started Is To Quit Talking And Begin Doing.” – Walt Disney',
    '“Security Is Mostly A Superstition. Life Is Either A Daring Adventure Or Nothing.” – Life Quote By Helen Keller',
    '“The Pessimist Sees Difficulty In Every Opportunity. The Optimist Sees Opportunity In Every Difficulty.” – Winston Churchill',
    '“Don’t Let Yesterday Take Up Too Much Of Today.” – Will Rogers',
    '“You Learn More From Failure Than From Success. Don’t Let It Stop You. Failure Builds Character.” – Unknown',
    '“If You Are Working On Something That You Really Care About, You Don’t Have To Be Pushed. The Vision Pulls You.” – Steve Jobs',
]

##############
# Exercise 1 #
##############
@app.route('/')
def exercise1():
    return 'Hi, ' + current_user.get_full_name() + '!'


##############
# Exercise 2 #
##############
@app.route('/quote')
def exercise2():
    return render_template(
        'quote-of-the-day.html',
        user=current_user,
        quote=random.choice(quotes)
    )

##############
# Exercise 3 #
##############
@app.route('/restaurant-data/<city>/<search_term>')
@app.route('/restaurant-data/<city>')
@app.route('/restaurant-data')
def exercise3(city='Evanston, IL', search_term=''):
    url = 'https://www.apitutor.org/yelp/simple/v3/businesses/search?location={0}&term={1}'.format(city, search_term)
    response = requests.get(url)
    data = response.json()
    return json.dumps(data)

##############
# Exercise 4 #
##############
@app.route('/restaurant/<city>/<search_term>')
@app.route('/restaurant/<city>')
@app.route('/restaurant')
def exercise4(city='Evanston, IL', search_term=''):
    url = 'https://www.apitutor.org/yelp/simple/v3/businesses/search?location={0}&term={1}'.format(city, search_term)
    response = requests.get(url)
    restaurants = response.json()
    pprint(restaurants[0]) # for debugging
    return render_template(
        'restaurant.html',
        user=current_user,
        search_term=search_term,
        city=city,
        restaurant=restaurants[0]
    )

@app.route('/restaurants/<city>/<search_term>')
@app.route('/restaurants/<city>')
@app.route('/restaurants')
def exercise5(city='Evanston, IL', search_term=''):
    url = 'https://www.apitutor.org/yelp/simple/v3/businesses/search?location={0}&term={1}'.format(city, search_term)
    response = requests.get(url)
    restaurants = response.json()
    pprint(restaurants) # for debugging
    return render_template(
        'restaurants.html',
        user=current_user,
        search_term=search_term,
        city=city,
        restaurants=restaurants
    )


    
