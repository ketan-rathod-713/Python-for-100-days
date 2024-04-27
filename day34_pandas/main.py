import pandas as pd
import numpy as np

df = pd.DataFrame({
    "one":[1,2,3],
    "two":[2,3,4]
})
print(df)
print(type(df))

df.to_csv("usingpandasDay34.csv")

