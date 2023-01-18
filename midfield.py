from turtle import Turtle

MIDFIELD_DISTRIBUTION = [(0,360), (0,355), (0,350), (0,330), (0,325), (0,320)]


class Midfield(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.set_midfield()
        self.top_midfield = 360


    def set_midfield(self):
        top_midfield = 360
        while top_midfield >= -340:
            for seg in range(3):
                new_segment = Turtle(shape = "square")
                new_segment.color("white")
                new_segment.up()
                new_segment.shapesize(0.2)
                new_segment.goto(x = 0, y = top_midfield)
                top_midfield -= 5
                self.segments.append(new_segment)
            top_midfield -= 15


            
            




