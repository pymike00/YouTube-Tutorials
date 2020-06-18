from kivymd.app import MDApp
from kivy.lang import Builder

KV = """
Screen:

    MDRectangleFlatButton:
        text: "Hello Kivy World!"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
"""


class MainApp(MDApp):

    def build(self):
        self.title = "Hello Kivy"
        self.theme_cls.theme_style = "Dark" # Light
        self.theme_cls.primary_palette = "Red"
        return Builder.load_string(KV)


MainApp().run()
