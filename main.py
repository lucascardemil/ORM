from flet import *
from views import views_handler
from pages.home import Home
from pages.scanner import Scanner

def main(page: Page):
    def route_change(route):
        print(page.route)
        page.views.clear()
        page.views.append(
           views_handler(page)[page.route]
        )
    
    page.on_route_change = route_change
    page.go('/')
app(target=main)