import pandas as pd
import os
import re

def extract_area(postcode):
    pc = postcode.replace(" ", "")
    match = re.match(r'^([A-Z]{1,2})', pc)
    return match.group(1) if match else None

input_file = "data/20250707_ons_postcode.csv"
output_dir = "data/postcode_clusters"
os.makedirs(output_dir, exist_ok=True)

chunksize = 100
required_cols = ['PCDS', 'LAT', 'LONG']

for chunk in pd.read_csv(input_file, chunksize=chunksize, usecols=required_cols):
    chunk['area'] = chunk['PCDS'].apply(extract_area)
    for area, group in chunk.groupby('area'):
        if area:  # skip None
            filename = os.path.join(output_dir, f"{area}.csv")
            group.drop(columns='area').to_csv(filename, mode='w' if not os.path.exists(filename) else 'a', index=False, header=not os.path.exists(filename))

print(f"Done! CSVs split by postcode area saved in '{output_dir}/'")
