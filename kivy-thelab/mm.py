from math import pi
from kivy.graphics.opengl import glEnable, glDisable, GL_BLEND, GL_DEPTH_TEST
from kivy.graphics.transformation import Matrix
from kivy.graphics.instructions import InstructionGroup
from kivy.graphics import Color, Mesh
import numpy as np
from kivy.graphics.opengl import glScalef
from kivy.uix.image import Image
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.floatlayout import FloatLayout
from math import sqrt
from kivy.graphics import Color, Box
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line, Ellipse
from kivy.vector import Vector


class AreaWidget(Widget):
    # ... (code from previous examples)


class AreaApp(App):
    # ... (code from previous examples)


class DistanceMeasureWidget(Widget):
    # ... (code from previous examples)


class LineNode(Widget):
    # ... (code from previous examples)


class MeasureSCNView(BoxLayout):
    # ... (code from previous examples)


class MeasureViewController(App):
    # ... (code from previous examples)


class SphereWidget(Widget):
    # ... (code from previous examples)


class SphereApp(App):
    # ... (code from previous examples)


if __name__ == '__main__':
    AreaApp().run()
