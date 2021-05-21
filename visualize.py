# %%
import pandas as pd
import plotly.graph_objects as go
import plotly.offline as offline
import plotly.express as px

offline.init_notebook_mode()

df = pd.read_csv("data/data.csv", parse_dates=["date"], index_col=0)
colors = px.colors.qualitative.Plotly


# %%
_df = df[df["injected"] > 0]
fig = go.Figure()
fig.layout.update({"title": "医療従事者+高齢者 累計ワクチン摂取回数"})
fig.layout.xaxis.update({"title": "日付"})
fig.layout.yaxis.update({"title": "摂取回数"})
fig.add_traces(
    go.Scatter(
        x=_df.index,
        y=_df["injected_total"].dropna(),
        name="摂取回数",
        mode="lines",
        line=dict(color=colors[0]),
    )
)
fig.add_traces(
    go.Scatter(
        x=_df.index,
        y=_df["injected_1st_total"],
        name="内1回目",
        mode="lines",
        line=dict(color=colors[1]),
    )
)
fig.add_traces(
    go.Scatter(
        x=_df.index,
        y=_df["injected_2nd_total"],
        name="内2回目",
        mode="lines",
        line=dict(color=colors[1]),
    )
)
fig.show()

# %%
_df = df[(df["injected_iryo"] > 0) & (df["injected_korei"] > 0)]
fig = go.Figure()
fig.layout.update({"title": "医療従事者+高齢者 日別ワクチン摂取回数（どちらも0でない日のみ表示）"})
fig.layout.xaxis.update({"title": "日付"})
fig.layout.yaxis.update({"title": "摂取回数"})
fig.add_traces(
    go.Scatter(
        x=_df.index,
        y=_df["injected"],
        name="摂取回数",
        mode="lines",
        line=dict(color=colors[0]),
    )
)
fig.add_traces(
    go.Scatter(
        x=_df.index,
        y=_df["injected_1st"],
        name="内1回目",
        mode="lines",
        line=dict(color=colors[1]),
    )
)
fig.add_traces(
    go.Scatter(
        x=_df.index,
        y=_df["injected_2nd"],
        name="内2回目",
        mode="lines",
        line=dict(color=colors[1]),
    )
)
fig.show()

# %%
_df = df[df["injected_iryo"] > 0]
fig = go.Figure()
fig.layout.update({"title": "医療従事者 累計ワクチン摂取回数"})
fig.layout.xaxis.update({"title": "日付"})
fig.layout.yaxis.update({"title": "摂取回数"})
fig.add_traces(
    go.Scatter(
        x=_df.index,
        y=_df["injected_total_iryo"],
        name="摂取回数",
        mode="lines",
        line=dict(color=colors[0]),
    )
)
fig.add_traces(
    go.Scatter(
        x=_df.index,
        y=_df["injected_1st_total_iryo"],
        name="内1回目",
        mode="lines",
        line=dict(color=colors[1]),
    )
)
fig.add_traces(
    go.Scatter(
        x=_df.index,
        y=_df["injected_2nd_total_iryo"],
        name="内2回目",
        mode="lines",
        line=dict(color=colors[1]),
    )
)
fig.show()

# %%
fig = go.Figure()
fig.layout.update({"title": "医療従事者 日別ワクチン摂取回数"})
fig.layout.xaxis.update({"title": "日付"})
fig.layout.yaxis.update({"title": "摂取回数"})
fig.add_traces(
    go.Scatter(
        x=_df.index,
        y=_df["injected_iryo"],
        name="摂取回数",
        mode="lines",
        line=dict(color=colors[0]),
    )
)
fig.add_traces(
    go.Scatter(
        x=_df.index,
        y=_df["injected_1st_iryo"],
        name="内1回目",
        mode="lines",
        line=dict(color=colors[1]),
    )
)
fig.add_traces(
    go.Scatter(
        x=_df.index,
        y=_df["injected_2nd_iryo"],
        name="内2回目",
        mode="lines",
        line=dict(color=colors[1]),
    )
)
fig.show()

# %%
_df = df[df["injected_korei"] > 0]
fig = go.Figure()
fig.layout.update({"title": "高齢者 累計ワクチン摂取回数"})
fig.layout.xaxis.update({"title": "日付"})
fig.layout.yaxis.update({"title": "摂取回数"})
fig.add_traces(
    go.Scatter(
        x=_df.index,
        y=_df["injected_total_korei"],
        name="摂取回数",
        mode="lines",
        line=dict(color=colors[0]),
    )
)
fig.add_traces(
    go.Scatter(
        x=_df.index,
        y=_df["injected_1st_total_korei"],
        name="内1回目",
        mode="lines",
        line=dict(color=colors[1]),
    )
)
fig.add_traces(
    go.Scatter(
        x=_df.index,
        y=_df["injected_2nd_total_korei"],
        name="内2回目",
        mode="lines",
        line=dict(color=colors[1]),
    )
)
fig.show()

# %%
fig = go.Figure()
fig.layout.update({"title": "高齢者 日別ワクチン摂取回数"})
fig.layout.xaxis.update({"title": "日付"})
fig.layout.yaxis.update({"title": "摂取回数"})
fig.add_traces(
    go.Scatter(
        x=_df.index,
        y=_df["injected_korei"],
        name="摂取回数",
        mode="lines",
        line=dict(color=colors[0]),
    )
)
fig.add_traces(
    go.Scatter(
        x=_df.index,
        y=_df["injected_1st_korei"],
        name="内1回目",
        mode="lines",
        line=dict(color=colors[1]),
    )
)
fig.add_traces(
    go.Scatter(
        x=_df.index,
        y=_df["injected_2nd_korei"],
        name="内2回目",
        mode="lines",
        line=dict(color=colors[1]),
    )
)
fig.show()
