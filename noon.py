import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button


class MyApp(App):

    def build(self):
        layout = kivy.uix.BoxLayout(orientation='vertical')
        label = Label(text='Hello World!')
        layout.add_widget(label)
        button = Button(text='Click Me!')
        layout.add_widget(button)
        return layout


if __name__ == '__main__':
    MyApp().run()
