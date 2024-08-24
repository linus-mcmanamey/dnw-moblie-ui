import reflex as rx
from icecream import ic
from rich import print
from loguru import logger
from rich.traceback import install
from rxconfig import config
from dnw_moblie_ui.src.sidebar import sidebar
from dnw_moblie_ui.src.navbar import navbar_user
from dnw_moblie_ui.pages.about import about
#development/dnw-moblie-ui/dnw_moblie_ui/src/sidebar.py
install()

class State(rx.State):
    user_id: str


def custom():
    return rx.text("Custom Route")


def index() -> rx.Component:
    return rx.flex(
            navbar_user()
            , rx.vstack(
                        rx.heading("Welcome to deeds-not-words!", size="9")
                        , rx.text("Get started byt logging in or creating an account.", size="5")
                        , rx.color_mode.button(position="center")
                        , spacing="0"
                        , justify="left"
                        , min_height="85vh"),
    spacing="4",
    padding="1em",
    flex_direction=["column", "column"],
    width="100%")
        #, sidebar()
        # , rx.color_mode.button(position="top-right")
        # , rx.vstack(rx.heading("Welcome to deeds-not-words!", size="9")
        #         , rx.text("Get started byt logging in or creating an account.", size="5")
        #         , spacing="5"
        #         , justify="center"
        #         , min_height="85vh"))


app = rx.App(theme=rx.theme(appearance = "dark", has_background = True, radius = "large", accent_color = "blue", accent_level = 10))
app.add_page(index, title= "deeds-not-words")
app.add_page(about)
app.add_page(custom, route="/custom-route")
