#loading some comma-separated value data using Pandas into a DataFrame:
%matplotlib inline
import numpy as np
import pandas as pd

df = pd.read_csv("PastHires.csv")
df.head()
print()