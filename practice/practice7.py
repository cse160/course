## Name: ...
# CSE 160
# Spring 2026
# Programming Practice 7

from math import isclose
import matplotlib.pyplot as plt

# ! MAKE SURE TO SUBMIT BOTH practice7.py AND music_sales.png ON GRADESCOPE !

# In Problems 1 and 2, you will expand the functionality of the provided 'RestaurantTracker' class
# below. This class keeps track of the restaurants you visit, organized by city. Each instance of
# the RestaurantTracker class has an instance variable called restaurant_dict with city names as
# keys. Each key in the dictionary corresponds to a list of (restaurant, rating) tuples, storing
# the name and rating (0.0 to 5.0) of each restaurant in that city. The __init__ and add_restaurant
# methods have been implemented for you.

class RestaurauntTracker:
    def __init__(self):
        """
        Creates a new RestaurantTracker instance with an instance variable called restaurant_dict
        initialized to an empty dictionary.
        """
        self.restaurant_dict = {}

    def add_restaurant(self, city, restaurant, rating):
        """
        Adds a restaurant and its rating as a tuple to the list of tuples for the corresponding
        city in restaurant_dict.

        Arguments:
            city: a string corresponding to the name of the city
            restaurant: a string corresponding to the name of the restaurant
            rating: a float representing the restaurant's rating

        Returns: None.
        """
        if city not in self.restaurant_dict:
            self.restaurant_dict[city] = []
        self.restaurant_dict[city].append((restaurant, rating))

    # ~~~ Begin Problem 1 ~~~
    def restaurant_list(self):
        """
        Returns a list of all restaurant names in the RestaurantTracker instance in alphabetical
        order.

        Arguments:
            None.

        Returns: A list of restaurant name strings sorted alphabetically.
        """
        # Write your code for Problem 1 here!


    # ~~~ End Problem 1 ~~~

    # ~~~ Begin Problem 2 ~~~
    def restaurant_average(self, city):
        """
        Returns the average rating of all restaurants in the given city. You can assume that city
        will always be a valid city in the RestaurantTracker instance.

        Arguments:
            city: a string

        Returns: A float representing the average rating.
        """
        # Write your code for Problem 2 here!


    # ~~~ End Problem 2 ~~~


s = RestaurauntTracker()

s.add_restaurant("Edmonds", "Ono Poke", 4.92)
s.add_restaurant("Seattle", "Ramen Danbo", 4.73)
s.add_restaurant("Seattle", "Flour Box", 4.39)
s.add_restaurant("St. Louis", "Pickles Deli", 4.28)

# Test problem 1: restaurant_list
assert s.restaurant_list() == ["Flour Box", "Ono Poke",
                               "Pickles Deli", "Ramen Danbo"]

# Test problem 2: city_average
assert isclose(s.restaurant_average("Seattle"), 4.56)
assert isclose(s.restaurant_average("St. Louis"), 4.28)
assert isclose(s.restaurant_average("Edmonds"), 4.92)


# ~~~ Begin Problem 3 ~~~
# The following lists will be used for the function below.
# This list represents year values from 2000-2026.
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014,
         2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026]

# This list represents the physical item sales of music globally in billions of USD.
physical_sales = [23.5, 23.0, 21.5, 20.0, 18.5, 17.0, 15.5, 13.0, 10.5, 9.0, 7.5, 6.5, 5.5, 5.0,
                  4.5, 4.0, 3.8, 3.5, 3.5, 3.6, 3.7, 4.0, 4.2, 4.4, 4.6, 4.8, 5.0]

# This list represents the digital download sales of music globally in billions of USD.
digital_downloads = [0.0, 0.1, 0.3, 0.5, 1.2, 2.0, 3.1, 3.8, 4.5, 5.0, 5.2, 5.5, 5.6, 5.3, 4.8,
                     4.0, 3.2, 2.5, 1.8, 1.3, 0.9, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2]

# This list represents the streaming revenue of music globally in billions of USD.
streaming_revenue = [0.0, 0.0, 0.0, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.7, 1.0, 1.5, 2.2, 3.5, 5.0,
                     7.0, 9.5, 12.0, 14.5, 17.0, 19.5, 22.0, 24.5, 26.5, 28.5, 30.0, 31.5]


# Problem 3: Implement the 'music_sales' function below to plot and compare the trends global music
# sales. Make sure to take advantage of the import statement on line 7, which defines the variable
# `plt`.

# MAKE SURE TO SUBMIT BOTH 'practice8.py' AND 'music_sales.png' ON GRADESCOPE!
# The music_sales_expected.png file in the data folder illustrates what your plot should look
# like. You have to submit your own plot, though. You cannot use ours.

def music_sales(years, physical, digital, streaming):
    """
    Given four lists, one representing year values, and three representing sales values, return a
    line plot that layers each of the three distinct sales values on top of one another versus the
    provided years. Your line plot should represent the trends in music sales across the three
    provided mediums during the given years.

    Additionally,
    - Add a title: "Comparing global music sales from 2000-2026"
    - Label the x-axis: "Years"
    - Label the y-axis: "Sales in billions of USD"
    - Add a legend
    - Save the plot with the name "music_sales"

    Arguments:
        years: a list of integers representing year values to plot
        physical: a list of floats representing the physical sales each year
        digital: a list of floats representing the digital sales each year
        streaming: a list of floats representing the streaming sales each year

    Returns: None.
    """
    # Write your code for Problem 3 here!


# ~~~ End Problem 3 ~~~


music_sales(years, physical_sales, digital_downloads, streaming_revenue)
