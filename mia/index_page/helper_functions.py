import dash_bootstrap_components as dbc
import dash_html_components as html

from app import app

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