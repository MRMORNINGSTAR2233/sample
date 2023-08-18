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
    def __init__(self, **kwargs):
        super(AreaWidget, self).__init__(**kwargs)
        self.floor_rect = {'length': 0, 'breadth': 0}

        self.length_nodes = []
        self.breadth_nodes = []
        self.current_state = 'lengthCalc'

        self.label_length = Label(text='--', pos=(50, 50))
        self.label_breadth = Label(text='--', pos=(50, 30))
        self.label_area = Label(text='--', pos=(50, 10))
        self.add_widget(self.label_length)
        self.add_widget(self.label_breadth)
        self.add_widget(self.label_area)

        self.bind(pos=self.update_touch_position)

    def on_touch_down(self, touch):
        if len(self.length_nodes) + len(self.breadth_nodes) >= 4:
            self.reset_measurement()

        if self.current_state == 'lengthCalc':
            self.length_nodes.append(touch.pos)
            with self.canvas:
                Color(1, 0, 0, 0.7)
                Ellipse(pos=(touch.pos[0] - 5,
                        touch.pos[1] - 5), size=(10, 10))
        elif self.current_state == 'breadthCalc':
            self.breadth_nodes.append(touch.pos)
            with self.canvas:
                Color(0, 1, 0, 0.7)
                Ellipse(pos=(touch.pos[0] - 5,
                        touch.pos[1] - 5), size=(10, 10))

        if len(self.length_nodes) == 2:
            self.current_state = 'breadthCalc'
            self.floor_rect['length'] = Vector(
                self.length_nodes[0]).distance(self.length_nodes[1])
            self.label_length.text = f"Length: {self.floor_rect['length']:.2f}m"

        if len(self.breadth_nodes) == 2:
            self.floor_rect['breadth'] = Vector(
                self.breadth_nodes[0]).distance(self.breadth_nodes[1])
            self.label_breadth.text = f"Breadth: {self.floor_rect['breadth']:.2f}m"
            self.label_area.text = f"Area: {self.floor_rect['length'] * self.floor_rect['breadth']:.2f}m²"

    def reset_measurement(self):
        self.length_nodes = []
        self.breadth_nodes = []
        self.current_state = 'lengthCalc'
        self.floor_rect['length'] = 0
        self.floor_rect['breadth'] = 0
        self.label_length.text = '--'
        self.label_breadth.text = '--'
        self.label_area.text = '--'
        self.canvas.clear()

    def update_touch_position(self, *args):
        self.label_length.pos = (self.pos[0] + 50, self.pos[1] + 50)
        self.label_breadth.pos = (self.pos[0] + 50, self.pos[1] + 30)
        self.label_area.pos = (self.pos[0] + 50, self.pos[1] + 10)


class AreaApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        area_widget = AreaWidget()
        layout.add_widget(area_widget)

        button_reset = Button(text='Reset')
        button_reset.bind(on_press=area_widget.reset_measurement)
        layout.add_widget(button_reset)

        return layout


class DistanceMeasureWidget(Widget):
    def __init__(self, **kwargs):
        super(DistanceMeasureWidget, self).__init__(**kwargs)
        self.distance = 0
        self.distance_nodes = []

        self.label_distance = Label(text='--', pos=(50, 50))
        self.add_widget(self.label_distance)

        self.bind(pos=self.update_touch_position)

    def on_touch_down(self, touch):
        if len(self.distance_nodes) >= 2:
            self.reset_measurement()

        self.distance_nodes.append(touch.pos)
        with self.canvas:
            Color(1, 1, 1, 0.7)
            Ellipse(pos=(touch.pos[0] - 5, touch.pos[1] - 5), size=(10, 10))

        if len(self.distance_nodes) == 2:
            start_pos, end_pos = self.distance_nodes
            self.distance = Vector(start_pos).distance(end_pos)
            self.label_distance.text = f"Distance: {self.distance:.2f}m"

    def reset_measurement(self):
        self.distance_nodes = []
        self.distance = 0
        self.label_distance.text = '--'
        self.canvas.clear()

    def update_touch_position(self, *args):
        self.label_distance.pos = (self.pos[0] + 50, self.pos[1] + 50)


class DistanceMeasureApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        distance_widget = DistanceMeasureWidget()
        layout.add_widget(distance_widget)

        button_reset = Button(text='Reset')
        button_reset.bind(on_press=distance_widget.reset_measurement)
        layout.add_widget(button_reset)

        return layout


class LineNode(Widget):
    def __init__(self, vectorA, vectorB, color, width, **kwargs):
        super(LineNode, self).__init__(**kwargs)

        self.box = None
        self.node_line = None

        self.setup_line(vectorA, vectorB, color, width)

    def setup_line(self, vectorA, vectorB, color, width):
        self.pos = vectorA
        self.size = (width, self.distance(vectorA, vectorB))

        self.canvas.before.clear()
        with self.canvas.before:
            Color(*color)
            self.box = Box(pos=self.pos, size=self.size)

        self.node_line = self.box

        orientation_node = Widget()
        orientation_node.pos = vectorB
        self.add_widget(orientation_node)

    def distance(self, vectorA, vectorB):
        return sqrt(
            (vectorA[0] - vectorB[0]) ** 2 +
            (vectorA[1] - vectorB[1]) ** 2 +
            (vectorA[2] - vectorB[2]) ** 2
        )

    def update_node(self, vectorA=None, vectorB=None, color=None):
        if vectorA and vectorB:
            self.size = (self.width, self.distance(vectorA, vectorB))
            self.box.size = self.size
            self.node_line.pos = (self.pos[0], self.pos[1] - self.height / 2)

            orientation_node = Widget()
            orientation_node.pos = vectorB
            self.clear_widgets()
            self.add_widget(self.node_line)
            self.add_widget(orientation_node)

        if color:
            self.canvas.before.clear()
            with self.canvas.before:
                Color(*color)
                self.box = Box(pos=self.pos, size=self.size)


class DistanceMeasureApp(App):
    def build(self):
        # Example usage of LineNode widget
        vectorA = (100, 100, 0)  # Replace with your SCNVector3
        vectorB = (200, 200, 0)  # Replace with your SCNVector3
        color = (1, 1, 1, 0.7)  # Replace with your UIColor
        width = 5  # Replace with your line thickness

        line_node = LineNode(vectorA, vectorB, color, width)

        return line_node
    
class MeasureSCNView(FloatLayout):
    def __init__(self, **kwargs):
        super(MeasureSCNView, self).__init__(**kwargs)
        self.marked_points = []

    def on_touch_down(self, touch):
        if len(self.marked_points) >= 2:
            self.clear_scene()

        hit_result_position = self.hit_result_for_point(touch.pos)
        if hit_result_position:
            self.marked_points.append(hit_result_position)
            self.draw_marked_point(hit_result_position)

        if len(self.marked_points) == 2:
            distance = self.distance_between_points(
                self.marked_points[0], self.marked_points[1])
            print(f"Distance between points: {distance:.2f} units")

    def hit_result_for_point(self, point):
        # Replace this function with your implementation for hitTest in Kivy
        # hitTest function returns the world coordinates of the hit point
        # from the screen point.
        pass

    def draw_marked_point(self, position):
        # Replace this function with your implementation for drawing points in Kivy
        # The position is the world coordinates from the hitTest result.
        # Use Kivy graphics to draw a marker at the given position.
        pass

    def distance_between_points(self, point1, point2):
        dx = point2[0] - point1[0]
        dy = point2[1] - point1[1]
        dz = point2[2] - point1[2]
        return sqrt(dx*dx + dy*dy + dz*dz)

    def clear_scene(self):
        # Replace this function with your implementation to clear the scene in Kivy
        # Remove all markers or lines drawn on the screen.
        self.marked_points = []


class MeasureApp(App):
    def build(self):
        return MeasureSCNView()


class LineNode(Widget):
    # Define LineNode widget similar to previous examples
    # ... (code from previous examples)

class MeasureSCNView(BoxLayout):
    # Define MeasureSCNView widget similar to previous examples
    # ... (code from previous examples)


class MeasureViewController(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        # Replace with the path to your center point image
        center_point_image_view = Image(source='center_point_image.png')
        scene_view = MeasureSCNView()

        layout.add_widget(center_point_image_view)
        layout.add_widget(scene_view)

        return layout

    def remove_nodes(self, node_list):
        # Implement the function to remove nodes from the scene in Kivy
        # You'll need to handle the removal of nodes from the MeasureSCNView scene
        pass

    def update_scale_from_camera_for_nodes(self, nodes, camera_position):
        # Implement the function to update node scaling based on camera distance in Kivy
        # You'll need to handle scaling of nodes based on their distance from the camera
        pass

    def on_start(self):
        # Implement the on_start method to run the scene in Kivy
        pass

    def on_stop(self):
        # Implement the on_stop method to pause the scene in Kivy
        pass

    def on_pause(self):
        # Implement the on_pause method to pause the scene in Kivy
        return True

    def on_resume(self):
        # Implement the on_resume method to resume the scene in Kivy
        pass


class SphereWidget(Widget):
    def __init__(self, color, radius, **kwargs):
        super(SphereWidget, self).__init__(**kwargs)

        self.mesh = Mesh(mode='triangle_fan')
        self.add_mesh()
        self.set_color(color)
        self.set_radius(radius)

        self.bind(pos=self.update_mesh)
        self.bind(size=self.update_mesh)

    def set_color(self, color):
        self.mesh.color = color

    def set_radius(self, radius):
        self.radius = radius
        self.update_mesh()

    def add_mesh(self):
        self.canvas.add(self.mesh)
        glEnable(GL_BLEND)
        glDisable(GL_DEPTH_TEST)
        self.canvas['projection_mat'] = Matrix(
        ).view_clip(-100, 100, -100, 100, 1, 1000, 1)

    def update_mesh(self, *args):
        pos = self.pos
        size = self.size
        self.canvas['translate'] = (-pos[0] -
                                    size[0] / 2, -pos[1] - size[1] / 2, -1)

        self.mesh.vertices = [pos[0] + size[0] / 2, pos[1] + size[1] / 2, -1,
                              pos[0] + size[0] / 2 +
                              0.5, pos[1] + size[1] / 2, 0,
                              pos[0] + size[0] / 2 + 0.5, pos[1] +
                              size[1] / 2 + 0.5, 0,
                              pos[0] + size[0] / 2, pos[1] + size[1] / 2 + 0.5, 0]


class SphereApp(App):
    def build(self):
        layout = FloatLayout()
        sphere_widget = SphereWidget(color=(1, 0, 0, 1), radius=1)
        layout.add_widget(sphere_widget)

        return layout


if __name__ == '__main__':
    AreaApp().run()
    DistanceMeasureApp().run()
    DistanceMeasureApp().run()
    MeasureApp().run()
    MeasureViewController().run()
    SphereApp().run()
