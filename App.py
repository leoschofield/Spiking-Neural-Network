from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color,Line, Ellipse
from kivy.uix.gridlayout import GridLayout
from kivy.animation import Animation
from kivy.clock import Clock

OPAQUE = 1
N = 7
class Neuron(Widget):

    def __init__(self,pos,size,x_index,y_index, **kwargs):
        super(Neuron, self).__init__(**kwargs)
        self.pos = pos
        self.x_index = x_index
        self.y_index = y_index
        with self.canvas:
            Color(1, 0, 0,0.5)
            self.Graphic = Ellipse(pos=self.pos, size=size)
            
        Clock.schedule_interval(self.my_callback, 2)

    def my_callback(self,dt):
        print(self.pos)


class Synapse(Widget):
    def __init__(self,pos,size, **kwargs):
        super(Synapse, self).__init__(**kwargs)
        self.pos = pos

        with self.canvas:
            Color(1, 0, 0,0.5)
            self.Graphic = Ellipse(pos=self.pos, size=size)

    def my_callback(self,dt):
        print(self.pos)
        

class IO(Widget):
    def __init__(self,pos,size, **kwargs):
        super(IO, self).__init__(**kwargs)

        with self.canvas:
            Color(1, 1, 1)
            self.Graphic = Ellipse(pos=pos, size=size)


class Touch(Widget):
    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)

    def on_touch_down(self, touch):
        with self.canvas:
            print(touch)


class myApp(App):
    def build(self):
        self.touch = Touch()
        neurons = []
        self.layout = GridLayout(cols = 1, row_force_default = True, row_default_height = 50)

        y_index = 0
        x_index = 0
        for y in range (100,((N+1)*100),100):
            y_index += 1
            for x in range (100,((N+1)*100),100):
                x_index += 1
                temp_neuron = Neuron((x,y),(50,50),x_index,y_index)
                self.layout.add_widget(temp_neuron)
                neurons.append(temp_neuron)

            
        self.layout.add_widget(self.touch)
        return self.layout

 
if __name__ == '__main__':
    myApp().run()