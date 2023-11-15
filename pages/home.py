from flet import *

class Home(UserControl):
    def __init__(self,page):
        super().__init__()
        self.page = page
        
    def build(self):
        return Column(
            controls=[
                Container(
                    theme=Theme(color_scheme=ColorScheme(primary=colors.YELLOW)),
                    content=Column(
                        controls=[
                            Text("Bienvenido al sistema ORM")
                        ]
                    )
                )
            ]
        )