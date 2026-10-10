# Warm-up: the program crashes before anyone clicks. Why?
import turtle


def say_hello(x, y):
    print("Hello")


turtle.shape("turtle")
turtle.onclick(say_hello())
turtle.done()
