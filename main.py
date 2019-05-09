import dash
import dash_bootstrap_components as dbc
import dash_daq as daq
import dash_core_components as dcc
import dash_html_components as html

from app import app
from mia.index_page.index_layout import index_layout





def parameter_customization():
    parameters = html.Div(children=[
        slider_parameter(),
        model_test_method(),
    ],className="allParameter")

    return parameters

def slider_parameter():

    slider = daq.Slider(
        min=0,
        max=100,
        value=25,
        handleLabel={"showCurrentValue": True, "label": "VALUE"},
        marks={
            0: {'label': '0', 'style': {'color': '#77b0b1'}},
            25: {'label': '25'},
            50: {'label': '50'},
            75: {'label': '75'},
            100: {'label': '100'}
        }, className="sliderParameter"
    )

    return slider


def model_test_method():
    dropdown = dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montreal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='NYC',
        className="sliderParameter"
    )

    return dropdown


def upload_files():
    uploadDiv = html.Div([
        dcc.Upload(
            id='upload-data',
            children=dbc.Jumbotron(children=[
                'Drag and Drop or ',
                html.A('Select Files')
            ], className="uploadFiles"),
            multiple=True
        ),
    ], className="uploadDiv")
    return uploadDiv

def main():
    index_layout()
    app.run_server(debug=True)


if __name__ == "__main__":
    main()