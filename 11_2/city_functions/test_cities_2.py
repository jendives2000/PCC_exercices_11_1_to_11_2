# This is part of the exercise 11-1.
# -----------------------------------------------------------------------------
from city_functions_2 import get_city_country

# -----------------------------------------------------------------------------


# 1c. Create a file called test_cities.py that tests the function you just wrote.
def test_cities():
    """Do pairs like City and Country names work?"""
    pair_of_city_country_names = get_city_country("Bordeaux", "France")
    assert pair_of_city_country_names == "Bordeaux, France"


# 1c.1. Write a function called test_city_country() to verify that calling your function with values such as 'santiago' and 'chile' results in the correct string.
def test_city_country():
    """Do pairs like city and country names in lower case work?"""
    low_pair_of_city_country_names = get_city_country("bordeaux", "france")
    assert low_pair_of_city_country_names == "Bordeaux, France"


def test_city_country_population():
    """Do the trio: city, country, population: xxx work?"""
    trio_city_country_pop = get_city_country("shanghai", "china", "28M")
    assert trio_city_country_pop == "Shanghai, China, population: 28M"


# 1d. Run the test, and make sure test_city_country() passes.
