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


def get_city_country(city_name, country_name, population=""):  # 2a. + 2b.
    """Returns a string of a city, a country name and an OPTIONAL population"""
    if population:
        return f"{city_name.title()}, {country_name.title()}, population: {population}"  # 2a.1.
    else:
        return f"{city_name.title()}, {country_name.title()}"
