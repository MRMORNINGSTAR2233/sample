import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.uix.spinner import Spinner
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_string('''
<MeasureScreen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Measure Distance'
            font_size: 30
            size_hint_y: None
            height: '40sp'
        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: '40sp'
            TextInput:
                id: text_input
                hint_text: 'Enter distance in meters'
                multiline: False
                size_hint_x: 0.7
                on_text_validate: root.calculate_distance()
            Spinner:
                id: spinner
                text: 'Select unit'
                values: ['Meters', 'Kilometers', 'Miles']
                size_hint_x: 0.3
        Label:
            id: result_label
            text: ''
            font_size: 20
            size_hint_y: None
            height: '40sp'
''')


class MeasureScreen(Screen):
    text_input = ObjectProperty(None)
    spinner = ObjectProperty(None)
    result_label = ObjectProperty(None)

    def calculate_distance(self):
        distance = float(self.text_input.text)
        unit = self.spinner.text
        if unit == 'Meters':
            result = distance
        elif unit == 'Kilometers':
            result = distance / 1000
        elif unit == 'Miles':
            result = distance / 1609.34
        self.result_label.text = f'Result: {result:.2f} {unit}'


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget
