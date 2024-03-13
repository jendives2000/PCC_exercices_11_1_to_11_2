# Exercises from the book Python Crash Course by Eric Matthes.
# These exercises are about Testings using the pytest package.
# -----------------------------------------------------------------------------
# Exercise 11-2:
# 2a. Modify your function so it requires a third parameter, population.
# 2a.1. It should now return a single string of the form City, Country, population: xxx, such as Santiago, Chile, population: 5000000.
# 2a.2. Run the test again, and make sure test_city_country() fails this time.
# 2b. Modify the function so the population parameter is optional.
# 2b.1. Run the test, and make sure test_city_country() passes again.
# 2c. Write a second test called test_city_country_population() that verifies you can call your function with the values 'santiago', 'chile', and 'population=5000000'.
# 2c.1. Run the tests one more time, and make sure this new test passes.
# -----------------------------------------------------------------------------
# This is part of the exercise 11-2.
# -----------------------------------------------------------------------------
from city_functions_2 import get_city_country

# -----------------------------------------------------------------------------


def test_cities():
    """Do pairs like City and Country names work?"""
    pair_of_city_country_names = get_city_country("Bordeaux", "France")
    assert pair_of_city_country_names == "Bordeaux, France"


def test_city_country():
    """Do pairs like city and country names in lower case work?"""
    low_pair_of_city_country_names = get_city_country("bordeaux", "france")
    assert low_pair_of_city_country_names == "Bordeaux, France"


def test_city_country_population():  # 2c.
    """Do the trio: city, country, population: xxx work?"""
    trio_city_country_pop = get_city_country("shanghai", "china", "28M")
    assert trio_city_country_pop == "Shanghai, China, population: 28M"
