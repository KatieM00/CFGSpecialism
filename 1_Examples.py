import pandas as pd

# Creating a Pandas Series from a list
data_list = [10, 20, 30, 40, 50]
series_from_list = pd.Series(data_list)

print(series_from_list)

import pandas as pd

# Creating a Pandas DataFrame from a dictionary
data_dict = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 22, 28, 35],
    'City': ['New York', 'London', 'Paris', 'Tokyo', 'Sydney']
}
df_from_dict = pd.DataFrame(data_dict)

print(df_from_dict)
#