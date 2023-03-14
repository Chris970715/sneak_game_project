from turtle import Screen, Turtle
import time
from snake_body import Snake
from food import Food
from score import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake Game")
screen.tracer(0)

game_is_on = True


snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


while(game_is_on):
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with the food obejct
    if (snake.segment[0].distance(food) < 15):
        food.refresh()
        snake.extend()
        score.increase_score()

    if (snake.segment[0].xcor() > 300 or snake.segment[0].xcor() < -300 or snake.segment[0].ycor() > 300 or snake.segment[0].ycor() < -300):
        score.reset()
        snake.reset()



    # Detect collision with tail
    for segment in snake.segment[1:]:
        if ((snake.segment[0].distance(segment) < 10) ):
            score.reset()
            snake.reset()

screen.exitonclick()