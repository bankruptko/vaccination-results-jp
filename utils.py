import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


def plot(df: pd.DataFrame, title: str, type: str = None, category: str = None):
    colors = px.colors.qualitative.Plotly

    suffix = ""
    if type:
        suffix += "_" + type
    if category:
        suffix += "_" + category

    fig = go.Figure()
    fig.layout.update({"title": title})
    fig.layout.xaxis.update({"title": "日付"})
    fig.layout.yaxis.update({"title": "摂取回数"})
    fig.add_traces(
        go.Scatter(
            x=df.index,
            y=df[f"injected{suffix}"].dropna(),
            name="摂取回数",
            mode="lines",
            line=dict(color=colors[0]),
        )
    )
    fig.add_traces(
        go.Scatter(
            x=df.index,
            y=df[f"injected_1st{suffix}"],
            name="内1回目",
            mode="lines",
            line=dict(color=colors[1]),
        )
    )
    fig.add_traces(
        go.Scatter(
            x=df.index,
            y=df[f"injected_2nd{suffix}"],
            name="内2回目",
            mode="lines",
            line=dict(color=colors[1]),
        )
    )
    fig.show()
