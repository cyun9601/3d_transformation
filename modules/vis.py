import plotly.graph_objects as go 
import numpy as np

def add_figure(data, layout):
    fig = go.Figure(data=data, layout=layout)

    fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
    fig.update_yaxes(
        scaleanchor='x',
        scaleratio = 1
    )
    return fig

def layout(width = 512, height = 384):
    layout = go.Layout(
        width=width,
        height=height,
        margin=dict(l=0,r=0,b=0,t=0),
        scene = dict(
            aspectmode='data'),
        showlegend = False
    )
    return layout

def plot_array(array: np.array): 
    splot = go.Scatter3d(
        x = array[:, 0], y = array[:, 1], z = array[:, 2],
        mode='markers',
        marker = dict(
            size = 1 
        )
    )

    pdata = [splot]

    fig = add_figure(pdata, layout())
    fig.show()
    return fig

def plot_pointcloud(pnts: np.array):
    fig = plot_array(pnts)