# Simple Python AGAR.IO Game (Single Player) Demo by @TokyoEdTech
# YouTube Python Tutorial Channel: 
# https://www.youtube.com/channel/UC2vm-0XX5RkWCXWwtBZGOXg/playlists
# Use the arrow keys to move your player and eat the smaller enemies
# While avoiding the bigger enemies
# NOTE: This is a work in progress so there is some ugly code
import turtle
import random
import math
import os
import time
 
#Set up screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("AGAR.IO Single Player")
wn.setup(900, 900)
 
class Game(turtle.Turtle):
 
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(5)
        self.color("white")
        self.goto(-390, 380)
        self.score = 0
        self.x_offset = 0
        self.y_offset = 0
        self.world_size = 500
        self.colors = ["red", "orange", "green", "blue", "yellow", "purple"]
        self.high_score = 0
 
    def show_score(self):
        self.clear()
        msg = "Score: {} Enemies  Remaining: {}  High Score: {}".format(int(self.score), len(enemies), int(self.high_score))
        self.write(msg, False, align="left", font=("Arial",14, "normal"))
 
    def change_score(self, points):
        self.score += points
        self.show_score()
 
    def play_sound(self, filename):
        os.system("afplay {}&".format(filename))
 
class Player(turtle.Turtle):  #Player
 
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(20)
        self.shape("circle")  
        self.color("white")
        self.speed = 3.5
        self.size = 2.0
 
    def move(self):
        pass
 
        #Border Checking for the Player
        if self.xcor() > game.world_size: 
            self.setx(game.world_size)
            self.left(180)
                    
        if self.xcor() < -game.world_size:
            self.setx(-game.world_size)
            self.left(180)
            
        if self.ycor() > game.world_size:
            self.sety(game.world_size)
            self.left(180)
            
        if self.ycor() < -game.world_size:
            self.sety(-game.world_size)
            self.left(180)
    
    #What happens if the user presses the left arrow?
    def left_arrow(self):
        x = self.xcor()
        self.setx(x - 30)
 
    #What happens if the user presses the right arrow?
    def right_arrow(self):
        x = self.xcor()
        self.setx(x + 30)
 
    #What happens if the user presses the up arrow?
    def up_arrow(self):
        y = self.ycor()
        self.sety(y + 30)
 
    #What happens if the user presses the down arrow?
    def down_arrow(self):
        y = self.ycor()
        self.sety(y - 30)
        
    def set_size(self, size):
        #Set the size
        self.size = size
        #Change the size that is shown
        self.shapesize(stretch_wid=size, stretch_len=size, outline=None)
 
 
class Enemy(turtle.Turtle):
 
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.color(random.choice(game.colors))
        self.shape("circle")
        self.speed = 3
        self.size = float(random.randint(5, 15)) / 10
        self.shapesize(stretch_wid=self.size, stretch_len=self.size, outline=None)
        self.goto(random.randint(-game.world_size, game.world_size), random.randint(-game.world_size, game.world_size))
        self.setheading(random.randint(0, 360))
        
    def move(self):
        self.forward(self.speed)
        self.setx(self.xcor() + game.x_offset)
        self.sety(self.ycor() + game.y_offset)
 
        #Border Checking for the Enemy
        if self.xcor() > game.world_size: 
            self.setx(game.world_size)
            self.left(180)
                    
        if self.xcor() < -game.world_size:
            self.setx(-game.world_size)
            self.left(180)
            
        if self.ycor() > game.world_size:
            self.sety(game.world_size)
            self.left(180)
            
        if self.ycor() < -game.world_size:
            self.sety(-game.world_size)
            self.left(180)
            
        #Simple AI
        #Randomly set heading towards player if the player is smaller
        #ATTACK
        if random.randint(1, 100) == 50 and player.size < self.size:
            #print ("ATTACK")
            #Four options
            attack_heading = self.get_heading(player)
            self.setheading(attack_heading)
 
        #Randomly set heading away from player if the player is bigger      
        #RUN
        if random.randint(1, 1000) == 50 and player.size > self.size:
            #print ("RUN")
            #Four options
            attack_heading = self.get_heading(player)
            run_heading = attack_heading + 180
            self.setheading(run_heading)
 
    def get_heading(self, other):
        if player.xcor() > self.xcor() and player.ycor() > self.ycor():
            return 45
 
        if player.xcor() < self.xcor() and player.ycor() > self.ycor():
            return 135
 
        if player.xcor() < self.xcor() and player.ycor() < self.ycor():
            return 225
 
        if player.xcor() > self.xcor() and player.ycor() < self.ycor():
            return 315      
            
    def set_size(self, size):
        #Update self size variable
        self.size = size
        #Change display size
        self.shapesize(stretch_wid=size, stretch_len=size, outline=None)
 
    def destroy(self):
        self.clear()
        self.hideturtle()
        self.goto(10000, 10000)     
 
#Collision checking function
#Uses the Pythagorean Theorem to Measure The Distance Between Two Objects
def isCollision(t1, t2):
    a = t1.xcor()-t2.xcor()
    b = t1.ycor()-t2.ycor()
    distance = math.sqrt((a ** 2) + (b ** 2))
    
    #Calculate Gap based on size of object
    gap = ((t1.size * 20.0) + (t2.size * 20.0)) / 2.0
 
    if distance < gap:
        return True
    else:
        return False
 
#Create class instances
player = Player()
game = Game()
 
#Create multiple enemies
enemies = []
for count in range(50):
    enemies.append(Enemy())
    
#Show the score
game.show_score()
 
#Set keyboard bindings
turtle.listen()
turtle.onkey(player.left_arrow, "Left")
turtle.onkey(player.right_arrow, "Right")
turtle.onkey(player.up_arrow, "Up")
turtle.onkey(player.down_arrow, "Down")
 
#Speed Up the Game
wn.tracer(0)
 
#Main Loop
while True:
    wn.update()
    player.move()
 
    #Iterate through enemies
    for enemy in enemies:
        enemy.move()
 
        #Check for a collision between the player and goal
        if isCollision(player, enemy):
            #Compare sizes
            #Player is larger
            if player.size >= enemy.size:
                #Hide the enemy
                enemy.hideturtle()
                enemy.goto(10000, 10000)
                #Increase the player size
                player.set_size(player.size + (enemy.size / 2))
                #Update the score
                game.change_score(enemy.size * 100)
                #Remove the enemy from the list of enemies
                enemies.remove(enemy)
 
            else:
                game.clear()
                game.write("GAME OVER...GAME OVER...GAME OVER", False, align="left", font=("Arial",14, "normal"))
                wn.update()
                time.sleep(1)
                for enemy in enemies:
                    enemy.destroy()
                enemies = []
                #Create multiple enemies
                enemies = []
                for count in range(50):
                    enemies.append(Enemy())
                player.set_size(1)
                if game.score > game.high_score:
                    game.high_score = game.score
                game.score = 0
                
                
    #Iterate through enemies and see if they collide with each other
    for enemy in enemies:
        for enemy2 in enemies:
            if enemy != enemy2:
                if isCollision(enemy, enemy2):
                    if enemy.size > enemy2.size:
                        #Hide the enemy2
                        enemy2.destroy()
                        #Increase the enemy size
                        enemy.set_size(enemy.size + (enemy2.size / 1.5))
                        #Remove enemy2 from the list of enemies
                        enemies.remove(enemy2)
                        break
                    else:
                        #Hide enemy2
                        enemy.destroy()
                        #Increase the enemy size
                        enemy2.set_size(enemy.size + (enemy2.size / 1.5))
                        #Remove enemy2 from the list of enemies
                        enemies.remove(enemy)
                        break
                        
    game.show_score()
    #Check to see how many enemies are still in the game
    if len(enemies) == 0:
        game.clear()
        game.write("Congratulations - you win!", False, align="left", font=("Arial",14, "normal"))
        wn.update()
        time.sleep(1)
        enemies = []
        #Create multiple enemies
        enemies = []
        for count in range(50):
            enemies.append(Enemy())
        player.set_size(1)
        #Set High Score
        if game.score > game.high_score:
            game.high_score = game.score
        game.score = 0