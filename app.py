import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly.graph_objects as go
import numpy as np
import plotly.express as px
import pandas as pd

# fig 0

bigram_df = pd.read_csv('https://raw.githubusercontent.com/thiha95/flying-dog-beers/master/bigram_df.csv', error_bad_lines=False)

fig0 = px.bar(bigram_df, y="bigram", x="freq", color = 'freq', animation_frame="year", orientation = 'h',

             title="Key Phrases of the Year",

             labels={ # replaces default labels by column name
                "bigram": "Two-Word Phrases",  "freq": "Frequency"},
             color_continuous_scale=px.colors.sequential.Viridis,
             template="simple_white")

fig0.update_layout(yaxis={'categoryorder':'total ascending'})


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title= 'ProQuest TDM: A Sample'


app.layout = html.Div(children=[
    html.H1(children='CBS 60 Minutes'),

    html.Div(children='''
        A ProQuest TDM Project.
    '''),

    html.Div(dcc.Graph(
        id='example-graph',
        figure=fig0
    ))
        ])

if __name__ == '__main__':
    app.run_server()
