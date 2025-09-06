import turtle
import argparse

def main():
    parser = argparse.ArgumentParser(description="Draws a Koch snowflake fractal.")
    parser.add_argument("level", type=int, help="The recursion level for the Koch snowflake.")

    args = parser.parse_args()
    recursion_level = args.level

    if recursion_level < 0:
        print("Error: Recursion level cannot be negative.")
        return

    print(f"Drawing Koch snowflake with recursion level {recursion_level}...")

    # Setup turtle
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("white")
    screen.title("Koch Snowflake")
    t = turtle.Turtle()
    t.speed(0)  # Fastest speed
    t.penup()
    t.goto(-200, 100)
    t.pendown()

    def koch_segment(t_obj, length, level):
        if level == 0:
            t_obj.forward(length)
        else:
            length /= 3.0
            koch_segment(t_obj, length, level - 1)
            t_obj.left(60)
            koch_segment(t_obj, length, level - 1)
            t_obj.right(120)
            koch_segment(t_obj, length, level - 1)
            t_obj.left(60)
            koch_segment(t_obj, length, level - 1)

    def koch_snowflake(t_obj, length, level):
        for _ in range(3):
            koch_segment(t_obj, length, level)
            t_obj.right(120)

    koch_snowflake(t, 400, recursion_level)
    screen.mainloop()


if __name__ == "__main__":
    main()