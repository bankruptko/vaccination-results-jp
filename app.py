import os
import pandas as pd


def read_kantei_vaccination_excel(uri: str) -> pd.DataFrame:
    df = pd.read_excel(
        uri,
        usecols=[0, 2, 3, 4],
        names=[
            "date",
            "injected",
            "injected_1st",
            "injected_2nd",
        ],
        parse_dates=["date"],
        index_col=0,
        skiprows=4,
        skipfooter=6,
    )
    return df


df_iryo = read_kantei_vaccination_excel(
    "http://www.kantei.go.jp/jp/content/IRYO-vaccination_data.xlsx"
)
df_korei = read_kantei_vaccination_excel(
    "http://www.kantei.go.jp/jp/content/KOREI-vaccination_data.xlsx"
)
df = (
    pd.merge(
        left=df_iryo,
        right=df_korei,
        left_index=True,
        right_index=True,
        how="outer",
        suffixes=("_iryo", "_korei"),
    )
    .fillna(0)
    .sort_index(ascending=True)
)

# 合算処理
df["injected"] = df["injected_iryo"] + df["injected_korei"]
df["injected_1st_total"] = df["injected_1st_iryo"] + df["injected_1st_korei"]
df["injected_2nd_total"] = df["injected_2nd_iryo"] + df["injected_2nd_korei"]

os.makedirs("data", exist_ok=True)
df.to_csv("data/data.csv")

# GitHub Pages
os.makedirs("output", exist_ok=True)
with open("./output/index.html", mode="w") as f:
    f.write("<html><body>yo</body></html>")
