import turtle as turtle_module
import random #for randomly putting colours

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup() # bcz we dont want to see the lines
tim.hideturtle() #for hiding the arrow
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
tim.setheading(225) #setting the starting position
tim.forward(300)
tim.setheading(0) #setting the initial dot's position
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1): #start from 1dot to 100dots
    tim.dot(20, random.choice(color_list)) #now tim turtle will choose random clr from colour list
    tim.forward(50) #going forward with 50space

    if dot_count % 10 == 0: #as the no of dots are 100 so it will go on up to 10,20,30,...,100
        tim.setheading(90) #for second row going right
        tim.forward(50) #from right position go upword
        tim.setheading(180) #
        tim.forward(500)
        tim.setheading(0) #coming to the initial dot's position









screen = turtle_module.Screen()
screen.exitonclick()