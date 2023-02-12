import pandas as pd
import os

# directory containing the csv files
path = '/path/to/csv_files/'

# list all csv files in the directory
files = [f for f in os.listdir(path) if f.endswith('.csv')]

# read all csv files into a list of dataframes
df_list = [pd.read_csv(os.path.join(path, f)) for f in files]

# concatenate all dataframes into one
merged_df = pd.concat(df_list)

# write the merged dataframe to a new csv file
merged_df.to_csv('merged_file.csv', index=False)
