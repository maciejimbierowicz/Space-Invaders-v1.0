# imports
from turtle import Screen, Turtle
from player import Player, Bullet
from playsound import playsound
from level import Level
import threading

# Creating game screen
screen = Screen()
screen.title('Space Invaders')
screen.bgcolor('black')
screen.bgpic('images/space1.gif')
screen.listen()
screen.tracer(0)

# Adding player and aliens shapes
screen.addshape('images/ship.gif')
screen.addshape('images/alien1.gif')
screen.addshape('images/explosion1.gif')

# Create player with Turtle
player = Player()
screen.onkey(player.move_right, 'Right')
screen.onkey(player.move_left, 'Left')


# Create the enemies with Turtle
aliens = []
alien_speed = 2


for x in range(24):
    aliens.append(Turtle())


# Position the aliens in their starting positions
def alien_position():
    x = -200
    y = 200
    for alien in aliens:
        alien.showturtle()
        alien.penup()
        alien.shape('images/alien1.gif')
        alien.setx(x)
        alien.sety(y)
        x += 70
        if x > 200:
            x = -200
            y -= 50


# Create alien moving function
def alien_move():
    global alien_speed
    for alien in aliens:
        new_x = alien.xcor() + alien_speed
        alien.setx(new_x)
        if alien.xcor() > 280:
            alien_speed *= -1
            for alienpos in aliens:
                y = alienpos.ycor()
                y -= 10
                alienpos.sety(y)
        elif alien.xcor() < -280:
            alien_speed *= -1
            for alienpos in aliens:
                y = alienpos.ycor()
                y -= 10
                alienpos.sety(y)


# Create bullet ready to fire function
fire = False


def bullet_ready():
    global fire
    if not fire:
        shot.goto(player.xcor(), player.ycor() + 18)
        playsound('sounds/lasershot.wav', False)
        fire = True


# Create bullet with Turtle
shot = Bullet()
shot.goto(player.xcor(), player.ycor() + 18)
screen.onkey(bullet_ready, 'space')

#Create scoreboard from turtle
level = Level()


# Check if bullet touched the alien
def check_damage(invaders, bullet):
    global score
    for invader in invaders:
        if invader.distance(bullet) < 20:
            invader.shape('images/explosion1.gif')
            screen.update()
            playsound('sounds/explosion.wav', False)
            bullet.sety(2000)
            invader.hideturtle()
            invader.sety(1000)
            invader.setx(30)
            score -= 1


def game_over():
    global end
    for alien in aliens:
        if alien.ycor() < -220:
            player.shape('images/explosion1.gif')
            screen.update()
            playsound('sounds/explosion.wav', False)
            end = True


# Add background music
def loop_sound():
    while True:
        playsound('sounds/music.wav', block=True)


loopThread = threading.Thread(target=loop_sound, name='backgroundMusic')
loopThread.daemon = True # shut down music thread when the rest of the program exits
loopThread.start()


# Main Game Loop
score = 24
game_on = True
music_on = False
alien_position()
end = False

while game_on:
    screen.update()
    # Shooting physics
    if fire:
        if shot.ycor() < 300:
            shot.showturtle()
            shot_ycor = shot.ycor()
            shot_ycor += 5
            shot.sety(shot_ycor)
        else:
            shot.hideturtle()
            fire = False
    # Increasing alien speed for the next lvl
    if score == 0:
        alien_position()
        level.next_level()
        score = 24
        alien_speed *= 1.1

    check_damage(invaders=aliens, bullet=shot)
    alien_move()
    game_over()
    if end:
        level.game_over()
        screen.update()
        break

screen.exitonclick()



