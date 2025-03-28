"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            #V1
            rx.heading("Benyamin Barani Nia", size="9"),

            #V2
            rx.text(
                "“The Best Way to Predict the Future is to Create it.”– P. Drucker & A. Lincoln",
                size="4",
                color_scheme="ruby",
            ),
            
            #V3
            rx.vstack(
                #V1
                rx.hstack(
                    #H1
                    rx.link(
                    rx.button("Website"),
                    href="https://Benwrites.ir",
                    is_external=True,
                    ),

                    #H2
                    rx.link(
                    rx.button("Google Scholar"),
                    href="https://scholar.google.com/citations?hl=en&user=os-xPR4AAAAJ",
                    is_external=True,
                    ),
                    
                    #H3
                    rx.link(
                    rx.button("Github"),
                    href="https://github.com/BenyaminBaraniNia",
                    is_external=True,
                    ),

                    #H4
                    rx.link(
                    rx.button("Linkedin"),
                    href="https://www.linkedin.com/in/benyamin-barani-nia/",
                    is_external=True,
                    ),

                    #H5
                    rx.link(
                    rx.button("Youtube"),
                    href="https://youtube.com/@bbnia.?si=t4Z7wMBMjaZKqnUZ",
                    is_external=True,
                    ),

                    spacing="1",
                    justify="center"
                ),

                #V2
                rx.hstack(
                    #H1
                    rx.link(
                    rx.button("Instagram"),
                    href="https://www.instagram.com/benyamin.b.n",
                    is_external=True,
                    ),

                    #H2
                    rx.link(
                    rx.button("Telegram"),
                    href="https://t.me/bbnia1",
                    is_external=True,
                    ),

                    #H3
                    rx.link(
                    rx.button("SoundCloud"),
                    href="https://soundcloud.com/benyamin-barani-525130635?utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing",
                    is_external=True,
                    ),

                    spacing="1",
                    justify="center",
                ),
            ),
            
            spacing="8",
            justify="center",
            min_height="85vh",
        ),
        
        #rx.logo(),
    )


app = rx.App()
app.add_page(index)
