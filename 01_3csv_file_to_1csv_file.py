import pandas as pd

# list of csv files to be merged
files = ['file1.csv', 'file2.csv', 'file3.csv']

# read all files into a list of dataframes
df_list = [pd.read_csv(file) for file in files]

# concatenate all dataframes into one
merged_df = pd.concat(df_list)

# write the merged dataframe to a new csv file
merged_df.to_csv('merged_file.csv', index=False)
