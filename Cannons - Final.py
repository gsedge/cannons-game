#imports all needed modules
import pygame
import random
import math
import tkinter as tk
import threading
 
#initialises pygame
pygame.init()


class Configuration:
    def __init__(self):
        global window, clock

        #loads all essential values in
        self.screenX = 1000
        self.screenY = 800

        window = pygame.display.set_mode((self.screenX, self.screenY))
        pygame.display.set_caption("CANNONS")
        clock = pygame.time.Clock()
        self.wanna_leave = False

        #loads in colours
        self.white = (250, 250, 250)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.grey = (130, 134, 148)

        #loads in fonts from pygame
        self.smalltext = pygame.font.SysFont("arial", 35)
        self.mediumtext = pygame.font.SysFont("arial", 50)
        self.bigtext = pygame.font.SysFont("mistral", 80)
        self.biggertext = pygame.font.SysFont("arial", 85)

        #loads in external media
        self.load_misc()
        self.load_cannons()
        self.level1_load()
        self.level2_load()
        self.level3_load()
        self.level4_load()
        self.level5_load()

    def load_misc(self):
        #loads in all random media
        self.menu_background = pygame.transform.scale((pygame.image.load("Data/misc/menu-background.jpg"))
                            , (self.screenX, self.screenY))
        
        self.rule_background = pygame.transform.scale((pygame.image.load("Data/misc/menu-background-rules.jpg"))
                            , (self.screenX, self.screenY))
        
        self.back_button = pygame.transform.scale((pygame.image.load("Data/misc/back.png")), (200, 100))
        
        self.firebutton = pygame.transform.scale((pygame.image.load("Data/misc/firebutton.jpg")), (150, 150))
        self.firebutton.set_colorkey((255, 255, 255))

        self.locked = pygame.image.load("Data/misc/locked.png")
        self.locked.set_colorkey((255, 255, 255))
        
        self.unlocked = pygame.image.load("Data/misc/unlocked.png")
        self.unlocked.set_colorkey((255, 255, 255))

        self.explosion = pygame.image.load("Data/misc/explosion.png")
        self.explosion.set_colorkey((255, 255, 255))

    def load_cannons(self):
        #loads in all the cannon pictures
        self.cannon1 = pygame.transform.scale((pygame.image.load("Data/cannons/cannon1.png")), (200, 100))
        self.cannon1.set_colorkey((255, 255, 255))

        self.cannon2 = pygame.transform.scale((pygame.image.load("Data/cannons/cannon2.png")), (200, 100))
        self.cannon2.set_colorkey((255, 255, 255))

        self.cannon3 = pygame.transform.scale((pygame.image.load("Data/cannons/cannon3.png")), (200, 100))
        self.cannon3.set_colorkey((255, 255, 255))

        self.cannon4 = pygame.transform.scale((pygame.image.load("Data/cannons/cannon4.png")), (200, 100))
        self.cannon4.set_colorkey((255, 255, 255))
        
    def level1_load(self):
        #loads in media specific to level 1
        self.level1_background = pygame.transform.scale((pygame.image.load("Data/1/background.jpg"))
                                , (self.screenX, self.screenY))
        
        self.level1_backgroundsnippet = pygame.transform.scale((pygame.image.load("Data/1/snippet.jpg"))
                                , (200, self.screenY))

        self.enemy1 = pygame.transform.scale((pygame.image.load("Data/1/enemy.png")), (150, 200))
        self.enemy1.set_colorkey((255, 255, 255))

    def level2_load(self):
        #loads in media specific to level 2
        self.level2_background = pygame.transform.scale((pygame.image.load("Data/2/background.png"))
                                , (self.screenX, self.screenY))
        
        self.level2_backgroundsnippet = pygame.transform.scale((pygame.image.load("Data/2/snippet.jpg"))
                                        , (200, self.screenY))

        self.enemy2 = pygame.transform.scale((pygame.image.load("Data/2/enemy.png")), (150, 200))
        self.enemy2.set_colorkey((255, 255, 255))

    def level3_load(self):
        #loads in media specific to level 3
        self.level3_background = pygame.transform.scale((pygame.image.load("Data/3/background.jpg"))
                                , (self.screenX, self.screenY))
        
        self.level3_backgroundsnippet = pygame.transform.scale((pygame.image.load("Data/3/snippet.jpg"))
                                , (200, self.screenY))

        self.enemy3 = pygame.transform.scale((pygame.image.load("Data/3/enemy.png")), (150, 200))
        self.enemy3.set_colorkey((255, 255, 255))

    def level4_load(self):
        #loads in media specific to level 4
        self.level4_background = pygame.transform.scale((pygame.image.load("Data/4/background.jpg"))
                                , (self.screenX, self.screenY))
        
        self.level4_backgroundsnippet = pygame.transform.scale((pygame.image.load("Data/4/snippet.jpg"))
                                , (200, self.screenY))

        self.enemy4 = pygame.transform.scale((pygame.image.load("Data/4/enemy.png")), (150, 200))
        self.enemy4.set_colorkey((255, 255, 255))

    def level5_load(self):
        #loads in media specific to level 5
        self.level5_background = pygame.transform.scale((pygame.image.load("Data/5/background.png"))
                                , (self.screenX, self.screenY))
        self.level5_backgroundsnippet = pygame.transform.scale((pygame.image.load("Data/5/snippet.png"))
                                , (200, self.screenY))

        self.enemy5 = pygame.transform.scale((pygame.image.load("Data/5/enemy.png")), (80, 145))
        self.enemy5.set_colorkey((255, 255, 255))

    def start(self, stage):
        #moves to stage where user can select level
        if stage == "SELECT":
            global select
            select = SelectStage()

    def mouse_pos(self):
        #gets position of mouse and returns it
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        return [x, y]

    def draw(self, stage):
        #selects what subroutine is needed for what stage of the game the user is at
        if stage == "MENU":
            menu.draw()
        elif stage == "SELECT":
            select.draw()
        elif stage == "PLAY":
            play.draw()
        else:
            finish.draw()

        pygame.display.flip()


class MenuStage:
    def __init__(self):
        #sets key values
        self.type = "MENU"

        #creates boxes
        self.play_rect = pygame.Rect(350, 300, 300, 100)
        self.rule_rect = pygame.Rect(350, 450, 300, 100)
        self.exit_rect = pygame.Rect(350, 600, 300, 100)

        #creates back button
        self.back_button = pygame.Rect(0, 0, 200, 100)

        #creates text needed
        self.cannon_text = con.biggertext.render("C A N N O N S", 5, con.white)
        self.play_text = con.bigtext.render("PLAY", 5, con.black)
        self.rule_text = con.bigtext.render("RULES" , 5, con.black)
        self.exit_text = con.bigtext.render("EXIT" , 5, con.black)

    def back(self):
        #moves stage back to menu
        self.type = "MENU"

    def draw(self):
        if self.type == "MENU":
            #gets position of mouse
            pos = con.mouse_pos()

            #draws background
            window.blit(con.menu_background, (0, 0, 0, 0))
            
            #draws cannon text
            window.blit(self.cannon_text,  (276, 115, 0, 0))

            #draws play box
            if self.play_rect.collidepoint(pos):
                #changes colour of box outline if mouse is over it
                pygame.draw.rect(window, con.blue, self.play_rect, 6)
            else:
                pygame.draw.rect(window, con.black, self.play_rect, 6)
                
            pygame.draw.rect(window, con.white, self.play_rect)
            window.blit(self.play_text, (425, 315, 0, 0))

            #draws rule box
            if self.rule_rect.collidepoint(pos):
                #changes colour of box outline if mouse is over it
                pygame.draw.rect(window, con.blue, self.rule_rect, 6)
            else:
                pygame.draw.rect(window, con.black, self.rule_rect, 6)
                
            pygame.draw.rect(window, con.white, self.rule_rect)
            window.blit(self.rule_text, (412, 465, 0, 0))

            #draws exit box
            if self.exit_rect.collidepoint(pos):
                #changes colour of box outline if mouse is over it
                pygame.draw.rect(window, con.blue, self.exit_rect, 6)
            else:
                pygame.draw.rect(window, con.black, self.exit_rect, 6)
            pygame.draw.rect(window, con.white, self.exit_rect)
            window.blit(self.exit_text, (427, 615, 0, 0))

        else:
            #draws background
            window.blit(con.rule_background, (0, 0, 0, 0))
            window.blit(con.back_button, (0, 0, 0, 0))

class SelectStage:
    def __init__(self):
        #sets needed variables for this stage
        global stage
        stage = "SELECT"
        self.back_button = pygame.Rect(0, 0, 200, 100)

        #creates text
        self.level1_text = con.smalltext.render("LEVEL 1", 5, con.red)
        self.level2_text = con.smalltext.render("LEVEL 2", 5, con.red)
        self.level3_text = con.smalltext.render("LEVEL 3", 5, con.red)
        self.level4_text = con.smalltext.render("LEVEL 4", 5, con.red)
        self.level5_text = con.smalltext.render("LEVEL 5", 5, con.red)

        #creates pane boxes
        self.pane1_box = pygame.Rect(0, 100, 200, 800)
        self.pane2_box = pygame.Rect(200, 0, 200, 800)
        self.pane3_box = pygame.Rect(400, 0, 200, 800)
        self.pane4_box = pygame.Rect(600, 0, 200, 800)
        self.pane5_box = pygame.Rect(800, 0, 200, 800)

    def back(self):
        #returns to the menu from the select stage
        global stage
        stage = "MENU"
        
    def draw(self):
        #draws pane 1
        window.blit(con.level1_backgroundsnippet, (0, 0, 0, 0))
        window.blit(self.level1_text, (42, 500, 0, 0))

        #draws pane 2
        window.blit(con.level2_backgroundsnippet, (200, 0, 0, 0))
        window.blit(self.level2_text, (242, 500, 0, 0))

        #draws pane 3
        window.blit(con.level3_backgroundsnippet, (400, 0, 0, 0))
        window.blit(self.level3_text, (442, 500, 0, 0))

        #draws pane 5
        window.blit(con.level4_backgroundsnippet, (600, 0, 0, 0))
        window.blit(self.level4_text, (642, 500, 0, 0))

        #draws pane 3
        window.blit(con.level5_backgroundsnippet, (800, 0, 0, 0))
        window.blit(self.level5_text, (842, 500, 0, 0))
        
        #draws back button
        window.blit(con.back_button, (0, 0, 0, 0))


class PlayStage:
    def __init__(self, level):
        #states initial values for the play stage
        self.level = level
        self.score = 50
        self.selecting = False
        self.flying = False
        self.firebutton = [pygame.Rect(800, 610, 150, 150), con.mediumtext.render("FIRE", 2, con.white)]
        self.fire_text = con.biggertext.render("CLICK TO FIRE", 5, con.white)
        self.unlocked_cannons = [[pygame.Rect(650, 15, 60, 60), True], [pygame.Rect(730, 15, 60, 60), False]
                                 , [pygame.Rect(810, 15, 60, 60), False], [pygame.Rect(890, 15, 60, 60), False]]

        #starts level user selected
        if self.level == 1:
            self.Level = Level1()

        elif self.level == 2:
            self.Level = Level2()

        elif self.level == 3:
            self.Level = Level3()

        elif self.level == 4:
            self.Level = Level4()
            
        else:
            self.Level = Level5()

        #sets initial cannon as users cannon
        self.user = CannonClass(self.Level.cannon_cords, 1)

        #sets health information for user
        self.user_health = 500
        self.healthbar = HealthBar(self.user.x, self.user.y)
                    
    def select(self):
        #creates slider for user to select where they want to shoot the cannon
        self.slider = Slider()

    def fire(self, x, y):
        #works out values to fire ball 
        play.selecting =  False
        self.user.recharged = False

        #changes values to level boundary if selected is too high
        if x < self.Level.x_boundary[0]:
            x = self.Level.x_boundary[0]
        elif x > self.Level.x_boundary[1]:
            x = self.Level.x_boundary[1]

        if x < self.Level.y_boundary[0]:
            x = self.Level.y_boundary[0]
        elif x > self.Level.y_boundary[1]:
            x = self.Level.y_boundary[1]

        height =  x - self.user.x
        power = self.user.y - y

        if power < 0:
            power = 1

        self.ball = Ball(self.user.x+100, self.user.y, height, power, True)
        self.flying = True

    def enemy_hit(self, enemy):
        #takes health away if enemy is hit
        if enemy == False:
            self.Level.enemy.health -= self.user.damage
            self.score += self.user.damage

            if self.Level.enemy.health <= 0:
                self.next_level()
                
        else:
            if enemy == 1:
                self.Level.enemy1.health -= self.user.damage
                self.score += self.user.damage
            elif enemy == 2:
                self.Level.enemy2.health -= self.user.damage
                self.score += self.user.damage                

            #if both enemys on level 5 are dead, go to winning screen
            if self.Level.enemy1.health <=0 and self.Level.enemy2.health <= 0:
                self.finish(True)
            
    def next_level(self):
        #changes level and sets essential values
        if self.level == 1:
            self.level = 2
            self.Level = Level2()
            self.healthbar.change(self.Level.cannon_cords[0], self.Level.cannon_cords[1])

        elif self.level == 2:
            self.level = 3
            self.Level = Level3()
            self.healthbar.change(self.Level.cannon_cords[0], self.Level.cannon_cords[1])

        elif self.level == 3:
            self.level = 4
            self.Level = Level4()
            self.healthbar.change(self.Level.cannon_cords[0], self.Level.cannon_cords[1])

        elif self.level == 4:
            self.level = 5
            self.Level = Level5()
            self.healthbar.change(self.Level.cannon_cords[0], self.Level.cannon_cords[1])
        
        #moves cannon to where they should be in each level
        self.user.x = self.Level.cannon_cords[0]
        self.user.y = self.Level.cannon_cords[1]

    def get_angle(self, cannon):
        #gets angle to rotate the cannon based on the position of the mouse compared to the cannon
        pos = con.mouse_pos()

        y_change = cannon.y - pos[1]
        x_change = pos[0] - cannon.x
        if x_change <= 0:
            x_change = 0.001

        radians = y_change / x_change
    
        radians = math.atan(radians)
        degrees = math.degrees(radians)

        return degrees

    def finish(self, outcome):
        #moves game to finish stage
        global finish
        finish = FinishStage(outcome)

    def get_reqscore(self, cannon):
        #returns score required to unlcok cannon
        if cannon == 2:
            value = 400
        elif cannon == 3:
            value = 700
        else:
            value = 1000
        return value
        
        
    def select_cannon(self, number):
        #changes between cannons
        if number == 0:
            self.user = CannonClass(self.Level.cannon_cords, 1)
            self.Level.cannon = 0
            
        elif number == 1:
            self.user = CannonClass(self.Level.cannon_cords, 2)
            self.Level.cannon = 1

        elif number == 2:
            self.user = CannonClass(self.Level.cannon_cords, 3)
            self.Level.cannon = 2

        elif number == 3:
            self.user = CannonClass(self.Level.cannon_cords, 4)
            self.Level.cannon = 3

    def unlock(self, number):
        #unlocks cannon if the user has a high enough score
        if number == 1:
            if self.unlocked_cannons[1][1] == False:
                if self.score >= self.get_reqscore(2):
                    self.score -= self.get_reqscore(2)
                    self.unlocked_cannons[1][1] = True
                
        elif number == 2:
            if self.score >= self.get_reqscore(3):
                self.score -= self.get_reqscore(3)
                self.unlocked_cannons[2][1] = True

        elif number == 3:
            if self.score >= self.get_reqscore(4):
                self.score -= self.get_reqscore(4)
                self.unlocked_cannons[3][1] = True

    def slider_pos(self):
        #checks the max and min positions for the slider
        pos = con.mouse_pos()

         #checks for x-axis boundary and if needed, corrects it
        if pos[0] < self.Level.x_boundary[0]:
            x_pos = self.Level.x_boundary[0]
        elif pos[0] > self.Level.x_boundary[1]:
            x_pos = self.Level.x_boundary[1]
        else:
            x_pos = pos[0]

        #checks for y-axis boundary and if needed, corrects it
        if pos[1] < self.Level.y_boundary[0]:
            y_pos = self.Level.y_boundary[0]
        elif pos[1] > self.Level.y_boundary[1]:
            y_pos = self.Level.y_boundary[1]
        else:
            y_pos = pos[1]

        return (x_pos, y_pos)
        
    def draw_selections(self):
        if self.flying == False:
            if self.level == 5:
                #draws white boxes behind cannon selections on level 5 as background is dark
                pygame.draw.rect(window, con.white, self.unlocked_cannons[0][0])
                pygame.draw.rect(window, con.white, self.unlocked_cannons[1][0])
                pygame.draw.rect(window, con.white, self.unlocked_cannons[2][0])
                pygame.draw.rect(window, con.white, self.unlocked_cannons[3][0])
                
            #draws box1
            #logic to determine wether box should be blue or black, depending on if it is selected or not
            if self.Level.cannon == 0:
                pygame.draw.rect(window, con.blue, self.unlocked_cannons[0][0], 3)
            else:
                pygame.draw.rect(window, con.black, self.unlocked_cannons[0][0], 3)

            #draws box2
            #logic to determine wether box should be blue or black, depending on if it is selected or not
            if self.Level.cannon == 1:
                pygame.draw.rect(window, con.blue, self.unlocked_cannons[1][0], 3)
            else:
                pygame.draw.rect(window, con.black, self.unlocked_cannons[1][0], 3)

            #logic to determine what padlock to show, depending on wether it can be unlocked or not
            if self.unlocked_cannons[1][1] == False:
                if self.score > play.get_reqscore(2):
                    window.blit(con.unlocked, self.unlocked_cannons[1][0])
                else:
                    window.blit(con.locked, self.unlocked_cannons[1][0])

            #draws box3
            #logic to determine wether box should be blue or black, depending on if it is selected or not
            if self.Level.cannon == 2:
                pygame.draw.rect(window, con.blue, self.unlocked_cannons[2][0], 3)
            else:
                pygame.draw.rect(window, con.black, self.unlocked_cannons[2][0], 3)

            #logic to determine what padlock to show, depending on wether it can be unlocked or not
            if self.unlocked_cannons[2][1] == False:
                if self.score > play.get_reqscore(3):
                    window.blit(con.unlocked, self.unlocked_cannons[2][0])
                else:
                    window.blit(con.locked, self.unlocked_cannons[2][0])

            #draws box4
            #logic to determine wether box should be blue or black, depending on if it is selected or not
            if self.Level.cannon == 3:
                pygame.draw.rect(window, con.blue, self.unlocked_cannons[3][0], 3)
            else:
                pygame.draw.rect(window, con.black, self.unlocked_cannons[3][0], 3)

            #logic to determine what padlock to show, depending on wether it can be unlocked or not
            if self.unlocked_cannons[3][1] == False:
                if self.score > play.get_reqscore(4):
                    window.blit(con.unlocked, self.unlocked_cannons[3][0])
                else:
                    window.blit(con.locked, self.unlocked_cannons[3][0])
                

    def draw(self):
        #draws background and everything specific to the level 
        self.Level.draw()

        #shows users score
        score_text = con.biggertext.render(str(self.score), 2, con.white)
        window.blit(score_text, (20, 10, 0, 0))

        if self.selecting == True:
            #draws slider and fire text
            play.slider.draw()
            window.blit(play.fire_text, (10, 700, 0, 0))

        else:
            #draws cannon selection boxes
            self.draw_selections()

        #draws healthbar if needed
        if play.selecting == False:
            self.healthbar.draw()

        #draws cannon
        self.user.draw()


class Level1(PlayStage):
    def __init__(self):
        #states initial values for level 1
        self.cannon_cords = (70, 450)
        self.user_hitbox = pygame.Rect(self.cannon_cords[0], self.cannon_cords[1], 200, 100)
        self.enemy_health = 200
        self.cannon = 0
        self.min_terminate = 400

        #loads in the enemy
        self.enemy = Enemy(825, 370, self.enemy_health, False, 1)

        #sets boundary for the slider
        self.x_boundary = [185, 380]
        self.y_boundary = [300, 550]

    def draw(self):
        #draws level 1 background
        window.blit(con.level1_background, (0, 0, 0, 0))

        if play.selecting == False and play.user.recharged == True:
            #draws the fire button
            pygame.draw.circle(window, con.black, (875, 690), 70)
            pygame.draw.circle(window, con.red, (875, 690), 60)
            window.blit(play.firebutton[1], (828, 660, 0, 0))

        #draws ball if it needs to be            
        if play.flying == True:
            play.ball.draw_ball()

        #draws enemy
        self.enemy.draw()


class Level2(PlayStage):
    def __init__(self):
        #sets initial values for level 2
        self.cannon_cords = (10, 240)
        self.user_hitbox = pygame.Rect(self.cannon_cords[0], self.cannon_cords[1], 200, 100)
        self.enemy_health =  200
        self.cannon = 0
        self.min_terminate = 500

        #loads in the enemy
        self.enemy = Enemy(775, 372, self.enemy_health, False, 2)

        #sets boundary for the slider
        self.x_boundary = [158, 440]
        self.y_boundary = [40, 240]

    def draw(self):
        #draws level 2 background
        window.blit(con.level2_background, (0, 0, 0, 0))

        if play.selecting == False and play.user.recharged == True:
            #draws the fire button
            pygame.draw.circle(window, con.black, (875, 690), 70)
            pygame.draw.circle(window, con.red, (875, 690), 60)
            window.blit(play.firebutton[1], (828, 660, 0, 0))

        #draws ball if it is currently being fired            
        if play.flying == True:
            play.ball.draw_ball()

        #draws enemy
        self.enemy.draw()
        

class Level3(PlayStage):
    def __init__(self):
        #sets initial values for stage 3
        self.cannon_cords = [70, 567]
        self.user_hitbox = pygame.Rect(self.cannon_cords[0], self.cannon_cords[1], 200, 100)
        self.exploding = False
        self.bird = pygame.Rect(490, 250, 70, 130)
        self.enemy_health =  400
        self.cannon = 0
        self.min_terminate = 400

        #loads in the enemy
        self.enemy = Enemy(750, 330, self.enemy_health, False, 3)

        #sets boundary for the slider
        self.x_boundary = [180, 380]
        self.y_boundary = [350, 500]

    def check_bird(self):
        #checks if a fired ball has collided with the user
        if self.bird.collidepoint(play.ball.x, play.ball.y):

            #sets values needed for the explosion GIF and creates the thread that will manipulate it
            self.explosion = Explosion(520, 290)
            self.exploding = True
            thread = threading.Thread(target=self.explode, args=([0]))
            thread.start()

    def explode(self, expanding):
        #recursive subroutine that will determine what to do to the explosion GIF depending on how big it has reached
        print()
        if expanding <= 20:
            expanding = expanding + 1
            self.explosion.increase()
            self.explode(expanding)
            
        else:
            self.exploding = False
            
    def draw(self):
        #draws level 3 background
        window.blit(con.level3_background, (0, 0, 0, 0))

        if play.selecting == False and play.user.recharged == True:
            #draws the fire button
            pygame.draw.circle(window, con.black, (875, 690), 70)
            pygame.draw.circle(window, con.red, (875, 690), 60)
            window.blit(play.firebutton[1], (828, 660, 0, 0))

        #draws ball if it needs to be            
        if play.flying == True:
            play.ball.draw_ball()

        #draws cannon and enemy
        self.enemy.draw()

        if self.exploding == True:
            self.explosion.draw()


class Level4(PlayStage):
    def __init__(self):
        #sets initial values for level 4
        self.cannon_cords = [10, 480]
        self.user_hitbox = pygame.Rect(self.cannon_cords[0], self.cannon_cords[1], 200, 100)
        self.enemy_health = 600
        self.cannon = 0
        self.min_terminate = 300

        #loads in the enemy
        self.enemy = Enemy(765, 372, self.enemy_health, False, 4)

        #sets boundary for the slider
        self.x_boundary = [100, 400]
        self.y_boundary = [300, 500]

    def draw(self):
        #draws level 4 background
        window.blit(con.level4_background, (0, 0, 0, 0))

        if play.selecting == False and play.user.recharged == True:
            #draws the fire button
            pygame.draw.circle(window, con.black, (875, 690), 70)
            pygame.draw.circle(window, con.red, (875, 690), 60)
            window.blit(play.firebutton[1], (828, 660, 0, 0))

        #draws ball if it needs to be            
        if play.flying == True:
            play.ball.draw_ball()

        #draws cannon and enemy
        self.enemy.draw()


class Level5(PlayStage):
    def __init__(self):
        #sets initial values for level 5
        self.cannon_cords = [140, 390]
        self.user_hitbox = pygame.Rect(self.cannon_cords[0], self.cannon_cords[1], 200, 100)
        self.enemy_health =  600
        self.cannon = 0
        self.min_terminate = 300

        #loads in the enemy
        self.enemy1 = Enemy(850, 100, self.enemy_health, True, 5)
        self.enemy2 = Enemy(850, 450, self.enemy_health, True, 5)
        self.enemys = [self.enemy1, self.enemy2]

        #sets boundary for the slider
        self.x_boundary = [340, 440]
        self.y_boundary = [200, 500]
        

    def draw(self):
        #draws level 5 background
        window.blit(con.level5_background, (0, 0, 0, 0))

        if play.selecting == False and play.user.recharged == True:
            #draws the fire button
            pygame.draw.circle(window, con.black, (875, 690), 70)
            pygame.draw.circle(window, con.red, (875, 690), 60)
            window.blit(play.firebutton[1], (828, 660, 0, 0))

        #draws ball if it is beibg fired           
        if play.flying == True:
            play.ball.draw_ball()

        #draws enemy
        for enemy in self.enemys:
            enemy.draw()
        

class Explosion:
    def __init__(self, x, y):
        #sets initial values for the explosion GIF
        self.x = x
        self.y = y
        self.width = 30
        self.height = 30
        self.rate = 0
        self.increased = False

    def increase(self):
        #manipulates the size and position of the explosion GIF
        if self.increased == False:
            self.rate += 1
            self.increased = True
        else:
            self.increased = False
            
        self.x -= 1
        self.y -= 1

        self.width = self.width + self.rate
        self.height = self.height + self.rate

    def draw(self):
        #draws the explosion
        pic = pygame.transform.scale(con.explosion, (self.width, self.height))
        window.blit(pic, (self.x, self.y, 1, 1))


class Enemy(PlayStage):
    def __init__(self, x, y, health, smaller, level):
        #sets all variables needed for the enemy
        self.size = smaller
        self.x = x
        self.y = y
        self.flying = False
        self.damage = 30

        if smaller == True:
            self.hitbox = pygame.Rect(self.x, self.y, 80, 140)
        else:
            self.hitbox = pygame.Rect(self.x, self.y, 150, 200)

        #determines what variables are needed based on what level enemy it is
        if level == 1:
            self.picture = con.enemy1
            self.speed = 5
            self.rate = 150
        elif level == 2:
            self.picture = con.enemy2
            self.speed = 7
            self.rate = 120
        elif level == 3:
            self.picture = con.enemy3
            self.speed = 10
            self.rate = 90
        elif level == 4:
            self.picture = con.enemy4
            self.speed = 12
            self.rate = 75
        else:
            self.picture = con.enemy5
            self.speed = 13
        
        self.health = health
        self.max_health = health
        
        self.jumping = False

    def fire(self):
        #sets variable needed to fire a ball at the user
        height = random.randint(100, 400)
        power = random.randint(15, 200)

        self.ball = Ball(self.x, self.y, height, power, False)
        self.flying = True

    def user_hit(self):
        #subtracts enemys damage from users health
        play.user_health -= play.Level.enemy.damage

    def jump(self):
        #sets variables needed for enemy to do jump action
        height = random.randint(5, 12)
        jumps = 0
        direction = "UP"

        #creates thread which manipulates enemys position
        thread = threading.Thread(target=self.jump_loop, args = (height, jumps, direction))
        thread.start()

    def jump_loop(self, height, jumps, direction):
        #recursively makes enemy do the jump action 
        if direction == "DOWN" and jumps == height:
            self.jumping = False
        else:
            if jumps == height:
                direction = "DOWN"
                jumps = 0

            if direction == "UP":
                self.y -= 8
            else:
                self.y += 8

            self.jump_loop(height, jumps+1, direction)

    def draw(self):
        #creates hitbox and health text
        self.hitbox = pygame.Rect(self.hitbox)
        health_text = con.smalltext.render(str(self.health), 10, con.white)

        if self.health > 0:
            #draws enemy health
            if self.size == True:
                window.blit(health_text, (self.x+20, self.y - 30))
            else:
                window.blit(health_text, (self.x + 50, self.y - 40))

            #actually draws enemy
            window.blit(self.picture, (self.hitbox))

            if self.flying:
                #draws ball if there is one currently being fired 
                self.ball.draw_ball()


class HealthBar(PlayStage):
    def __init__(self, x, y):
        #sets initial position of healthbar
        self.user_healthbar = pygame.Rect(x, (y-25),200, 30)

    def change(self, x, y):
        #changes position of healthbar 
        self.user_healthbar = pygame.Rect(x, (y-25),200, 30)
        
    def draw(self):
        #draws health bar above cannon
        x_length = play.user_health // 2.5
        pygame.draw.rect(window, con.white, (self.user_healthbar))
        pygame.draw.rect(window, con.green, (self.user_healthbar[0], self.user_healthbar[1], x_length
                        , self.user_healthbar[3]))
        pygame.draw.rect(window, con.black, (self.user_healthbar), 2)


class Ball(PlayStage):
    def __init__(self, x, y, height, power, direction):
        #sets initial values for the ball that has been fired
        self.x = x + 10
        self.y = y
        self.direction = direction
        
        self.equate(height, power)

    def equate(self, height, power):
        #creates quadratic equation for the balls route, forming a curve
        self.height = height
        self.power = power

        #ensures that there is a valid domain for the square route of the function
        if power <= 0:
            power = 1
        if height <= 0:
            height = 0
        numerator = height/power
        if numerator <= 0:
            numerator = 0.0001

        #sets all values 
        self.a = (1/math.sqrt(numerator)) * 1.25
        self.b = height * (power/100)
        self.c = power * (height ) * 2

    def get_y(self, x):
        #uses equation to get the y-axis position in relation to the x-axis position
        x = x - 350
        
        y = -(self.a*(x* x)) + (self.b * x) + self.c
        y = y // 1000
        y = play.user.y - y
        
        return y

    def check_colour(self):
        x = int(self.x)
        y = int(self.y)

        #bottom of the ball
        point1 = (x, y+24)
        #right of the ball
        point2 = (x+24, y)
        #bottom right of ball
        point3 = (x+24, y+24)

        #checks colour of the background at point where ball is to see if it is the floor
        if point1[0] < con.screenX and point1[0] > 0:
            if point2[0] < con.screenX and point2[0] > 0:
                if point3[0] < con.screenX and point2[0] > 0:

                    if point1[1] < con.screenY and point1[1] > 0:
                        if point2[1] < con.screenY and point2[1] > 0:
                            if point3[1] < con.screenY and point2[1] > 0:
       
                                if point1[1] < 800 and point2[1] < 800 and point3[1] < 800: 
                                    colour1 = window.get_at(point1)[:3]
                                    colour2 = window.get_at(point2)[:3]
                                    colour3 = window.get_at(point3)[:3]

                                if colour1 == con.black or colour2 == con.black or colour3 == con.black:
                                    if x > play.Level.min_terminate:
                                        return True
        else:
            return False

    def check_boundary(self, mode):
        condition = False

        if mode == True:
            #checks wether ball is out of boundary
            if (self.x + 25) > con.screenX:
                condition = "BOUNDARY"

            #checks wether ball has hit the ground
            elif self.check_colour() and play.level < 5:
                condition = "BOUNDARY"

            #checks wether ball has hit an enemy
            possible_cords = [[self.x, self.y], [self.x + 25, self.y], [self.x, self.y + 25], [self.x+25, self.y+25]]
            for cord in possible_cords:
                    x = cord[0]
                    y = cord[1]
                    
                    if play.level == 5:
                        if play.Level.enemy1.hitbox.collidepoint(x, y):
                            condition = ["ENEMY", 1]
                        elif play.Level.enemy2.hitbox.collidepoint(x, y):
                            condition = ["ENEMY", 2]
                        
                    else:
                        if play.Level.enemy.hitbox.collidepoint(x, y):
                            condition = "ENEMY"
        else:
            #checks wether ball is outside boundary
            if (self.x - 25) > con.screenX:
                condition = "BOUNDARY"

            #checks wether ball has hit ground
            elif self.check_colour():
                condition = "BOUNDARY"

            #checks wether ball has hit user
            possible_cords = [[self.x, self.y], [self.x + 25, self.y], [self.x, self.y + 25], [self.x+25, self.y+25]]
            for cord in possible_cords:
                    x = cord[0]
                    y = cord[1]

                    if play.Level.user_hitbox.collidepoint(x, y):
                        condition = "ENEMY"
        return condition
                    
    def draw_ball(self):
        #draws ball
        if self.direction == False:
            pygame.draw.circle(window, con.blue, (self.x, self.y), 25)
        else:
            pygame.draw.circle(window, con.red, (self.x, self.y), 25)


class Slider:
    def position(self):
        value = play.slider_pos()
        x_pos = value[0]
        y_pos = value[1]

        return (x_pos, y_pos)
                
    def draw(self):
        #gets mouse position
        values = self.position()
        x_pos = values[0]
        y_pos = values[1]

        #draws blue background slider
        pygame.draw.circle(window, con.blue, (play.user.x+80, play.user.y+20), 27)
        pygame.draw.line(window, con.blue, (play.user.x+80, play.user.y+20), (x_pos, y_pos), 55)
        pygame.draw.circle(window, con.blue, (x_pos, y_pos), 27)

        #draws white slider
        pygame.draw.circle(window, con.white, (play.user.x+80, play.user.y+20), 16)
        pygame.draw.line(window, con.white, (play.user.x+80, play.user.y+20), (x_pos, y_pos), 25)
        pygame.draw.circle(window, con.white, (x_pos, y_pos), 16)



class CannonClass:
    def __init__(self, cords, cannon_type):
        #states initial value for cannon
        self.cannon_type = cannon_type
        self.x = cords[0]
        self.y = cords[1]

        #sets values for specific cannon tiers
        if self.cannon_type == 1:
            self.damage = 50
            self.speed = 10
        elif self.cannon_type == 2:
            self.damage = 80
            self.speed = 13
        elif self.cannon_type == 3:
            self.damage = 120
            self.speed = 13
        else:
            self.damage = 180
            self.speed = 20

        self.recharged = True

        
    def draw(self):
        #gets angle to rotate the cannon by
        angle = round(play.get_angle(self), 0)

        #draws the cannon depending on what tier cannon it is
        if self.cannon_type == 1:
            cannon = pygame.transform.rotate(con.cannon1, angle)
        elif self.cannon_type == 2:
            cannon = pygame.transform.rotate(con.cannon2, angle)
        elif self.cannon_type == 3:
            cannon = pygame.transform.rotate(con.cannon3, angle)
        else:
            cannon = pygame.transform.rotate(con.cannon4, angle)

        cannon.set_colorkey((255, 255, 255))
        window.blit(cannon, (self.x, self.y, 100, 50))



class FinishStage:
    #code for the finish stage
    def __init__(self, outcome):
        global stage
        stage = "FINAL"

        #determines text to display on finish screen
        if outcome:
            self.win_text = con.biggertext.render("<<YOU WON>>", 30, con.green)
        else:
            self.win_text = con.biggertext.render("<<YOU LOST>>", 30, con.red)

        self.quit_button = pygame.Rect(300, 550, 400, 200)
        self.quit_text = con.biggertext.render("QUIT?", 30, con.white)


    def draw(self):
        #draws background for final stage 
        pygame.draw.rect(window, con.white, (0, 0, con.screenX, con.screenY))

        pygame.draw.rect(window, con.black, self.quit_button)
        pygame.draw.rect(window, con.red, self.quit_button, 2)

        window.blit(self.quit_text, (400, 600, 0, 0))
        window.blit(self.win_text, (250, 200, 0, 0))


class ExitGame:
    def __init__(self):
        #creates tkinter window
        self.root = tk.Tk()
        self.root.title(" ")

        #sets up window formatting
        Top_frame = tk.Frame(self.root)
        Bottom_frame = tk.Frame(self.root)

        Top_frame.grid(row=0, column=0)
        Bottom_frame.grid(row=1, column=0)

        #tells mainloop they have clicked exit
        con.wanna_leave = True

        #creates the text and buttons
        tk.Label(Top_frame, text="WOULD YOU LIKE TO LEAVE?", font="none 18 bold").grid()
        tk.Button(Bottom_frame, text="RETURN", font="none 20", width=11, height=2
                  , command= lambda: self.leave(False)).grid(row=0, column=0)
        
        tk.Button(Bottom_frame, text="LEAVE", font="none 20", width=11, height=2
                  , command= lambda: self.leave(True)).grid(row=0, column=1)
        self.root.mainloop()

    def leave(self, choice):
        #decides what to do depending on what the user clicks
        if choice == True:

            #closes the program
            self.root.destroy()
            self.decision = True   

        else:
            #goes back to the game
            self.root.destroy()
            self.decision = False

def mainloop(running):
    global play, finish, stage, count, jump_assigned, clickedcount

    while running:
        #manages time management
        count += 1
        clock.tick(30)

        #gets all actions taken
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                leave = ExitGame()

        #gets position of mouse and keys pressed, if pressed
        keys = pygame.key.get_pressed()
        pos = con.mouse_pos()


        if stage == "MENU":
            #all the code to determine actions needed depening on the input in the menu
            if pygame.mouse.get_pressed()[0]:
                if (count-clickedcount) > 5:

                    if menu.type == "MENU":

                        #checks if user clicks play
                        if menu.play_rect.collidepoint(pos):
                            con.start("SELECT")
                            clickedcount = count

                        #checks if user clicks rules
                        elif menu.rule_rect.collidepoint(pos):
                            menu.type = "RULES"
                            clickedcount = count

                        #checks if user clicks exit
                        elif menu.exit_rect.collidepoint(pos):
                            running = False
                    else:
                        #checks if user clicks back from the rules page
                        if menu.back_button.collidepoint(pos):
                            menu.back()
                            clickedcount = count

        elif stage == "SELECT":
            if pygame.mouse.get_pressed()[0]:
                if (count-clickedcount) > 5:
                #checks where the user has clicked in the selection menu

                    #checks wether the user presses back
                    if select.back_button.collidepoint(pos):
                        select.back()
                        clickedcount = count

                    else:
                        #appropriate commands if they click level 1
                        if select.pane1_box.collidepoint(pos):
                            play = PlayStage(1)
                            stage = "PLAY"
                            clickedcount = count

                        #appropriate commands if they click level 2
                        elif select.pane2_box.collidepoint(pos):
                            play = PlayStage(2)
                            stage = "PLAY"
                            clickedcount = count

                        #appropriate commands if they click level 3
                        elif select.pane3_box.collidepoint(pos):
                            play = PlayStage(3)
                            stage = "PLAY"
                            clickedcount = count
                            
                        #appropriate commands if they click level 4
                        elif select.pane4_box.collidepoint(pos):
                            play = PlayStage(4)
                            stage = "PLAY"
                            clickedcount = count

                        #appropriate commands if they click level 5
                        elif select.pane5_box.collidepoint(pos):
                            play = PlayStage(5)
                            stage = "PLAY"
                            clickedcount = count

        elif stage == "PLAY":
            #all the code to determine actions needed depening on the input in the play stage

            #randomly gives the user points every once in a while
            if count % 510 == 0:
                play.score += random.randint(10, 150)

            if play.user_health <= 0:
                play.finish(False)

            #gives the enemy a chance to jump
            if play.score > 300 and jump_assigned == False:
                if play.level < 5:
                    jump_assigned = True
                    jump_count = count

            #if the enemy is told to jump, it initiates the thread to do so
            if jump_assigned == True:
                if play.level < 5:
                    if play.Level.enemy.jumping == False:
                        if (count - jump_count) > 20:

                            jump_count = count
                            choice = random.randint(1, 30)
                            if choice < 4:
                                play.Level.enemy.jumping = True
                                play.Level.enemy.jump()
                            

            if play.flying == True:
                if play.level == 3:
                    play.Level.check_bird()
                #checks if the users ball has hit anything
                condition = play.ball.check_boundary(True)
                    
                if condition == "BOUNDARY":
                    #detects that the users ball has hit a boundary
                    play.flying = False
                    play.user.recharged = True
                    
                elif condition == "ENEMY":
                    #detects that the users ball has hit an enemy in levels 1-4 
                    play.flying = False
                    play.enemy_hit(False)
                    
                    play.user.recharged = True
                elif condition == ["ENEMY", 1]:
                    #detects that the users ball has hit enemy 1 in level 5
                    play.flying = False
                    play.enemy_hit(1)
                    
                    play.user.recharged = True
                elif condition == ["ENEMY", 2]:
                    #detects that the users ball has hit enemy 2 in level 5
                    play.flying = False
                    play.enemy_hit(2)
                    play.user.recharged = True
                    
                else:
                    #moves the fired user ball along
                    play.ball.x += play.user.speed 
                    play.ball.y = play.ball.get_y(play.ball.x)
                    
            if play.level < 5:
                if play.Level.enemy.flying == True:
                    #checks if the enemy ball has hit anything
                    condition = play.Level.enemy.ball.check_boundary(False)
                        
                    if condition == "BOUNDARY":
                        #detects that the enemy ball has hit a boundary
                        play.Level.enemy.flying = False
                        
                    elif condition == "ENEMY":
                        #detects that the enemy ball has hit the user 
                        play.Level.enemy.flying = False
                        play.Level.enemy.user_hit()
                    else:
                        #moves the enemy ball
                        play.Level.enemy.ball.x -= play.Level.enemy.speed
                        play.Level.enemy.ball.y = play.Level.enemy.ball.get_y(play.Level.enemy.ball.x)

                #gives a chance for the enemy to fire at the user
                if count > 200:
                    if random.randint(1, play.Level.enemy.rate) == 6 and play.Level.enemy.flying == False:
                        if count > 400:
                            play.Level.enemy.fire()

            #determines what to do if the mouse is clicked
            if pygame.mouse.get_pressed()[0]:
                if (count-clickedcount) > 5:
                    clickedcount = count

                    if play.selecting == True:
                        #once user selects where they want to fire, this fires the ball
                        play.fire(pos[0], pos[1])

                    else:
                        if play.user.recharged == True and play.flying == False:
                            if play.firebutton[0].collidepoint(pos):
                                #lets user select where they want to fire the cannon
                                play.selecting = True
                                play.select()

                        if play.unlocked_cannons[0][0].collidepoint(pos):
                                #selects cannon 1
                                play.select_cannon(0)

                        elif play.unlocked_cannons[1][0].collidepoint(pos):
                            if play.unlocked_cannons[1][1] == False:
                                #unlocks cannon 2
                                play.unlock(1)
                            else:
                                #selects cannon 2
                                play.select_cannon(1)

                        elif play.unlocked_cannons[2][0].collidepoint(pos):
                            if play.unlocked_cannons[2][1] == False:
                                #unlocks cannon 3
                                play.unlock(2)
                            else:
                                #selects cannon 3
                                play.select_cannon(2)

                        elif play.unlocked_cannons[3][0].collidepoint(pos):
                            if play.unlocked_cannons[3][1] == False:
                                #unlcks cannon 4
                                play.unlock(3)
                            else:
                                #selects cannon 4
                                play.select_cannon(3)

        else:
            if pygame.mouse.get_pressed()[0]:
                #exits the program
                if finish.quit_button.collidepoint(pos):
                    running = False

        #determines what to do if the user would like to leave
        if con.wanna_leave:
            if leave.decision:
                running = False
            else:
                con.wanna_leave = False

        #goes to drawing suboutine
        con.draw(stage)

    else:
        #destroys tab and says a thank you message
        pygame.quit()
        print ("THANK YOU FOR PLAYING")
    
def start():
    #initialises classes
    global con, menu, count, jump_assigned, stage, clickedcount, decision  
    con = Configuration()
    menu = MenuStage()

    #sets needed global variables
    stage = "MENU"

    #sets needed variables
    count = 0
    clickedcount = 0
    jump_assigned = False

    #starts the loop
    mainloop(True)        


if "__main__" == "__main__":
    start()

