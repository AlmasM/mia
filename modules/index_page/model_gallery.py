import dash_html_components as html
import dash_bootstrap_components as dbc

from app import app

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