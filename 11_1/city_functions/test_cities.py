# This is part of the exercise 11-1.
# -----------------------------------------------------------------------------
from city_functions import get_city_country  # 1b.

# -----------------------------------------------------------------------------


# 1c. Create a file called test_cities.py that tests the function you just wrote.
#def test_cities():
    """Do pairs like City and Country names work?"""
    pair_of_city_country_names = get_city_country("Bordeaux", "France")
    assert pair_of_city_country_names == "Bordeaux, France"


# 1c.1. Write a function called test_city_country() to verify that calling your function with values such as 'santiago' and 'chile' results in the correct string.
#def test_city_country():
    """Do pairs like city and country names in lower case work?"""
    low_pair_of_city_country_names = get_city_country("bordeaux", "france")
    assert low_pair_of_city_country_names == "Bordeaux, France"


# 1d. Run the test, and make sure test_city_country() passes.