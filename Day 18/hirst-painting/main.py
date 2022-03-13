from random import choice

import colorgram
#
# colours = colorgram.extract('20_001.jpg', 30)
# colour_list = []
# colourT = ()
# for colour in colours:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#
#     newColour = (r, g, b)
#     colour_list.append(newColour)
#
# print(colour_list)

import turtle

colour_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82)]


bob = turtle.Turtle()

bob.penup()
bob.backward(500)
bob.right(90)
bob.forward(300)
bob.left(90)
screen = turtle.Screen()
screen.colormode(255)

for x in range (10):
    for y in range(10):
        bob.pencolor(choice(colour_list))
        bob.dot(20)
        bob.forward(70)
    bob.left(90)
    bob.forward(70)
    bob.right(90)
    bob.backward(700)

screen.exitonclick()

