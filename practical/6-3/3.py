import pandas as pd

data = [10, 20, 30, 40, 50]
index = ["a", "b", "c", "d", "e"]
si = pd.Series(data, index)
print(si)