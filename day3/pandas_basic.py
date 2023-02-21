import pandas as pd

path = 'drinks.csv'
df = pd.read_csv(path)
print(df)
df2 = pd.DataFrame({'Yes': [50, 21], 'No': [10, 10]})
print(df2)
