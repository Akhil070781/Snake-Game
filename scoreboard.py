from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self) :
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x=0,y=280)
        self.color("white")
        self.score=0
        with open("data.txt") as file:
            self.highscore=int(file.read())
        self.write(arg=f"Score :{self.score}  High Score: {self.highscore}",move=False,align="center",font=("Arial",13,"normal"))
    
    def update(self):
        self.score+=1
        self.clear()    
        self.write(arg=f"Score :{self.score}  High Score: {self.highscore}",move=False,align="center",font=("Arial",13,"normal"))
    
    def write_score(self):
        self.clear()    
        self.write(arg=f"Score :{self.score}  High Score: {self.highscore}",move=False,align="center",font=("Arial",13,"normal"))
    # def game_over(self):
    #     self.home()
    #     self.clear()           
    #     self.write(arg=f"GAME OVER !! Score :{self.score}",move=False,align="center",font=("Arial",13,"normal"))
        
    def reset(self):
        if self.score>(self.highscore):
            self.highscore= (self.score)
        self.score=0
        with open("data.txt",mode='w') as file:
            file.write(f"{self.highscore}")

        