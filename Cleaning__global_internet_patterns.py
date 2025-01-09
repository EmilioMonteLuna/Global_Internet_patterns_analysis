import pandas as pd
import numpy as np
import pycountry_convert as pc
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
file_path = 'internet_usage.csv'
data = pd.read_csv(file_path)

# Clean the data
# Drop rows with any missing values
data_cleaned = data.dropna()

# Convert 'Year' columns to long format for easier analysis
data_long = pd.melt(data_cleaned, id_vars=['Country Name', 'Country Code'],
                    var_name='Year', value_name='Internet Usage (%)')

# Convert 'Year' to integer type
data_long['Year'] = data_long['Year'].astype(int)

# Ensure 'Internet Usage (%)' is numeric
data_long['Internet Usage (%)'] = pd.to_numeric(data_long['Internet Usage (%)'], errors='coerce')

# Calculate the Internet Usage Growth Rate
data_long['Internet Usage Growth Rate (%)'] = data_long.groupby('Country Name')['Internet Usage (%)'].transform(lambda x: x.pct_change(fill_method=None) * 100)

# Replace infinite values with NaN
data_long.replace([np.inf, -np.inf], np.nan, inplace=True)

# Map 'Country Code' to 'Continent'
def get_continent(country_code):
    try:
        country_alpha2 = pc.country_alpha3_to_country_alpha2(country_code)
        continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
        continent_name = pc.convert_continent_code_to_continent_name(continent_code)
        return continent_name
    except KeyError:
        return np.nan

data_long['Continent'] = data_long['Country Code'].apply(get_continent)

# Prepare data for calculations
# Calculate average internet usage per year
average_usage_per_year = data_long.groupby('Year')['Internet Usage (%)'].mean().reset_index()
average_usage_per_year.columns = ['Year', 'Average Internet Usage (%)']

# Calculate median internet usage per country
median_usage_per_country = data_long.groupby('Country Name')['Internet Usage (%)'].median().reset_index()
median_usage_per_country.columns = ['Country Name', 'Median Internet Usage (%)']

# Calculate standard deviation of internet usage per country
std_dev_usage_per_country = data_long.groupby('Country Name')['Internet Usage (%)'].std().reset_index()
std_dev_usage_per_country.columns = ['Country Name', 'Standard Deviation of Internet Usage (%)']

# Calculate total internet usage per continent
total_usage_per_continent = data_long.groupby('Continent')['Internet Usage (%)'].sum().reset_index()
total_usage_per_continent.columns = ['Continent', 'Total Internet Usage (%)']

# Calculate yearly growth rate per continent
yearly_growth_rate_per_continent = data_long.groupby(['Continent', 'Year'])['Internet Usage (%)'].mean().groupby(level=0).pct_change(fill_method=None) * 100
yearly_growth_rate_per_continent = yearly_growth_rate_per_continent.reset_index()
yearly_growth_rate_per_continent.columns = ['Continent', 'Year', 'Yearly Growth Rate (%)']

# Calculate yearly growth rate per country
yearly_growth_rate_per_country = data_long.groupby(['Country Name', 'Year'])['Internet Usage (%)'].mean().groupby(level=0).pct_change(fill_method=None) * 100
yearly_growth_rate_per_country = yearly_growth_rate_per_country.reset_index()
yearly_growth_rate_per_country.columns = ['Country Name', 'Year', 'Yearly Growth Rate (%)']

# Get top 10 countries by average internet usage
average_usage_per_country = data_long.groupby('Country Name')['Internet Usage (%)'].mean().reset_index()
average_usage_per_country.columns = ['Country Name', 'Average Internet Usage (%)']
top_countries = average_usage_per_country.sort_values(by='Average Internet Usage (%)', ascending=False).head(10)

# Save additional CSV files
data_cleaned.to_csv("cleaned_internet_usage.csv", index=False)
data_long.to_csv("internet_usage_long_format.csv", index=False)
average_usage_per_year.to_csv("average_usage_per_year.csv", index=False)
median_usage_per_country.to_csv("median_usage_per_country.csv", index=False)
std_dev_usage_per_country.to_csv("std_dev_usage_per_country.csv", index=False)
total_usage_per_continent.to_csv("total_usage_per_continent.csv", index=False)
yearly_growth_rate_per_continent.to_csv("yearly_growth_rate_per_continent.csv", index=False)
yearly_growth_rate_per_country.to_csv("yearly_growth_rate_per_country.csv", index=False)
top_countries.to_csv("top_countries.csv", index=False)



# Check for any NaN values in the 'Continent' column
# Identify country codes that are not mapped to a continent
unmapped_countries = data_long[data_long['Continent'].isna()][['Country Name', 'Country Code']]

if not unmapped_countries.empty:
    print("The following country codes could not be mapped to a continent:")
    print(unmapped_countries)
else:
    print("All country codes are successfully mapped to their respective continents.")

# Visualization
plt.figure(figsize=(14, 7))

# Plot average internet usage over time
plt.subplot(1, 2, 1)
sns.lineplot(data=average_usage_per_year, x='Year', y='Average Internet Usage (%)')
plt.title('Average Internet Usage Over Time')
plt.xlabel('Year')
plt.ylabel('Average Internet Usage (%)')

# Plot top 10 countries by average internet usage
plt.subplot(1, 2, 2)
sns.barplot(data=top_countries, x='Average Internet Usage (%)', y='Country Name', palette='viridis')
plt.title('Top 10 Countries by Average Internet Usage')
plt.xlabel('Average Internet Usage (%)')
plt.ylabel('Country Name')

plt.tight_layout()
plt.show()