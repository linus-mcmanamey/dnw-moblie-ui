import reflex as rx
from dnw_moblie_ui.src.sidebar import sidebar

def about() -> rx.Component:
    return rx.container(rx.text("About Page")
        , sidebar()
        , rx.color_mode.button(position="top-right")
        , rx.vstack(rx.heading("Welcome to deeds-not-words!", size="9")
                , rx.text("Get started byt logging in or creating an account.", size="5")
                , spacing="5"
                , justify="center"
                , min_height="85vh"))