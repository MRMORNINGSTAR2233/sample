from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class ContentView(BoxLayout):
    def __init__(self, **kwargs):
        super(ContentView, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.label = Label(text='Hello, Kivy!',
                           size_hint=(None, None), size=(200, 50))
        self.add_widget(self.label)


if __name__ == '__main__':
    class MeasureMeApp(App):
        def build(self):
            return ContentView()

    MeasureMeApp().run()
