import pandas as pd
import numpy as np
df = pd.read_csv("C:\\Users\\Administrator\\Documents\\Python Scripts\\titanic.csv")
print(df.isnull().values.ravel().sum())
