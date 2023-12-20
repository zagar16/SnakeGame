from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            contents = file.read()
            self.high_score = int(contents)
        self.color("red")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score is: {self.score} High score: {self.high_score}", align="center", font=("Arial", 16, "normal"))

    def scoreboard(self):
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
        # self.goto(0, 0)
        # self.color("red")
        # self.write(f"GAME OVER", align="center", font=("Arial", 16, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()





