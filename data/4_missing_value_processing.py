import pandas as pd

data = pd.read_csv('dataset_1.csv')

median = data['Active mass loading'].median()
data.fillna({'Active mass loading': median}, inplace=True)

data.to_csv('dataset_processed.csv', index=False)
