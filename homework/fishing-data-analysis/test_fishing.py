from classes import (Country, Fishing)
from difflib import get_close_matches
import inspect
import os
import csv
from io import StringIO
import math


def test_country_init():
    '''
    Test the initialization of the Country class. Ensures that the class is created with
    fields for farmed, wild caught, consumption, population, production, and need.
    '''
    print("\t... initialization (aka __init__)... ", end='')
    country = Country("Testland", 2010, 2012)

    attrs = dir(country)

    expected_attrs = [
        'name', 'farmed', 'wild_caught', 'consumption',
        'population', 'production', 'need', 'years'
    ]

    for attr in expected_attrs:
        if attr in attrs:
            continue

        if attr == "name":
            assert country.name == "Testland", \
                f"Expected name to be 'Testland', got {country.name} instead."

        closest = get_close_matches(attr, attrs, n=1)
        close_msg = "No similar attribute found."
        if closest and len(closest) > 0:
            closest = closest[0]
            close_msg = f"Was '{closest}' supposed to be it?"

        raise AssertionError(
            f"Attribute '{attr}' not found in Country class. {close_msg}"
        )

    print("PASSED!")


def test_country_update_data():
    '''
    Test the update_data method of the Country class. Ensures that data is correctly
    updated for farmed, wild caught, consumption, and population measures.
    '''
    print("\t... update_data method... ", end='')

    country = Country("Testland", 2010, 2012)
    check_method(country, "update_data", ["row"])

    row = {
        "measure": "farmed",
        "2010": "1000",
        "2011": "1500",
        "2012": ""
    }
    country.update_data(row)
    assert country.farmed == {2010: 1000.0, 2011: 1500.0, 2012: None}

    row["measure"] = "wild caught"
    country.update_data(row)
    assert country.wild_caught == {2010: 1000.0, 2011: 1500.0, 2012: None}

    row["measure"] = "consumption"
    country.update_data(row)
    assert country.consumption == {2010: 1000.0, 2011: 1500.0, 2012: None}

    row["measure"] = "population"
    country.update_data(row)
    assert country.population == {2010: 1000.0, 2011: 1500.0, 2012: None}

    print("PASSED!")


def test_country_get_actual_production():
    '''
    Test the get_actual_production method of the Country class. Ensures that production
    is calculated correctly based on farmed and wild caught data.
    '''
    print("\t... get_actual_production method... ", end='')

    country = Country("Testland", 2010, 2012)
    check_method(country, "get_actual_production", ["year"])

    country.farmed = {2010: 1000.0, 2011: None, 2012: 2000.0}
    country.wild_caught = {2010: 500.0, 2011: 300.0, 2012: None}

    country.get_actual_production(2010)
    assert country.production[2010] == 1500.0, \
        f"Expected production for 2010 to be 1500.0, got {country.production[2010]}"

    country.get_actual_production(2011)
    assert country.production[2011] == 300.0, \
        f"Expected production for 2011 to be 300.0, got {country.production[2011]}"

    country.get_actual_production(2012)
    assert country.production[2012] == 2000.0, \
        f"Expected production for 2012 to be 2000.0, got {country.production[2012]}"

    print("PASSED!")


def test_country_get_production_need():
    '''
    Test the get_production_need method of the Country class. Ensures that need is
    calculated correctly based on population and consumption data.
    '''
    print("\t... get_production_need method... ", end='')

    country = Country("Testland", 2010, 2012)
    check_method(country, "get_production_need", ["year"])

    country.population = {2010: 1000000.0, 2011: None, 2012: 2000000.0}
    country.consumption = {2010: 10.0, 2011: 15.0, 2012: None}

    country.get_production_need(2010)
    assert country.need[2010] == 10000.0, \
        f"Expected need for 2010 to be 10000.0, got {country.need[2010]}"

    country.get_production_need(2011)
    assert country.need[2011] is None, \
        f"Expected need for 2011 to be None, got {country.need[2011]}"

    country.get_production_need(2012)
    assert country.need[2012] is None, \
        f"Expected need for 2012 to be None, got {country.need[2012]}"

    print("PASSED!")


def test_country_calculate():
    '''
    Test the calculate method of the Country class. Ensures that production and need
    are calculated correctly based on farmed, wild caught, consumption, and population data.
    '''
    print("\t... calculate method... ", end='')

    country = Country("Testland", 2010, 2012)
    check_method(country, "calculate", [])

    country.farmed = {2010: 1000.0, 2011: 1500.0, 2012: None}
    country.wild_caught = {2010: 500.0, 2011: None, 2012: 200.0}
    country.consumption = {2010: 10.0, 2011: 15.0, 2012: None}
    country.population = {2010: 1000000.0, 2011: None, 2012: 2000000.0}

    country.calculate()

    assert country.production == {
        2010: 1500.0,
        2011: 1500.0,
        2012: 200.0
    }, f"Expected production to be {country.production}"

    assert country.need == {
        2010: 10000.0,
        2011: None,
        2012: None
    }, f"Expected need to be {country.need}"

    print("PASSED!")


def test_country_predict_need():
    '''
    Test the predict_need method of the Country class. Ensures that the predicted need
    is calculated correctly based on population and consumption data. The function should
    just exist and not be modified from what was given.
    '''
    print("\t... predict_need method... ", end='')
    country = Country("Testland", 2010, 2012)
    check_method(country, "predict_need", ["predict_years"])
    print("PASSED!")


def test_fishing_init():
    '''
    Test the initialization of the Fishing class. Ensures that the class is created with
    fields for countries and years.
    '''
    print("\t... initialization (aka __init__)... ", end='')

    check_method(Fishing, "__init__", ["filename"])

    test_csv = StringIO()
    test_csv.write("country,country code,measure,2010,2011,2012\n")
    test_csv.write("United States,USA,farmed,1000,1500,2000\n")
    test_csv.write("United States,USA,wild caught,500,600,700\n")
    test_csv.write("United States,USA,consumption,10,15,20\n")
    test_csv.write("United States,USA,population,300000000,310000000,320000000\n")

    fishing = Fishing(stringio_to_fd(test_csv))

    attrs = dir(fishing)
    expected_attrs = ['countries', 'min_year', 'max_year']

    for attr in expected_attrs:
        if attr in attrs:
            continue

        closest = get_close_matches(attr, attrs, n=1)
        close_msg = "No similar attribute found."
        if closest and len(closest) > 0:
            closest = closest[0]
            close_msg = f"Was '{closest}' supposed to be it?"

        raise AssertionError(
            f"Attribute '{attr}' not found in Fishing class. {close_msg}"
        )

    print("PASSED!")


def test_fishing_parse_data():
    '''
    Test the parse_data method of the Fishing class. Ensures that data is correctly
    parsed and stored in the countries dictionary.
    '''
    print("\t... parse_data method... ", end='')

    test_csv = StringIO()
    test_csv.write("country,country code,measure,2010,2011,2012\n")
    test_csv.write("United States,USA,farmed,1000,1500,2000\n")
    test_csv.write("United States,USA,wild caught,500,600,700\n")
    test_csv.write("United States,USA,consumption,10,15,20\n")
    test_csv.write("United States,USA,population,300000000,310000000,320000000\n")

    dict_contents = list(csv.DictReader(open(stringio_to_fd(test_csv))))
    try:
        # Temporarily override Fishing's init; we'll put it back later
        f_original_init = Fishing.__init__

        def new_init(self):
            self.countries = {}
            self.min_year = 2010
            self.max_year = 2012

        Fishing.__init__ = new_init
        fishing = Fishing()

        check_method(fishing, "parse_data", ["raw_data"])

        fishing.parse_data(dict_contents)
        assert isinstance(fishing.countries, dict), \
            "Expected countries to be a dictionary."

        assert len(fishing.countries) == 1, \
            "Expected countries to contain only one country for test data."

        for code, country in fishing.countries.items():
            assert isinstance(country, Country), \
                f"Expected country with code {code} to be an instance of Country."

        print("PASSED!")
    finally:
        Fishing.__init__ = f_original_init


def test_fishing_total_production_need():
    '''
    Test the total_production_need method of the Fishing class. Ensures that the total
    production need is calculated correctly across all countries.
    '''
    print("\t... total_production_need method... ", end='')

    test_csv = StringIO()
    test_csv.write("country,country code,measure,2010,2011,2012\n")
    test_csv.write("United States,USA,farmed,1000,1500,2000\n")
    test_csv.write("United States,USA,wild caught,500,600,700\n")
    test_csv.write("United States,USA,consumption,10,15,20\n")
    test_csv.write("United States,USA,population,300000000,310000000,320000000\n")

    fishing = Fishing(stringio_to_fd(test_csv))

    years_to_predict = 10
    total_need = fishing.total_production_need(years_to_predict)

    assert math.isclose(total_need, 23383333.33333), \
        f"Expected total production need to be (approx.) 23383333.33333, got {total_need}"

    print("PASSED!")


def stringio_to_fd(s):
    '''
    STUDENTS: You do not need to understand this function for the homework.
    ----------------------------------------
    Convert a StringIO object to a file descriptor for testing purposes. This 
    returns an object that can be passed to `open` or similar functions that
    expect a path to a file.

    This is useful for simulating file input in tests without needing to create
    actual files on disk.
    '''
    r, w = os.pipe()
    os.write(w, s.getvalue().encode())
    os.close(w)
    return r


def check_method(instance, method_name, expected_params=[]):
    m = getattr(instance, method_name, None)

    if m is None or not callable(m):
        raise AssertionError(
            f"{method_name} function not found in Country class. Did you implement it yet?")

    params = inspect.signature(m).parameters
    for param in expected_params:
        if param not in params:
            closest = get_close_matches(param, params.keys(), n=1)
            if closest and len(closest) > 0:
                closest = closest[0]
                raise AssertionError(
                    f"{method_name} is missing parameter '{param}'. " +
                    f"Was '{closest}' supposed to be it?"
                )
            raise AssertionError(f"{method_name} is missing parameter '{param}'.")


if __name__ == "__main__":
    try:
        print("Testing Country class methods...")
        test_country_init()
        test_country_update_data()
        test_country_get_actual_production()
        test_country_get_production_need()
        test_country_calculate()
        test_country_predict_need()

        print()
        print("Testing Fishing class methods...")
        test_fishing_init()
        test_fishing_parse_data()
        test_fishing_total_production_need()

    except Exception as e:
        print("FAILED!")
        raise e

    print()
    print("All tests passed!")
