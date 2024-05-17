import pandas as pd

data = pd.read_csv('dataset_processed.csv')

data_reduced = data.drop(['Electrolyte', 'Active mass loading', 'Current collector', 'Potential window', 'B', 'P', 'S'], axis=1)

data_reduced.to_csv('dataset_reduced.csv', index=False)