import turtle as t
count = int(input())
def sanjiaoxing(san):
    t.penup()
    t.goto(san[0])
    t.pendown()
    t.goto(san[1])
    t.goto(san[2])
    t.goto(san[0])
def get_mid(a, b):
    x = (a[0] + b[0]) / 2
    y = (a[1] + b[1]) / 2
    return [x, y]
def draw_san(size, i):
    sanjiaoxing(size)
    if i > 0:
        size2 = [size[0], get_mid(size[0], size[1]), get_mid(size[0], size[2])]
        draw_san(size2, i - 1)
        size3 = [get_mid(size[0], size[2]), get_mid(size[1], size[2]), size[2]]
        draw_san(size3, i - 1)
        size4 = [get_mid(size[0], size[1]), size[1], get_mid(size[1], size[2])]
        draw_san(size4, i - 1)
def main():
    t.penup()
    t.left(90)
    t.forward(350)
    t.pendown()
    t.write("Треугольник Серпинского", False, выровнять="center", font=(" ", 20, "normal"))
t.speed(100)
points = [[-200, 0], [200, 0], [0, 300]]
draw_san(points, count)
t.exitonclick()



