import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import dash_daq as daq
import pandas as pd 
import matplotlib.pyplot as plt

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout=dbc.Container([
    dbc.Row([
        dbc.Col([], lg='12')
    ]),
    dbc.Row( [
        dbc.Col([
            
        ], lg='6'),
        dbc.Col([], lg='6'),
    ]),


dbc.Row( [
                dbc.Col([
            
            html.Div(id='', className='pts', children=[html.H3(id='', className='sym', children='Hiv Source'),
            html.Ul(id='', className='', children=[
                html.Li(id='', className='', children=["blood"
                    
                ]),
                 html.Li(id='', className='', children=["semen"
                    
                ]),
                 html.Li(id='', className='', children=["vaginal and rectal fluids"
                    
                ]),
                 html.Li(id='', className='', children=["breast milk"
                    
               
                    
                ])
                
            ])])])])   ,
html.Br(id='', className='', children=[]),




])

if __name__=='__main__':
    app.run_server(debug=True,port=2003)