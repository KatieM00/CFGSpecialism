# Q5
import pandas as pd

# Specify the path to the CSV file
csv_file_path = 'netflix_titles.csv'

# Load the CSV file into a Pandas DataFrame
netflix_df = pd.read_csv(csv_file_path)

# Display the first few rows of the DataFrame
print(netflix_df.head())

# Q2
# Specify the path to the CSV file
csv_file_path = 'netflix_titles.csv'

# Load the CSV file into a Pandas DataFrame
netflix_df = pd.read_csv(csv_file_path)

# Display the first 10 rows of the DataFrame
print(netflix_df.head(10))

# Q3

# Specify the path to the CSV file
csv_file_path = 'netflix_titles.csv'

# Load the CSV file into a Pandas DataFrame
netflix_df = pd.read_csv(csv_file_path)

# Display the last 5 rows of the DataFrame
print(netflix_df.tail(5))

# Q4

# Specify the path to the CSV file
csv_file_path = 'netflix_titles.csv'

# Load the CSV file into a Pandas DataFrame
netflix_df = pd.read_csv(csv_file_path)

# Drop rows with any missing values
no_missing_values_df = netflix_df.dropna()

# Get the count of rows with no missing values
num_rows_no_missing_values = no_missing_values_df.shape[0]

# Display the count and the resulting DataFrame
print("Number of rows with no missing values:", num_rows_no_missing_values)
print("\nDataFrame with no missing values:")
print(no_missing_values_df)

# Q5

# Specify the path to the CSV file
csv_file_path = 'netflix_titles.csv'

# Load the CSV file into a Pandas DataFrame
netflix_df = pd.read_csv(csv_file_path)

# Filter rows where the 'type' column is 'Movie'
movies_df = netflix_df[netflix_df['type'] == 'Movie']

# Display the resulting DataFrame with only 'Movie' rows
print(movies_df)

# Q6

# Specify the path to the CSV file
csv_file_path = 'netflix_titles.csv'

# Load the CSV file into a Pandas DataFrame
netflix_df = pd.read_csv(csv_file_path)

# Calculate the average duration of movies in the dataset
average_duration = netflix_df[netflix_df['type'] == 'Movie']['duration'].str.extract('(\d+)').astype(float).mean()

# Filter rows where 'type' is 'Movie' and 'duration' is missing
missing_duration_movies = netflix_df[(netflix_df['type'] == 'Movie') & (netflix_df['duration'].isnull())]

# Replace missing durations with the calculated average using .loc
missing_duration_movies.loc[:, 'duration'] = average_duration

# Display the resulting DataFrame
print(missing_duration_movies)

# Q7

# Specify the path to the CSV file
csv_file_path = 'netflix_titles.csv'

# Load the CSV file into a Pandas DataFrame
netflix_df = pd.read_csv(csv_file_path)

# Check for duplicates in the DataFrame
duplicates = netflix_df.duplicated()

# Count the number of duplicate rows
num_duplicates = duplicates.sum()
print("Number of duplicate rows:", num_duplicates)

# Remove duplicates and create a new DataFrame
cleaned_netflix_df = netflix_df.drop_duplicates()

# Display the cleaned DataFrame
print(cleaned_netflix_df)

# Q8

# Specify the path to the CSV file
csv_file_path = 'netflix_titles.csv'

# Load the CSV file into a Pandas DataFrame
netflix_df = pd.read_csv(csv_file_path)

# Create a dictionary to map current column names to capitalized versions
column_mapping = {column: column.capitalize() for column in netflix_df.columns}

# Rename the columns using the dictionary
netflix_df.rename(columns=column_mapping, inplace=True)

# Display the DataFrame with capitalized column names
print(netflix_df)

# Q9

# Specify the path to the original CSV file and the new CSV file
csv_file_path = 'netflix_titles.csv'
cleaned_csv_file_path = 'cleaned_netflix_titles.csv'

# Load the CSV file into a Pandas DataFrame
netflix_df = pd.read_csv(csv_file_path)

# Drop duplicates and create a new DataFrame
cleaned_netflix_df = netflix_df.drop_duplicates()

# Rename columns to start with a capital letter
column_mapping = {column: column.capitalize() for column in cleaned_netflix_df.columns}
cleaned_netflix_df.rename(columns=column_mapping, inplace=True)

# Save the cleaned DataFrame as a new CSV file
cleaned_netflix_df.to_csv(cleaned_csv_file_path, index=False)

print("Cleaned dataset saved to:", cleaned_csv_file_path)

# MATPLOTLIB QUESTIONS

# Q1

import pandas as pd
import matplotlib.pyplot as plt

# Specify the path to the cleaned CSV file
cleaned_csv_file_path = 'cleaned_netflix_titles.csv'

# Load the cleaned CSV file into a Pandas DataFrame
cleaned_netflix_df = pd.read_csv(cleaned_csv_file_path)

# Filter rows where 'type' is 'Movie'
movies_df = cleaned_netflix_df[cleaned_netflix_df['Type'] == 'Movie'].copy()

# Convert the 'Release_year' column to strings using .loc
movies_df.loc[:, 'Year'] = movies_df['Release_year'].astype(str)

# Count the frequency of movies by year
year_counts = movies_df['Year'].value_counts().sort_index()

# Plot the frequency of movies by year
plt.figure(figsize=(12, 6))
plt.bar(year_counts.index, year_counts.values, color='royalblue')
plt.xlabel('Release Year')
plt.ylabel('Number of Movies')
plt.title('Frequency of Movies by Year of Release')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

# Q2

import pandas as pd
import matplotlib.pyplot as plt

# Specify the path to the cleaned CSV file
cleaned_csv_file_path = 'cleaned_netflix_titles.csv'

# Load the cleaned CSV file into a Pandas DataFrame
cleaned_netflix_df = pd.read_csv(cleaned_csv_file_path)

# Count the occurrences of each genre
genre_counts = cleaned_netflix_df['Listed_in'].value_counts()

# Select the top 5 most popular genres
top_genres = genre_counts.head(5)

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(top_genres, labels=top_genres.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('Top 5 Most Popular Movie Genres')
plt.axis('equal')  # Equal aspect ratio ensures that the pie is drawn as a circle.

plt.show()

# NUMPY QUESTIONS
# Q1

import numpy as np  # Import the numpy module

arr = np.array([0, 56, 82, 500, 140, 43, 92, 10, 25, 11, 18, 26, 150, 240, 364, 196])
arr

# Q2

import numpy as np

arr = np.array([0, 56, 82, 500, 140, 43, 92, 10, 25, 11, 18, 26, 150, 240, 364, 196])

# Count the number of odd numbers in the array
odd_count = np.sum(arr % 2 != 0)

print("Number of odd numbers:", odd_count)

# Q3

import numpy as np

arr = np.array([0, 56, 82, 500, 140, 43, 92, 10, 25, 11, 18, 26, 150, 240, 364, 196])

# Replace odd numbers with 999
arr[arr % 2 != 0] = 999

print("Modified array:", arr)

# Q4

import numpy as np

arr = np.array([0, 56, 82, 500, 140, 43, 92, 10, 25, 11, 18, 26, 150, 240, 364, 196])

# Convert the 1D array into a 4D array of shape (2, 2, 2, 2)
arr_4d = arr.reshape(2, 2, 2, 2)

# Reverse the columns along the fourth axis
arr_reversed = arr_4d[:, :, :, ::-1]

print("Modified 4D array:")
print(arr_reversed)

# Q5

import numpy as np

arr = np.array([0, 56, 82, 500, 140, 43, 92, 10, 25, 11, 18, 26, 150, 240, 364, 196])

# Find values between 100 and 500
filtered_values = arr[(arr > 100) & (arr <= 500)]

print("Values between 100 and 500:", filtered_values)

