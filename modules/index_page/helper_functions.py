import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_daq as daq
import dash_core_components as dcc

from app import app


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

def title_main():
    title = dbc.Jumbotron(children=[
        html.H1("MIA", className="header1"),
        html.H1("Machine In Action"),
    ], className="jumbotronMain")

    return title


def section_header(titleName):
    title = dbc.Jumbotron(children=[
        html.H3(titleName, className="title3"),
    ], className="jumbotronMain")

    return title


def image_element(imageLocation, imageClassName):
    imageElement = html.Img(src=app.get_asset_url(imageLocation), className=imageClassName)

    return imageElement