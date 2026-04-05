"""
* Name:
* Date:
* CSE 160
* Homework 5
* Description:
"""

import csv  # noqa: F401
import matplotlib.pyplot as plt  # noqa: F401
from numpy.polynomial import polynomial as poly  # noqa: F401
from utils import (min_year, max_year)  # noqa: F401


class Country():

    # Problem 1a
    def __init__(self, name, start_year, end_year):
        # Write your doc-string above, remove pass and write your code below

        self.years = list(range(start_year, end_year + 1))

    # Problem 1b
    def update_data(self, row):
        # Write your doc-string above, remove pass and write your code below
        pass

    # Problem 1c
    def get_actual_production(self, year):
        # Write your doc-string above, remove pass and write your code below
        pass

    # Problem 1d
    def get_production_need(self, year):
        # Write your doc-string above, remove pass and write your code below
        pass

    # Problem 1e
    def calculate(self):
        # Write your doc-string above, remove pass and write your code below
        pass

    # Problem 3
    def plot_production_vs_need(self):
        # Write your doc-string above, remove pass and write your code below
        pass

    def predict_need(self, predict_years):
        """
        Given a number of years to predict in the future, produces a dictionary
        containing the following keys.

            years: a list of years from the first year to the last predicted
            year
            values: a list of the predicted needs at each given year.

        For example calling:
        predict_need(data, "AMP", 5)

        will produce:
        {'years': [1961, 1962, 1963, 1964, 1965, 1966],
         'values': [10380.76, 10383.41, 10386.06, 10388.70, 10391.35,
                    10394.00]}
        """
        years = []
        needs = []
        for year in self.need:
            if self.need[year] is not None:
                years.append(year)
                needs.append(self.need[year])
        b, m = poly.polyfit(years, needs, 1)
        p_years = []
        p_need = []
        for year in range(self.years[0], self.years[-1] + predict_years + 1):
            p_years.append(year)
            p_need.append(m * year + b)
        return {"years": p_years, "values": p_need}


class Fishing():

    # Problem 2a
    def __init__(self, filename):
        """
        Takes in a .csv filename and initializes an empty dictionary. Hint:
        call parse_data() to populate that dictionary with Country objects.
        """
        # Remove pass and write your code here
        pass
        # Uncomment the following line of code once you write this method
        # self.parse_data(raw_data)

    # Problem 2b
    def parse_data(self, raw_data):
        # Write your doc-string above, remove pass and write your code below
        pass

    # Problem 2c
    def total_production_need(self, years_to_predict):
        # Write your doc-string above, remove pass and write your code below
        pass
