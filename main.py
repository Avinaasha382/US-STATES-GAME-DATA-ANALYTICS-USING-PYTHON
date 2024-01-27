import turtle
import pandas
screen = turtle.Screen()

img = "blank_states_img.gif"
screen.addshape(img)
screen.title("US-STATES-GAME")

turtle.shape(img)
statesGuessed = set()
data = pandas.read_csv("50_states.csv")
pen = turtle.Turtle()
pen.hideturtle()
while len(statesGuessed)<50:

    user_input = screen.textinput(title = f"Guess a state: {len(statesGuessed)} / {50}", prompt = "Whats another state's name?")
    user_input = user_input.title()
    print(user_input)

    if user_input in data["state"].to_list():
        
        currState = data[data["state"]==user_input]
        currState_list = currState.iloc[0].to_list()
        print(currState_list)
        statesGuessed.add(user_input)
        pen.penup()
        pen.goto(currState_list[1],currState_list[2])
        pen.write(user_input, align="center", font=("Arial", 10, "normal"))
    
    if user_input == "Exit":
        break

allStates = data["state"].to_list()

statesMissed = []

for state in allStates:
    if state not in statesGuessed:
        statesMissed.append(state)


data_dict = {"States_Missed_From_Guessing":statesMissed}

newData = pandas.DataFrame(data_dict)
newData.to_csv("States_Missed.csv")




    



    
    


   
turtle.mainloop()