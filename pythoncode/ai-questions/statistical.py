# Let's suposed I have three tables, with dates (X) and Y value. In the three tables are common dates, but the three tables have dates not found in others. Is possible a function in python that return a table with the joint dates and the Y values of each table for the joint dates?

# One way to achieve this is by using Pandas, a powerful and widely used data analysis library in Python. You can read the three tables into separate Pandas dataframes and then perform an outer join on the date columns, which will give you a new dataframe that contains all the joint dates and the corresponding Y values from each table.

import pandas as pd

# Read in the three tables as dataframes
df1 = pd.read_csv("table1.csv")
df2 = pd.read_csv("table2.csv")
df3 = pd.read_csv("table3.csv")

# Perform an outer join on the date columns
df_merged = df1.merge(df2, on="X", how="outer").merge(df3, on="X", how="outer")

# Fill missing values with 0
df_merged.fillna(0, inplace=True)

# Save the merged dataframe to a new file
df_merged.to_csv("merged_tables.csv", index=False)

# instead of filling the missing values with 0, return only those rows with dates in the three?

import pandas as pd

# Read in the three tables as dataframes
df1 = pd.read_csv("table1.csv")
df2 = pd.read_csv("table2.csv")
df3 = pd.read_csv("table3.csv")

# Perform an outer join on the date columns
df_merged = df1.merge(df2, on="X", how="outer").merge(df3, on="X", how="outer")

# Remove rows with missing values
df_merged.dropna(inplace=True)

# Save the merged dataframe to a new file
df_merged.to_csv("merged_tables.csv", index=False)

# what are most coommon statistics used for a table of data like those, maybe average Y, maximum, minimum, and what others? 

#It depends on the specific data and what you're trying to analyze, but some of the most common statistical measures used with a table of data like this might include:

#Mean or average: the sum of all Y values divided by the number of values.
#Median: the middle value when the values are sorted.
#Mode: the most frequently occurring Y value.
#Maximum: the largest Y value in the table.
#Minimum: the smallest Y value in the table.
#Range: the difference between the maximum and minimum Y values.
#Standard deviation: a measure of the spread of the Y values around the mean.
#Variance: the average of the squared deviations from the mean.
#These are just a few examples, and the specific measures you use will depend on the type of data you have and the questions you're trying to answer. Additionally, Pandas provides many other useful methods for working with and summarizing data, so I recommend looking into the Pandas documentation for more information.

import pandas as pd

# Read in the data from the file into a Pandas dataframe
df = pd.read_csv("table1.csv")

# Compute the mean of the Y values
mean = df['Y'].mean()
print("Mean:", mean)

# Compute the median of the Y values
median = df['Y'].median()
print("Median:", median)

# Compute the mode of the Y values
mode = df['Y'].mode().values[0]
print("Mode:", mode)

# Compute the minimum of the Y values
minimum = df['Y'].min()
print("Minimum:", minimum)

# Compute the maximum of the Y values
maximum = df['Y'].max()
print("Maximum:", maximum)

# Compute the range of the Y values
range = maximum - minimum
print("Range:", range)

# Compute the standard deviation of the Y values
std_dev = df['Y'].std()
print("Standard Deviation:", std_dev)

# Compute the variance of the Y values
variance = df['Y'].var()
print("Variance:", variance)

# To get the minimum and maximum X dates from your table, you can use the min and max methods of the Pandas dataframe:

import pandas as pd

# Read in the data from the file into a Pandas dataframe
df = pd.read_csv("table1.csv")

# Convert the X column to a datetime type, if necessary
df['X'] = pd.to_datetime(df['X'])

# Get the minimum X date
min_date = df['X'].min()
print("Minimum date:", min_date)

# Get the maximum X date
max_date = df['X'].max()
print("Maximum date:", max_date)



