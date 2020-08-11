import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px

import numpy as np
import pandas as pd


########### Define your variables

tabtitle='A ProQuest TDM Project'
myheading='CBS 60 Miniutes Analysis'

########### Set up the chart





########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading)
    ]
)

if __name__ == '__main__':
    app.run_server()
