import dash
import os
import dash_bootstrap_components as dbc

cwd = os.getcwd()
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server
app.config.suppress_callback_exceptions = True
