import dash
import dash_bootstrap_components as dbc
import dash_daq as daq
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], assets_url_path="css")


def image_element(imageLocation, imageClassName):
    imageElement = html.Img(src=app.get_asset_url(imageLocation), className=imageClassName)

    return imageElement

def nav_button(imageLocation, imageClassName, navText, navClassName, colorButton="secondary"):
    navButton = dbc.Button(children=[image_element(imageLocation, imageClassName), navText], color=colorButton, outline=True, className=navClassName)

    return navButton


navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink(children=[nav_button("images/main.png", "navImage", "Home", "mr-1"), ], href="#"),className="navBar"),
        dbc.NavItem(dbc.NavLink(children=[nav_button("images/how_it_works.png", "navImage", "How it works", "mr-1"), ], href="#"),className="navBar"),
        dbc.NavItem(dbc.NavLink(children=[nav_button("images/about.png", "navImage", "About Me", "mr-1"), ], href="https://almasmyrzatay.com/"),className="navBar"),
        dbc.NavItem(dbc.NavLink(children=[nav_button("images/donate.png", "navImage", "Donate", "mr-1"), ], href="https://ko-fi.com/almaska"),className="navBar"),

    ],
    brand=["MIA"],
    brand_href="#",
    sticky="top",
)



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


def card_gallery(cardName, imagePath):


    imageGallery = html.Img(src=app.get_asset_url(imagePath), className="imageGallery")

    card = dbc.Card(children=[
                dbc.CardHeader(cardName),
                dbc.CardBody([
                        imageGallery,
                ], className="cardGallery"),
    ])

    buttonGallery = dbc.Button(children=[card], color="light", className="buttonGallery")

    return buttonGallery

def model_gallery():
    models = html.Div(children=[
        card_gallery("Decision Tree", "images/decision_tree.png"),
        card_gallery("Support Vector Machine", "images/svm.png"),
        card_gallery("Linear Regression", "images/regression.png"),
        card_gallery("Logistic Regression", "images/regression.png"),
        card_gallery("Image Recognition", "images/neural_nets.png"),
        card_gallery("Clustering", "images/cluster.png"),
    ], className="modelGallery")

    return models

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


app.layout = html.Div([
                        navbar,
                        title_main(),
                        html.Img(src='https://media.giphy.com/media/1hM7Y24L8jd6ZLHxAH/giphy.gif'),
                        section_header("Select your model..."),
                        model_gallery(),
                        section_header("Some initial parameters customization..."),
                        parameter_customization(),
                        section_header("Upload your data..."),
                        upload_files(),
                     ])

if __name__ == "__main__":
    app.run_server(debug=True)