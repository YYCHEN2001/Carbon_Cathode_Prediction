import pandas as pd

data = pd.read_csv('dataset_1.csv')

median = data['AML'].median()
data.fillna({'AML': median}, inplace=True)

data.to_csv('dataset_processed.csv', index=False)
