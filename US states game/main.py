import turtle
import pandas

screen = turtle.Screen()
data = pandas.read_csv('50_states.csv')
screen.title('U.S. States game')
image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)

correct_guesses = []

while len(correct_guesses) < 50:
    answer = (screen.textinput(title=f'{len(correct_guesses)}/50 correct states', prompt='What is another states name?')
              .title())
    if answer == 'Exit':
        break
    for item in data.state:
        if item == answer:
            tim = turtle.Turtle()
            tim.penup()
            tim.hideturtle()
            new_x = data.loc[data['state'] == item, 'x'].values[0]
            new_y = data.loc[data['state'] == item, 'y'].values[0]
            tim.goto(new_x, new_y)
            tim.write(arg=item, align='center', font=('Arial', 10, 'normal'))
            correct_guesses.append(item)
        else:
            pass

all_states = data.state.to_list()
states_to_learn = []

for item in all_states:
    if item not in correct_guesses:
        states_to_learn.append(item)

dataf = pandas.DataFrame(states_to_learn, columns=["states to learn"])
dataf.to_csv('list.csv', index=False)
