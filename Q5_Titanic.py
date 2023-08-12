import pandas as pd
titanic = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv')

# a. How many columns and rows does the data have?
num_rows, num_cols = titanic.shape
print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_cols}")

# b. Get a sense of data and find the min, max, and count/mean depending on the data type.
data_summary = titanic.describe(include='all')
print(data_summary)

# c. Give an overview of all missing values in the data.
missing_values = titanic.isnull().sum()
print(missing_values)

# d. Drop rows with missing age values
titanic_age_present = titanic.dropna(subset=['age']).copy()

# Group the passengers into 10-year age ranges
age_ranges = list(range(0, 81, 10))
age_labels = [f"{start} - {end-1}" for start, end in zip(age_ranges[:-1], age_ranges[1:])]
age_labels.append("80+")

# Adjust the bins to include the rightmost edge for the last category
age_ranges.append(81)

# Use .loc to avoid SettingWithCopyWarning
titanic_age_present.loc[:, 'age_category'] = pd.cut(titanic_age_present['age'], bins=age_ranges, labels=age_labels, right=False)

# e. For each age category created in d), find out how many passengers are female/male, and how many traveled in each class.
passengers_by_age_category = titanic_age_present.groupby(['age_category', 'sex', 'pclass']).size().reset_index(name='passenger_count')
print(passengers_by_age_category)

