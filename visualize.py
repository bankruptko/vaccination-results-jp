# %%
import pandas as pd
import plotly.offline as offline
from utils import plot

offline.init_notebook_mode()

df = pd.read_csv("data/data.csv", parse_dates=["date"], index_col=0)


# %%
_df = df[df["injected"] > 0]
plot(df=_df, title="医療従事者+高齢者 累計ワクチン摂取回数", type="total")

# %%
_df = df[(df["injected_iryo"] > 0) & (df["injected_korei"] > 0)]
plot(df=_df, title="医療従事者+高齢者 日別ワクチン摂取回数（どちらも0でない日のみ表示）")
# %%
_df = df[df["injected_iryo"] > 0]
plot(df=_df, title="医療従事者 累計ワクチン摂取回数", type="total", category="iryo")

# %%
plot(df=_df, title="医療従事者 日別ワクチン摂取回数", category="iryo")

# %%
_df = df[df["injected_korei"] > 0]
plot(df=_df, title="高齢者 累計ワクチン摂取回数", type="total", category="korei")

# %%
plot(df=_df, title="高齢者 日別ワクチン摂取回数", category="korei")
