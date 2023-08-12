import matplotlib.pyplot as plt
import pandas as pd

# Read the CSV file into a DataFrame
data = pd.read_csv('company_sales_data.csv')

# Extract data for face cream and facewash units sold
months = data['month_number']
facecream_units = data['facecream']
facewash_units = data['facewash']

# Calculate the offset for side-by-side positioning
bar_width = 0.4
bar_offset = bar_width / 2

# Creating the bar chart
plt.figure(figsize=(10, 6))
plt.bar(months, facecream_units, label='Face Cream', color='b', width=0.4)
plt.bar(months, facewash_units, label='Face Wash', color='g', width=0.4, bottom=facecream_units)

# Adding labels and title
plt.xlabel('Month')
plt.ylabel('Units Sold')
plt.title('Units Sold per Month for Face Cream and Face Wash')
plt.xticks(months)
plt.legend()

# Display the plot
plt.tight_layout()
plt.show()
#