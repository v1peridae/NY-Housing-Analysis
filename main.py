import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

ny_housing = pd.read_csv('NY-House-Dataset.csv')

# How much do houses generally cost in different parts of NYC?
housing_cost = ny_housing.groupby(['SUBLOCALITY'])[
    'PRICE'].mean().reset_index()


def millions_formatter(x, pos):
    return f'{x / 1e6:.0f}M'


''' plt.bar(housing_cost['SUBLOCALITY'], housing_cost['PRICE'])
plt.gca().yaxis.set_major_formatter(FuncFormatter(millions_formatter))
plt.xlabel('Part of NYC')
plt.xticks(rotation=90)
plt.ylabel('Average Price (Millions)')
plt.title('Average Price of Houses in Different Parts of NYC')
plt.show()


# What types of homes are most common in the dataset?
home_types = ny_housing.groupby('TYPE').size().reset_index(name='COUNTS')
home_types = home_types.sort_values('COUNTS', ascending=False)
plt.bar(home_types['TYPE'], home_types['COUNTS'])
plt.xlabel('Type of Home')
plt.ylabel('Number of Homes')
plt.xticks(rotation=90)
plt.title('Number of Homes by Type')
plt.show()

# How many bedrooms and bathrooms do most homes have in the dataset?
bedrooms_mode = ny_housing['BEDS'].mode()[0]
bathrooms_mode = ny_housing['BATH'].mode()[0]
print("Most homes in the dataset have", bedrooms_mode,
      "bedrooms and", int(bathrooms_mode), "bathrooms.")


# In which areas are most homes located, and are there areas with more homes?
sublocality_counts = ny_housing['SUBLOCALITY'].value_counts()

plt.bar(sublocality_counts.index, sublocality_counts.values)
plt.xlabel('Sublocality')
plt.ylabel('Number of Homes')
plt.xticks(rotation=90)
plt.title('Number of Homes by Sublocality')
plt.show()'''

# Are there certain brokers who list more homes, and do they usually have higher or lower prices?
broker_counts = ny_housing.groupby(
    'BROKERTITLE').size().reset_index(name='COUNTS')
broker_counts = broker_counts.sort_values('COUNTS', ascending=False)
plt.bar(broker_counts['BROKERTITLE'], broker_counts['COUNTS'])
plt.xlabel('Broker')
plt.ylabel('Number of Listings')
plt.title('Number of Listings by Broker')
plt.xticks(rotation=90)
plt.show()

broker_prices = ny_housing.groupby(
    'BROKERTITLE')['PRICE'].mean().reset_index(name='AVERAGE_PRICE')
broker_prices = broker_prices.sort_values('AVERAGE_PRICE', ascending=False)
plt.bar(broker_prices['BROKERTITLE'], broker_prices['AVERAGE_PRICE'])
plt.xlabel('Broker')
plt.ylabel('Average Price of Listings')
plt.title('Average Price of Listings by Broker')
plt.xticks(rotation=90)
plt.show()

# What states have the most homes listed, and are there differences in average prices?

# Do certain addresses have higher-priced homes, and are there popular neighborhoods?

# Are there specific areas that tend to have more expensive or larger homes?

# Do the number of bedrooms or bathrooms affect the price of a home?

# How have home prices changed over the years in the dataset?

# Are there any homes with unusually high or low prices in the dataset?

# Are homes priced differently in various neighborhoods or states?
