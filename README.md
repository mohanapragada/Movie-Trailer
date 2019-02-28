# Movie-Trailer
TITLE : Movie Trailer Website 
AUTHOR : Mohana Pragada
PYTHON VERSION : Python 3.5
PROJECT : A python file generating a html web page
CODE CHECKER: PEP8

Description: A server-side code that stores a list of movies, including box art, imagery, a movie trailer URL, and serve this data as web page; allowing visitors to review their movies and watch trailers.

In this readme file, I explain in detail how our website; fresh_tomatoes.py functions with media.py and entertainment.py to display movie title, poster_image, and trailer. I later on explained how i reconfigured the fresh_tomatoes.py file to include Moive_reviews, and a "About Udacity" link to Udacity website. Finally, i explained how to run this program.

PLAN
Programming Foundations with Python

We started off with a plan:

Go to the website
See all of the movies displayed
Click on one to play it's trailer
It's pretty simple in terms of concept, but how about implementation?

Class structure

We will need classes to build this movie website. We want our Movie class to be a template for a generic movie, and then create instances of that class like this:

love_and_basketball = Movie()

and add details to each specific movie. So, we first need to come up with a list of properties that we think every movie should have:

title
trailer
storyline
poster_image
reviews
