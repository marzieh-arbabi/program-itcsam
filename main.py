from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        lbl=Label(text="ITC SAM Karaj",font_size='20sp')
        return lbl


MyApp().run()