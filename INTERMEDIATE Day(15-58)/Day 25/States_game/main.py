import turtle
import pandas


screen = turtle.Screen()
screen.title("Indian States Game")
screen.setup(713, 836)
image = "indian_map_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("indian_states.csv")
all_states = data.state.to_list()
guessed_state = []

while len(guessed_state) < 30:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/29 States Correct",
                                    prompt="What's another state name").title()
    if answer_state == "Exit":
        # the above 3-4 line code can also be done by list comprehension
        # missing_state = [state for state in all_states if state not in guessed_state]
        missing_state = []
        for state in all_states:
            if state not in guessed_state:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("missing_state.csv")
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)























# turtle.exitonclick()

# To get the co-ordinates we xan use this function
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()