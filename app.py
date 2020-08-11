import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px

import numpy as np
import pandas as pd


########### Define your variables

tabtitle='PQTDM'
myheading='CBS 60 Miniutes Analysis'

########### Set up the chart

# fig2

# polarity scatter plot

fig2 = go.Figure()

df_pol = pd.read_csv('df_pol.csv')

# make subplots
fig2.add_trace(
    go.Scatter(
        x=df_pol[df_pol['polarity'] >= 0][df_pol['word_count'] >= 100]['year'],
        y=df_pol[df_pol['polarity'] >= 0][df_pol['word_count'] >= 100]['polarity'],
        mode="markers",
        marker=dict(color='red')
    ))

fig2.add_trace(
    go.Scatter(
        x=df_pol[df_pol['polarity'] < 0][df_pol['word_count'] >= 100]['year'],
        y=df_pol[df_pol['polarity'] < 0][df_pol['word_count'] >= 100]['polarity'],
        mode="markers",
        marker=dict(color='blue')
    ))


fig2.update_layout(
    autosize=False,
    showlegend=False,
    plot_bgcolor='white'
)

annotations = []

# Title
annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.05,
                              xanchor='left', yanchor='bottom',
                              text='Style: Positive vs Negative',
                              font=dict(family='Arial',
                                        size=24,
                                        color='rgb(37,37,37)'),
                              showarrow=False))

fig2.update_layout(annotations=annotations)


########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    
    html.Div(children='''
        A ProQuest TDM Project.
    '''),
    
    html.Div(dcc.Graph(
        id='example-graph2',
        figure=fig2))
    ]
)

if __name__ == '__main__':
    app.run_server()
