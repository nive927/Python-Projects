# CODE: to extract the colors from a
# Hirst Painting using colorgram package
#
# import colorgram
#
# # returns a list of 100 colors as Color gram objects extracted from the image
# colors_in_image = colorgram.extract("image.jpg", 100)
#
# colors_in_image_rgb = list()
#
# # Color objects have the rgb attribute
# for color_obj in colors_in_image:
#     # colors_in_image_rgb.append(color_obj.rgb)
#     r = color_obj.rgb.r
#     g = color_obj.rgb.b
#     b = color_obj.rgb.g
#     colors_in_image_rgb.append((r, g, b))
#
# print(colors_in_image_rgb)

colors_in_image_rgb = [(246, 243, 245), (233, 246, 239), (246, 242, 239), (240, 243, 246), (132, 205, 166), (221, 106, 148), (32, 61, 42), (199, 148, 135), (166, 48, 58), (141, 162, 184), (39, 157, 105), (237, 90, 212), (150, 66, 59), (216, 71, 82), (168, 33, 29), (235, 157, 165), (51, 90, 111), (35, 55, 61), (156, 31, 33), (17, 71, 97), (52, 49, 44), (230, 166, 161), (170, 221, 188), (57, 48, 51), (184, 113, 103), (32, 109, 60), (105, 159, 126), (175, 188, 200), (34, 210, 151), (65, 56, 66), (106, 124, 140), (153, 227, 202), (48, 71, 69), (131, 121, 128)]

# circle size: 20
# space: 50 apart
# 10 X 10 image

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(colors_in_image_rgb))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()