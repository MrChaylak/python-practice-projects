# import colorgram
#
# colors = colorgram.extract('scam_art.jpg', 30)
# rgb_list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_tuple = (r, g, b)
#     rgb_list.append(rgb_tuple)
#
# print(rgb_list)
import random
import turtle as t
t.colormode(255)
color_list = [(203, 165, 108), (152, 74, 48), (52, 93, 124), (170, 153, 41), (223, 202, 136), (137, 32, 21), (132, 163, 185), (47, 121, 88), (198, 91, 72), (15, 99, 73), (70, 47, 39), (147, 179, 148), (98, 73, 75), (162, 142, 157), (234, 175, 164), (55, 46, 49), (184, 205, 172), (24, 81, 87), (38, 61, 74), (142, 22, 25), (85, 146, 126), (45, 65, 85), (175, 91, 94), (214, 177, 183), (18, 70, 64), (109, 125, 151)]

tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
x = -230
y = -230
tim.teleport(x, y)
count = 0
for _ in range(100):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    count += 1
    if count == 10:
        y += 50
        tim.teleport(x, y)
        count = 0


screen = t.Screen()
screen.exitonclick()
