import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Titanic dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
titanic_data = pd.read_csv(url)

# Question 1: Pie chart for male/female passengers proportion

gender_counts = titanic_data['sex'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90, colors=['blue', 'pink'])
plt.title('Proportion of Male/Female Passengers')
plt.show()

# Question 2: Pie chart for passengers in each class proportion
class_counts = titanic_data['class'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(class_counts, labels=class_counts.index, autopct='%1.1f%%', startangle=90, colors=['gold', 'lightcoral', 'lightskyblue'])
plt.title('Proportion of Passengers in Each Class')
plt.show()

# Question 3: Relationship between age and fare using a scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=titanic_data, x='age', y='fare', hue='sex')
plt.title('Relationship between Age and Fare')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.legend(title='Sex')
plt.show()

