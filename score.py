from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.upload_data()
        self.penup()
        self.goto(0, 265)
        self.update()
        self.hideturtle()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align='center', font=('Arial', 24, 'normal'))

    def increase_score(self):
        self.score += 1
        self.update()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_data()
        self.score = 0
        self.update()

    def upload_data(self):
        with open("data.txt",mode="r") as file:
            self.high_score = int(file.read())

    def update_data(self):
        with open("data.txt",mode="w") as file:
            file.write(f"{self.high_score}")