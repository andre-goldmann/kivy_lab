from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout

class BoxLayoutExample(BoxLayout):
  pass
  # def __init__(self, **kwargs):
  #   super().__init__(**kwargs)
  #   self.orientation = "vertical"
  #
  #   b1 = Button(text="A")
  #   b2 = Button(text="A")
  #   self.add_widget(b1)
  #   self.add_widget(b2)

class MainWidget(Widget):
  pass

class TheLapApp(App):
  pass

TheLapApp().run()