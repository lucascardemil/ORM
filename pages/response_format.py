from flet import *

class ResponseFormat(UserControl):
    def __init__(self,page):
        super().__init__()
        self.page = page
    
    def build(self):
        upload_button_test = Ref[ElevatedButton]()
        
        def btn_click(e):
            if not txt_name.value:
                txt_name.error_text = "Please enter your name"
                self.page.update()
            else:
                name = txt_name.value
                print(name)
        
        txt_name = TextField(label="Nombre Alumno")

        return Column(
            controls = [
                Container(
                    theme=Theme(color_scheme=ColorScheme(primary=colors.YELLOW)),
                    content = Column(
                        controls=[
                            txt_name,
                            ElevatedButton("Revisar", ref=upload_button_test, on_click=btn_click, disabled=True)
                        ]
                    )
                )
            ]
        )
