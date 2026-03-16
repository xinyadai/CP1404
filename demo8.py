from kivy.app import App
from kivy.app import Builder

class HelloWorld(App):
    def build(self):
        self.root = Builder.load_file('widget.kv')
        return self.root


HelloWorld().run()