import dash_bootstrap_components as dbc
import dash_html_components as html

from app import app
from mia.index_page.model_gallery import model_gallery
from mia.index_page.helper_functions import image_element
from mia.index_page.helper_functions import title_main, section_header


def nav_button(imageLocation, imageClassName, navText, navClassName, colorButton="secondary"):
    navButton = dbc.Button(children=[image_element(imageLocation, imageClassName), navText], color=colorButton, outline=True, className=navClassName)

    return navButton

def navigation_bar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink(children=[nav_button("images/main.png", "navImage", "Home", "mr-1"), ], href="#"),
                        className="navBar"),
            dbc.NavItem(
                dbc.NavLink(children=[nav_button("images/how_it_works.png", "navImage", "How it works", "mr-1"), ],
                            href="#"), className="navBar"),
            dbc.NavItem(dbc.NavLink(children=[nav_button("images/about.png", "navImage", "About Me", "mr-1"), ],
                                    href="https://almasmyrzatay.com/"), className="navBar"),
            dbc.NavItem(dbc.NavLink(children=[nav_button("images/donate.png", "navImage", "Donate", "mr-1"), ],
                                    href="https://ko-fi.com/almaska"), className="navBar"),

        ],
        brand=["MIA"],
        brand_href="#",
        sticky="top",
    )

    return navbar

def index_layout():

    app.layout = html.Div([
        navigation_bar(),
        title_main(),
        html.Img(src='https://media.giphy.com/media/1hM7Y24L8jd6ZLHxAH/giphy.gif'),
        section_header("Select your model..."),
        model_gallery(),
        # section_header("Some initial parameters customization..."),
        # parameter_customization(),
        # section_header("Upload your data..."),
        # upload_files(),
    ])