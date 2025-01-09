# Analyzing Global Internet Patterns Analysis

## 📖 Background
In this competition, I explored a dataset that highlights internet usage for different countries from 2000 to 2023. The goal was to import, clean, analyze, and visualize the data using Python.

The end goal was a clean, self-explanatory, and interactive visualization. By conducting a thorough analysis, I delved deeper into how internet usage has changed over time and identified the countries still widely impacted by lack of internet availability.


## 📂 Project Structure
The project is organized as follows:

- `Cleaning__global_internet_patterns.py`: The main script for data cleaning, analysis, and visualization.
- `internet_usage.csv`: The raw dataset containing internet usage statistics.
- `cleaned_internet_usage.csv`: The cleaned dataset after preprocessing.
- `internet_usage_long_format.csv`: The dataset in long format for easier analysis.
- `average_usage_per_year.csv`: Average internet usage per year.
- `median_usage_per_country.csv`: Median internet usage per country.
- `std_dev_usage_per_country.csv`: Standard deviation of internet usage per country.
- `total_usage_per_continent.csv`: Total internet usage per continent.
- `yearly_growth_rate_per_continent.csv`: Yearly growth rate of internet usage per continent.
- `yearly_growth_rate_per_country.csv`: Yearly growth rate of internet usage per country.
- `top_countries.csv`: Top 10 countries by average internet usage.

## 💾 Data

Internet Usage (internet_usage.csv)

Column name	Description
------------------------------------------------------------------------------
Country Name	Name of the country
------------------------------------------------------------------------------
Country Code	Countries 3 character country code
------------------------------------------------------------------------------
2000	Contains the % of population of individuals using the internet in 2000
------------------------------------------------------------------------------
2001	Contains the % of population of individuals using the internet in 2001
------------------------------------------------------------------------------
2002	Contains the % of population of individuals using the internet in 2002
------------------------------------------------------------------------------
2003	Contains the % of population of individuals using the internet in 2003
------------------------------------------------------------------------------
....	...
2023	Contains the % of population of individuals using the internet in 2023
------------------------------------------------------------------------------


## Some Questions/Objectives:

Visualize internet usage over time, by country
How has internet usage changed over time, are there any patterns emerging?


## Analysis and Visualization
The analysis includes:  
 - Calculating the internet usage growth rate for each country.
 - Mapping country codes to their respective continents.
 - Calculating average, median, and standard deviation of internet usage per country.
 - Calculating total internet usage per continent.
 - Calculating yearly growth rates of internet usage per continent and country.
 - Identifying the top 10 countries by average internet usage.

## 🧾 Executive summary

Global internet usage has grown steadily since 2000, with an average penetration rate of 38.17% across 217 countries. 
  Iceland leads with nearly universal connectivity at 87.67%, while nations like Niger and Somalia struggle with rates below 20%, highlighting the digital divide. 
  Europe boasts the highest average internet usage by continent, exceeding 80%, whereas Africa shows the fastest growth due to infrastructure expansion. 
  Despite slowing growth rates in mature markets like North America and Europe, developing regions continue to drive global adoption. 
  These findings emphasize the need for targeted investments in underconnected regions to bridge the digital gap.
