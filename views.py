from flet import *
from pages.home import Home
from pages.scanner import Scanner
from pages.response_format import ResponseFormat

def views_handler(page):
    pages = [
        IconButton(icons.HOME, on_click= lambda _: page.go("/")),
        IconButton(icons.SCANNER, on_click= lambda _: page.go("/scanner")),
        IconButton(icons.TEXT_FIELDS, on_click= lambda _: page.go("/response_format")),
    ]

    return {
        '/':View(
            route='/',
            controls=[
                AppBar(
                    leading=Icon(icons.PALETTE),
                    leading_width=40,
                    title=Text("Inicio"),
                    center_title=False,
                    bgcolor=colors.SURFACE_VARIANT,
                    actions=pages
                ),
                Home(page)
            ]
        ),
        '/scanner':View(
            route='/scanner',
            controls=[
                AppBar(
                    leading=Icon(icons.PALETTE),
                    leading_width=40,
                    title=Text("Revisar Examen"),
                    center_title=False,
                    bgcolor=colors.SURFACE_VARIANT,
                    actions=pages
                ),
                Scanner(page)
            ]
        ),
        '/response_format':View(
            route='/response_format',
            controls=[
                AppBar(
                    leading=Icon(icons.PALETTE),
                    leading_width=40,
                    title=Text("Hoja de respuestas"),
                    center_title=False,
                    bgcolor=colors.SURFACE_VARIANT,
                    actions=pages
                ),
                ResponseFormat(page)
            ]
        ),
    }