import pandas as pd
import os
import concurrent.futures

def read_csv(file):
    return pd.read_csv(file)

# directory containing the csv files
path = '/path/to/csv_files/'

# list all csv files in the directory
files = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.csv')]

# use concurrent.futures to read all csv files in parallel
with concurrent.futures.ThreadPoolExecutor() as executor:
    df_list = [df for df in executor.map(read_csv, files)]

# concatenate all dataframes into one
merged_df = pd.concat(df_list)

# write the merged dataframe to a new csv file
merged_df.to_csv('merged_file.csv', index=False)
