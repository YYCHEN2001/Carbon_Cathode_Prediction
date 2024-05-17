import pandas as pd

# Load the dataset
file_path = 'dataset_20240513.csv'  # Make sure to update this path to your dataset's location
data = pd.read_csv(file_path)

# Create a new column 'micro%' using values from 'Vmicro/Vt' and 'Smicro/SSA'
data['micro%'] = data['Vmicro/Vt'].fillna(data['Smicro/SSA'])

data_processed = data.drop(columns=['Smicro', 'Smeso', 'Vmicro', 'Vmeso', 'Vmicro/Vt', 'Smicro/SSA'])

# Save the processed data to a new CSV file
processed_file_path = 'dataset_1.csv'  # Update this path as needed
data_processed.to_csv(processed_file_path, index=False)

print("Processed data saved to:", processed_file_path)
