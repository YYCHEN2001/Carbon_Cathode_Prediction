import pandas as pd

data = pd.read_csv('dataset_processed.csv')

data_reduced = data.drop(['Elyte', 'AML', 'CC', 'PW', 'B', 'P', 'S'], axis=1)

data_reduced.to_csv('dataset_reduced.csv', index=False)