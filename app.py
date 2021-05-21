import os
import pandas as pd

os.makedirs("data", exist_ok=True)
df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
df.to_csv("data/data.csv")

os.makedirs("output", exist_ok=True)

with open("./output/index.html", mode="w") as f:
    f.write("<html><body>yo</body></html>")
