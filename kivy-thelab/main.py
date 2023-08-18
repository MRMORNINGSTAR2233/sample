from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    count = 0

    def build(self):
        layout = BoxLayout(orientation='vertical')

        button = Button(text='Click Me', size_hint=(None, None), size=(200, 50))
        button.bind(on_press=self.button_tapped)
        layout.add_widget(button)

        self.label = Label(text='Count: 0', size_hint=(None, None), size=(200, 50))
        layout.add_widget(self.label)

        return layout

    def button_tapped(self, instance):
        self.count += 1
        self.label.text = f'Count: {self.count}'

if __name__ == '__main__':
    MyApp().run()
