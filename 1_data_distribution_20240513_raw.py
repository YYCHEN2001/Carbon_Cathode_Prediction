import pandas as pd

# 读取Excel文件
df = pd.read_csv('data/dataset_20240513.csv')

# 对每一列进行分布统计
statistics = df.describe(include='all')

# 保存统计结果为md文件
statistics.to_markdown('output/report/report_distribution_raw.md')
