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

r1 = Rectangle(x=1, y=6, width=10, height=7, color=(100, 200, 125))
r1.draw(canvas)
s1 = Square(x=1, y=3, side=3, color=(0, 100, 222))
s1.draw(canvas)
canvas.make('output/canvas.png')
