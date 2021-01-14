import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get(
    'https://forecast.weather.gov/MapClick.php?lat=34.05361000000005&lon=-118.24549999999999#.X_7gXegzZk4')
soup = BeautifulSoup(page.content, 'html.parser');

week = soup.find(id='seven-day-forecast-body')
# print(week)
# print(soup.find_all('a'))
items = week.find_all(class_="tombstone-container")

# Collect period names
periods_names = [item.find(class_='period-name').get_text() for item in items]
# Collect short descriptions
short_description = [item.find(class_='short-desc').get_text() for item in items]
# Collect temperatures
temperatures = [item.find(class_='temp').get_text() for item in items]

print(periods_names)
print(short_description)
print(temperatures)

# Using pandas cool feature 1
weather_stuff = pd.DataFrame({
    'period': periods_names,
    'short_descriptions': short_description,
    'temperatures': temperatures,
})

print(weather_stuff)

# Using pandas cool feature 2
# Generated csv by panda, generates a csv file
weather_stuff.to_csv('weather.csv')
