import random
import turtle as t

t.bgcolor('yellow')

#mato
caterpillar = t.Turtle()
caterpillar.shape('square')
caterpillar.color('red')
caterpillar.speed(0)
caterpillar.penup()
caterpillar.hideturtle()
#lehti
leaf = t.Turtle()
leaf_shape = ((0, 0), (14, 2), (18, 6), (20, 20), \
              (6, 18), (2, 14))
t.register_shape('leaf', leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.hideturtle()
leaf.speed(0)

#kivi
rock = t.Turtle()
rock_shape = ((-10,20),(10,20),(20,10),(20,-10),(10,-20),(-10,-20),(-20,-10),(-20,10))
t.register_shape('rock', rock_shape)
rock.shape('rock')
rock.color('grey')
rock.penup()
rock.hideturtle()
rock.speed(0)

#arrow
arrow = t.Turtle()
arrow_shape = ((-15,7.5),(-10,0),(-15,-7.5),(5,-7.5),(15,0),(5,7.5))
t.register_shape('arrow', arrow_shape)
arrow.shape('arrow')
arrow.color('grey')
arrow.penup()
arrow.hideturtle()
arrow.speed(0)

#tekstit
#aloitus
game_started = False
text_turtle = t.Turtle()
text_turtle.write('aloita painamalla space näppäintä', align='center', \
                  font=('Arial', 16, 'bold'))
text_turtle.hideturtle()

#score
score_turtle = t.Turtle()
score_turtle.hideturtle
score_turtle.speed(0)



def outside_window():
    left_wall = -t.window_width() / 2
    right_wall = t.window_width() / 2
    top_wall = t.window_height() / 2
    bottom_wall = -t.window_height() / 2
    (x, y) = caterpillar.pos()
    outside = \
            x< left_wall or \
            x> right_wall or \
            y< bottom_wall or \
            y> top_wall
    return outside

def game_over():
    caterpillar.color('yellow')
    leaf.color('yellow')
    rock.color('yellow')
    arrow.color('yellow')
    t.penup()
    t.hideturtle()
    t.write('GAME OVER!', align='center', font=('Arial', 16, 'bold'))

def display_score(current_score):
    score_turtle.clear()
    score_turtle.penup()
    x = (t.window_width() / 2) - 50
    y = (t.window_height() / 2) - 55
    score_turtle.setpos(x, y)
    score_turtle.write(str(current_score), align='right', \
                       font=('Arial', 40, 'bold'))

def place_leaf():
    leaf.ht()
    leaf.setx(random.randint(-200, 200))
    leaf.sety(random.randint(-200, 200))
    leaf.st()

def place_rock():
    rock.ht()
    rock.setx(random.randint(-200, 200))
    rock.sety(random.randint(-200, 200))
    rock.st()

def place_arrow():
    arrow.ht()
    arrow.setx(random.randint(-200, 200))
    arrow.sety(random.randint(-200, 200))
    arrow.st()

def start_game():
    global game_started
    if game_started:
        return
    game_started = True

    score = 0
    text_turtle.clear()

    caterpillar_speed = 2
    caterpillar_lenght = 3
    caterpillar.shapesize(1, caterpillar_lenght, 1)
    caterpillar.showturtle()
    display_score(score)
    place_leaf()
    place_rock()
    place_arrow()

    while True:
        caterpillar.forward(caterpillar_speed)
        if caterpillar.distance(leaf) < 20:
            place_leaf()
            caterpillar_lenght += 1
            caterpillar.shapesize(1, caterpillar_lenght, 1)
            caterpillar_speed = caterpillar_speed + 1
            score += 10
            display_score(score)
            
        if caterpillar.distance(rock) < 38:
            game_over()
            
        if caterpillar.distance(arrow) < 35:
            game_over()
        
        if outside_window():
            game_over()
            break

def move_up():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(90)
        
def move_down():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(270)

def move_left():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(180)

def move_right():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(0)
        
t.onkey(start_game, 'space')
t.onkey(move_up, 'Up')
t.onkey(move_down, 'Down')
t.onkey(move_left, 'Left')
t.onkey(move_right, 'Right')
t.listen()
t.mainloop()
