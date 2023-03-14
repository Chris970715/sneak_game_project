from turtle import Screen, Turtle

following = [(0,0),(-20, 0),(-40, 0)]

class Snake:

    def __init__(self):
        self.segment = []
        self.set_snake()

    def set_snake(self):

       for position in following:
            self.add_segment(position)

    '''range( start, stop, step)'''
    def move(self):
        for num in range(len(self.segment) - 1, 0, -1):
            self.segment[num].goto(self.segment[num - 1].position())
        self.segment[0].forward(20)

    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segment.append(new_segment)

    def extend(self):
        self.add_segment(self.segment[-1].position())

    def reset(self):
        for seg in self.segment:
            seg.goto(1000,1000)
        self.segment.clear()
        self.set_snake()

    def up(self):
        if self.segment[0].heading() != 270:
            self.segment[0].setheading(90)



    def down(self):
        if self.segment[0].heading() != 90:
            self.segment[0].setheading(270)



    def left(self):
        if self.segment[0].heading() != 0:
            self.segment[0].setheading(180)


    def right(self):
        if self.segment[0].heading() != 180:
            self.segment[0].setheading(0)
