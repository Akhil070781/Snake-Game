import turtle

y_cor=[0,-20,-40]

class Snake:
    def __init__(self):    
        self.snake=[]    
        self.create_snake()
        self.head=self.snake[0]
    
    def create_snake(self):
        for _ in range(3):
            new_piece=turtle.Turtle(shape="square")
            new_piece.color("white")
            new_piece.penup()
            new_piece.goto(x=y_cor[_],y=0)
            (self.snake).append(new_piece)   
            
    def add_end(self):
        new_piece=turtle.Turtle(shape="square")
        new_piece.color("white")
        new_piece.penup()
        new_piece.goto(x=self.snake[-1].xcor(),y=self.snake[-1].ycor())
        (self.snake).append(new_piece)      
        
    def reset(self):
        for seg in self.snake:
            seg.goto(1000,1000)
        self.snake.clear()
        self.create_snake()   
        self.head=self.snake[0]
             
        
    def move(self):        
        for seg_no in range(len((self.snake))-1,0,-1):
            (self.snake)[seg_no].goto(x=(self.snake)[seg_no-1].xcor(),y=(self.snake)[seg_no-1].ycor())
        (self.head).forward(20)
        
    def up(self):
        if (self.head).heading()!=270:
            (self.head).setheading(90)
    
    def down(self):
        if (self.head).heading()!=90:
            (self.head).setheading(270)
        
    def left(self):
        if (self.head).heading()!=0:
            (self.head).setheading(180)

    def right(self):
        if (self.head).heading()!=180:
            (self.head).setheading(0)
        