# Import the Turtle Graphics module
import turtle
import random

# Define program constants
WIDTH=500
HEIGHT=500
DELAY= 150 # Milliseconds between screen updates
FOOD_SIZE = 25

offsets = {
    "up": (0, 20),
    'down': (0, -20),
    'left': (-20, 0),
    'right': (20, 0)
}


def bind_direction_keys():
    screen.onkey(lambda: set_snake_directon("up"), "Up")
    screen.onkey(lambda: set_snake_directon("right"), "Right")
    screen.onkey(lambda: set_snake_directon("down"), "Down")
    screen.onkey(lambda: set_snake_directon("left"), "Left")


def set_snake_directon(direction):
    global snake_direction
    if (direction == "up"):
        if (snake_direction != "down"): # No self collision
            snake_direction = "up"
    elif (direction == "down"):
        if (snake_direction != "up"): # No self collision
            snake_direction = "down"
    elif (direction == "left"):
        if (snake_direction != "right"): # No self collision
            snake_direction = "left"
    elif (direction == "right"):
        if (snake_direction != "left"): # No self collision
            snake_direction = "right"


def game_loop():
    stamper.clearstamps() # Remove existing stamps made my stamper

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0] # x coord
    new_head[1] += offsets[snake_direction][1] # y coord


    # Check collisions
    if new_head in snake or new_head[0] < - WIDTH / 2 or new_head[0] > WIDTH / 2 \
        or new_head[1] < - HEIGHT / 2 or new_head[1] > HEIGHT / 2:
        reset() # closes the program
    else:
        # Add new head to snake body
        snake.append(new_head)

        # check for food collision
        if not food_collision():
            snake.pop(0) # Keep the snake the same length unless fed


        # Draw snake for first time
        for segment in snake:
            stamper.goto(segment[0], segment[1])
            stamper.stamp()

        # Refresh Screen
        screen.title(f'Snake Crossing. Score: {score}')
        screen.update()

        # Rinse and repeat
        turtle.ontimer(game_loop, DELAY)

    
def food_collision():
    global food_pos, score
    if get_distance(snake[-1], food_pos) < 20:
        score += 1 # Increment score
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        return True
    return False


def get_random_food_pos():
    x = random.randint(- WIDTH / 2 + FOOD_SIZE, WIDTH / 2 - FOOD_SIZE)
    y = random.randint(- HEIGHT / 2 + FOOD_SIZE, HEIGHT / 2 - FOOD_SIZE)
    return (x,y)


def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2-y1) ** 2 + (x2 - x1) ** 2) ** 0.5 # Pythagorus' Theorem
    return distance


def reset():
    global score, snake, snake_direction, food_pos
    # Create snake as a list of coordinate pairs
    snake = [[0,0], [20,0], [40,0], [60,0]]
    snake_direction = "up"
    score = 0
    food_pos = get_random_food_pos()
    food.goto(food_pos)
    game_loop()


# Create the window used for drawing
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT) # Sets the dimensions for the Turtle Graphics Window
screen.title('Snake Crossing')
screen.bgcolor('black')
screen.tracer(0) # Turns off automatic animation


# Event Handlers
screen.listen()

# Specify event callbacks # (function callback, key it responds to)
bind_direction_keys()


# create a turtle to do my bidding
stamper = turtle.Turtle()
stamper.shape('circle')
stamper.color('green')
stamper.penup()

# Draw snake for first time
# for segment in snake:
#     stamper.goto(segment[0], segment[1])
#     stamper.stamp()

# Food
food = turtle.Turtle()
food.shape('triangle')
food.shapesize(FOOD_SIZE / 20)
food.color('orange')
food.penup()

# Set animation in motion
reset()

# Finish nicely
turtle.done()

# Updates: 
# Increase speed every time score increases
# Use images to better visualize snake object