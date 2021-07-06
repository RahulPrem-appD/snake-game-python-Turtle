from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 280)
        self.current_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.write(f"Score: {self.current_score}", move=False, align="center", font=("Courier", 12, "normal"))

    def update_score(self):
        self.current_score += 1
        self.undo()
        self.write(f"Score: {self.current_score}", move=False, align="center", font=("Courier", 12, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align="center", font=("Courier", 12, "normal"))