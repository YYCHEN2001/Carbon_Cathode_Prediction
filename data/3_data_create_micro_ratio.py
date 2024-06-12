import pandas as pd

# Load the dataset
file_path = 'dataset_20240513.csv'  # Make sure to update this path to your dataset's location
data = pd.read_csv(file_path)

# Create a new column 'micro%' using values from 'Vmicro/PV' and 'Smicro/SSA'
data['Mic'] = data['Vmicro/PV'].fillna(data['Smicro/SSA'])

# Identify the position of the 'PV' column
pv_index = data.columns.get_loc('PV') + 1  # Get the index and add 1 to place 'Mic' after 'PV'

# Create a list of all columns, inserting 'Mic' after 'PV'
columns = list(data.columns)  # Get all column names
# Insert 'Mic' right after 'PV'
columns.insert(pv_index, 'Mic')
# Now remove the old 'Mic' which is at the end of the list
columns.pop()

# Reassign the DataFrame with new column order
data = data[columns]

data_processed = data.drop(columns=['Smicro', 'Smeso', 'Vmicro', 'Vmeso', 'Vmicro/PV', 'Smicro/SSA'])

# Save the processed data to a new CSV file
processed_file_path = 'dataset_1.csv'  # Update this path as needed
data_processed.to_csv(processed_file_path, index=False)

print("Processed data saved to:", processed_file_path)
