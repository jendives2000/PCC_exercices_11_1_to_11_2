def get_city_country(city_name, country_name, population=""):
    """Returns a string of a city, a country name and an OPTIONAL population"""
    if population:
        return f"{city_name.title()}, {country_name.title()}, population: {population}"
    else:
        return f"{city_name.title()}, {country_name.title()}"


# 1b. Store the function in a module called city_functions.py,
