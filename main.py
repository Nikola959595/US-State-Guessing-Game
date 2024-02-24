import pandas
import turtle
import pygame

#Initialize screen from turtle
screen = turtle.Screen()
screen.setup(725, 491)
screen.title("U.S. States Game")
screen.bgpic("blank_states_img.gif")

#Load and play music from pygame mixer
# pygame.mixer.init()
# pygame.mixer_music.load("Lynyrd Skynyrd - Sweet Home Alabama.wav")
# pygame.mixer_music.play()

data = pandas.read_csv("50_states.csv")

#Convert states and their coords to a list
states_list = data.state.tolist()
states_x = data.x.to_list()
states_y = data.y.to_list()

#Initialize turtle object for writing state names on the screen
timmy = turtle.Turtle()
timmy.penup()
timmy.speed("fastest")
timmy.hideturtle()

#Answer bank for holding the user's guesses to check if they guessed the state already
answer_bank = []
score = 0

#Main game logic
while True:
    answer_state = screen.textinput(f"{score}/50 states guessed", "What's a name of a state?")
    if answer_state is None:
        break
    elif answer_state in answer_bank:
        score += 0      
    elif answer_state in states_list:
        score += 1
        answer_bank.append(answer_state)
        index = states_list.index(answer_state)
        timmy.goto(states_x[index], states_y[index])
        timmy.write(f"{answer_state}", "True", "center", ("Courier", 8, "normal"))
    elif score == 50:
        break    


          
