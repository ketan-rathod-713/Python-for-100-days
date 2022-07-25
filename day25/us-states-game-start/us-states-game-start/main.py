
# Turtle only works with gif file not png or anything

import turtle
import pandas

screen = turtle.Screen()
screen.title("Us states quiz")
image = "blank_states_img.gif"
screen.addshape(image) # shape to add in screen

turtle.shape(image) # now i can use that image as it is in screen `

# Now solve this
# First read the csv file
data = pandas.read_csv("50_states.csv")

# How to get the coordinates of the screen

def get_mouse_click_coor(x,y):
    print(x, y)

    # To get the text input
    answer_state = screen.textinput(title="Guess the state", prompt="What is another states name ?")
    print(answer_state)
    states_list = data["state"].to_list()
    print(states_list)
    for state_name in states_list:
        if(state_name == answer_state):
            # get the data of that state
            req_state_data = data[data.state == state_name] # bracket ke andar where condition where data.state == state_name or whatever column
            print(req_state_data)
            # Now that we got the state now make a turtle and let it go there , place turtle on the x and y location
            turtle_state_name = turtle.Turtle()
            turtle_state_name.hideturtle()
            turtle_state_name.penup()
            turtle_state_name.goto(int(req_state_data.x),int(req_state_data.y))
            turtle_state_name.write(state_name)


    # return x, y , this was not working but ig now I can do my whole stuff here so let's do it

coordinates_clicked = turtle.onscreenclick(get_mouse_click_coor) # it will pass the coordinates where it get clicked by this call back function
# print(coordinates_clicked) Not working !!






# find in a list of states


# for state_name in states_list:
#     if(answer_state == state_name && ):


# screen.exitonclick() Here we are going to click on the screen so it will stop so
screen.mainloop()
