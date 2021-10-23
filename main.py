from canvas import Canvas
from shapes import Rectangle, Square

# Canvas width and height
canvas_width = int(input("Canvas width: "))
canvas_height = int(input("Canvas height: "))

# Canvas color: Black or White
colors = {"white": (255, 255, 255), "black": (0, 0, 0)}
canvas_color = input("Canvas color, black or white? ")

# Create a canvas
canvas = Canvas(width=canvas_width, height=canvas_height, color=colors[canvas_color])

# Ask the number of shapes to be drawn
number_shapes = int(input("How many shapes would you like to draw? "))

# Draw the shapes by asking the user what he/she wants to draw
for i in range(number_shapes):
    print(f"Shape #{i + 1}: ")
    shape_type = input("Rectangle or Square? ")
    if shape_type.lower() == "rectangle":
        x = int(input("x of the top left corner: "))
        y = int(input("y of the top left corner: "))
        width = int(input("Width of the rectangle: "))
        height = int(input("Height of the rectangle: "))
        red = int(input("Intensity of red portion of the color [0, 255]: "))
        green = int(input("Intensity of green portion of the color [0, 255]: "))
        blue = int(input("Intensity of blue portion of the color [0, 255]: "))

        # Create the rectangle
        r = Rectangle(x, y, width, height, color=(red, green, blue))
        r.draw(canvas)

    if shape_type.lower() == "square":
        x = int(input("x of the top left corner: "))
        y = int(input("y of the top left corner: "))
        side = int(input("Side of the square: "))
        red = int(input("Intensity of red portion of the color [0, 255]: "))
        green = int(input("Intensity of green portion of the color [0, 255]: "))
        blue = int(input("Intensity of blue portion of the color [0, 255]: "))

        # Create the square
        s = Square(x, y, side, color=(red, green, blue))
        s.draw(canvas)

canvas.make('output/canvas.png')
