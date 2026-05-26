# Name: ...
# CSE 160
# Spring 2026
# Fishing Analysis

import csv
import matplotlib.pyplot as plt
from numpy import polyfit
import os


class Country():

    def __init__(self, name, start_year, end_year):
        """


        >>> country = Country("Testland", 2010, 2012)
        >>> country.name
        'Testland'
        >>> country.years
        [2010, 2011, 2012]
        >>> country.farmed
        {2010: None, 2011: None, 2012: None}
        >>> country.wild_caught
        {2010: None, 2011: None, 2012: None}
        >>> country.consumption
        {2010: None, 2011: None, 2012: None}
        >>> country.population
        {2010: None, 2011: None, 2012: None}
        >>> country.production
        {2010: None, 2011: None, 2012: None}
        >>> country.need
        {2010: None, 2011: None, 2012: None}
        """
        self.years = list(range(start_year, end_year + 1))
        pass  # REMOVE THIS LINE AND REPLACE IT WITH YOUR CODE ...

    def update_data(self, row):
        """


        >>> country = Country("Testland", 2010, 2012)

        >>> row = {"measure": "farmed", "2010": "1000", "2011": "1500", "2012": ""}
        >>> country.update_data(row)
        >>> country.farmed
        {2010: 1000.0, 2011: 1500.0, 2012: None}

        >>> row["measure"] = "wild caught"
        >>> country.update_data(row)
        >>> country.wild_caught
        {2010: 1000.0, 2011: 1500.0, 2012: None}

        >>> row["measure"] = "consumption"
        >>> country.update_data(row)
        >>> country.consumption
        {2010: 1000.0, 2011: 1500.0, 2012: None}

        >>> row["measure"] = "population"
        >>> country.update_data(row)
        >>> country.population
        {2010: 1000.0, 2011: 1500.0, 2012: None}
        """
        pass  # REMOVE THIS LINE AND REPLACE IT WITH YOUR CODE ...

    def calc_actual_production(self, year):
        """


        >>> country = Country("Testland", 2010, 2012)
        >>> country.farmed = {2010: 1000.0, 2011: None, 2012: 2000.0}
        >>> country.wild_caught = {2010: 500.0, 2011: 300.0, 2012: None}
        >>> country.calc_actual_production(2010)
        >>> country.production[2010]
        1500.0
        >>> country.calc_actual_production(2011)
        >>> country.production[2011]
        300.0
        >>> country.calc_actual_production(2012)
        >>> country.production[2012]
        2000.0
        """
        pass  # REMOVE THIS LINE AND REPLACE IT WITH YOUR CODE ...

    def calc_production_need(self, year):
        """


        >>> country = Country("Testland", 2010, 2012)
        >>> country.population = {2010: 1000000.0, 2011: None, 2012: 2000000.0}
        >>> country.consumption = {2010: 10.0, 2011: 15.0, 2012: None}
        >>> country.calc_production_need(2010)
        >>> country.need[2010]
        10000.0
        >>> country.calc_production_need(2011)
        >>> country.need[2011]
        >>> country.calc_production_need(2012)
        >>> country.need[2012]
        """
        pass  # REMOVE THIS LINE AND REPLACE IT WITH YOUR CODE ...

    def calculate(self):
        """


        >>> country = Country("Testland", 2010, 2012)
        >>> country.farmed = {2010: 1000.0, 2011: 1500.0, 2012: None}
        >>> country.wild_caught = {2010: 500.0, 2011: None, 2012: 200.0}
        >>> country.consumption = {2010: 10.0, 2011: 15.0, 2012: None}
        >>> country.population = {2010: 1000000.0, 2011: None, 2012: 2000000.0}
        >>> country.calculate()
        >>> country.production
        {2010: 1500.0, 2011: 1500.0, 2012: 200.0}
        >>> country.need
        {2010: 10000.0, 2011: None, 2012: None}
        """
        pass  # REMOVE THIS LINE AND REPLACE IT WITH YOUR CODE ...

    def plot_production_vs_need(self):
        # Don't forget to write a docstring!
        pass  # REMOVE THIS LINE AND REPLACE IT WITH YOUR CODE ...

    def predict_need(self, predict_years):
        """
        Given a number of years to predict in the future, returns a 2-tuple of a list of years from
        the latest year to the given number of years in the future and a list of predicted needs
        for each year.
        """
        years = []
        needs = []
        for year in self.need:
            if self.need[year] is not None:
                years.append(year)
                needs.append(self.need[year])
        m, b = polyfit(years, needs, 1)
        p_years = []
        p_need = []
        for year in range(self.years[0], self.years[-1] + predict_years + 1):
            p_years.append(year)
            p_need.append(m * year + b)
        return p_years, p_need


class Fishing():

    def __init__(self, filename):
        """


        >>> data = Fishing("small.csv")
        >>> data.min_year
        1995
        >>> data.max_year
        2000
        >>> list(data.countries)
        ['CAN', 'MEX', 'USA']
        >>> isinstance(data.countries["CAN"], Country)
        True
        >>> isinstance(data.countries["MEX"], Country)
        True
        >>> isinstance(data.countries["USA"], Country)
        True
        """
        with open(filename) as f:
            reader = csv.DictReader(f)
            self.min_year = min(int(k) for k in reader.fieldnames if k.isnumeric())
            self.max_year = max(int(k) for k in reader.fieldnames if k.isnumeric())
            pass  # REMOVE THIS LINE AND REPLACE IT WITH YOUR CODE ...

    def total_production_need(self, years_to_predict):
        """


        >>> data = Fishing("small.csv")
        >>> data.total_production_need(50)  # doctest: +ELLIPSIS
        13243690.762...
        """
        pass  # REMOVE THIS LINE AND REPLACE IT WITH YOUR CODE ...


def plot_linear_prediction(country):
    """Plots the best-fit line and prediction for the given country."""
    plt.plot(country.need.keys(), country.need.values(), label="data", linestyle="", marker="s")

    prediction = country.predict_need(50)
    plt.plot(prediction["years"], prediction["values"], linestyle="--", label="best-fit prediction")

    plt.title("Predicted Production Need For " + country.name)
    plt.xlabel("Year")
    plt.ylabel("Metric Tonnes")
    plt.legend()
    plt.savefig(os.path.dirname(__file__) + "/" + country.name + "-need-prediction.png")
    plt.clf()


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # Uncomment this code when you're ready to visualize the data
    # usa = data.countries["USA"]
    # usa.plot_production_vs_need()
    # plot_linear_prediction(usa)
