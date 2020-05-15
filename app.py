import pygame
import time
import random

'''Game initialization with pygame'''
pygame.init()
'''Screen Display size'''
display_width = 400
display_height = 400
display = pygame.display.set_mode((display_width,display_height))

''' Background color RGB'''

white=(255,255,255)

''' Snake Color RGB'''
black=(0,0,0)

'''Text Color RGB'''
red=(255,0,0)
magenta = (255,0,255)
'''Food Color RGB'''
blue=(0,0,255)

'''Covid Color'''
green = (0, 255, 0)

'''Snake Size and characteristics'''
snake_size = 10

'''Snake Speed'''
speed = pygame.time.Clock()
snake_speed = 30

'''Message display'''
font_style = pygame.font.SysFont("comicsansms", 15)
score_style = pygame.font.SysFont("comicsansms", 25)

random_num_width = random.randint(0,display_width)
random_num_height = random.randint(0,display_height)

def snake(snake_size, snake_body,color):
    for x in snake_body:
        pygame.draw.rect(display, color,[x[0], x[1], snake_size, snake_size])

def score(score):
    value = score_style.render("Your Score is: "+str(score), True, magenta )
    display.blit(value, [ 0,0] )


def message_lost(msg, color):
    message = font_style.render(msg, True, color)
    display.blit(message,[display_width/12,display_height/2])

'''game loop '''
def repeat_game():
    close_display = False    
    game_over=False

    ''' Starting coordinates '''
    x1 = display_width/2
    y1 = display_height/2

    ''' Coordinate Changes'''
    x1_change = 0
    y1_change = 0

    '''Directions'''
    up = False
    down = False
    left = False
    right = False

    '''Snake Body'''
    snake_body = []
    length_of_snake = 1
    snake_speed = 20
    snake_color = True

    random_num_width = random.randint(0,display_width)
    random_num_height = random.randint(0,display_height)


    '''Food Coordinates'''
    foodX = round(random.randrange(0, display_width - (snake_size*4))/10)*10
    foodY = round(random.randrange(0, display_height - (snake_size*4))/10)*10
   

    ''' Covid coordinates'''
    covidX = round(random.randrange(0, display_width - (snake_size*4))/10)*10
    covidY = round(random.randrange(0, display_height - (snake_size*4))/10)*10
    covidX2 = round(random.randrange(0, display_width - (snake_size*4))/10)*10
    covidY2 = round(random.randrange(0, display_height - (snake_size*4))/10)*10
    covidX3 = round(random.randrange(0, display_width - (snake_size*4))/10)*10
    covidY3 = round(random.randrange(0, display_height - (snake_size*4))/10)*10
    covidX4 = round(random.randrange(0, display_width - (snake_size*4))/10)*10
    covidY4 = round(random.randrange(0, display_height - (snake_size*4))/10)*10
    covidX5 = round(random.randrange(0, display_width - (snake_size*4))/10)*10
    covidY5 = round(random.randrange(0, display_height - (snake_size*4))/10)*10
    covidX6 = round(random.randrange(0, display_width - (snake_size*4))/10)*10
    covidY6 = round(random.randrange(0, display_height - (snake_size*4))/10)*10   
    
    while not game_over:
        while close_display == True:
            display.fill(white)
            message_lost(':( you lost , press Q to quit or P to play again', red)
            score(length_of_snake-1)
            pygame.display.update()
            
            for key_pressed in pygame.event.get():                
                if key_pressed.type == pygame.QUIT:
                    game_over = True
                    close_display = False                    

                if key_pressed.type == pygame.KEYDOWN:
                    if key_pressed.key == pygame.K_q:
                        game_over = True
                        close_display = False
                    if key_pressed.key == pygame.K_p:
                        repeat_game()
                   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and right == False:
                    x1_change = -snake_size
                    y1_change = 0
                    left = True
                    up = False
                    down = False
                    right = False
                elif event.key == pygame.K_RIGHT and left == False:
                    x1_change = snake_size
                    y1_change = 0
                    left = False
                    up = False
                    down = False
                    right = True
                elif event.key == pygame.K_UP and down == False:
                    x1_change = 0
                    y1_change = -snake_size
                    left = False
                    up = True
                    down = False
                    right = False
                elif event.key == pygame.K_DOWN and up == False:
                    x1_change = 0
                    y1_change = snake_size
                    left = False
                    up = False
                    down = True
                    right = False

        if x1 >=display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            close_display = True
        if length_of_snake < 0:
            close_display = True
        
        x1 += x1_change
        y1 += y1_change
        display.fill(white)
        pygame.draw.rect(display,blue,[foodX,foodY,snake_size,snake_size])
        pygame.draw.circle(display,green,[covidX,covidY], 5)
        pygame.draw.circle(display,green,[covidX2,covidY2], 5)
        pygame.draw.circle(display,green,[covidX3,covidY3], 5)
        pygame.draw.circle(display,green,[covidX4,covidY4], 5)
        pygame.draw.circle(display,green,[covidX5,covidY5], 5)
        pygame.draw.circle(display,green,[covidX6,covidY6], 5)
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)

        snake_body.append(snake_Head)
        if len(snake_body) > length_of_snake:
            del snake_body[0]

        for x in snake_body[:-1]:
            if x == snake_Head:
                close_display = True
        
        if snake_color:
            snake(snake_size,snake_body,black)
        else:
            snake(snake_size,snake_body,red)
        

        score(length_of_snake-1)
        pygame.display.update()

        if x1 == foodX and y1 == foodY:
            foodX = round(random.randrange(0, display_width - (snake_size*4))/10)*10
            foodY = round(random.randrange(0, display_height - (snake_size*4))/10)*10
            covidX = round(random.randrange(0, display_width - (snake_size*4))/10)*10
            covidY = round(random.randrange(0, display_height - (snake_size*4))/10)*10
            covidX2 = round(random.randrange(0, display_width - (snake_size*4))/10)*10
            covidY2 = round(random.randrange(0, display_height - (snake_size*4))/10)*10
            covidX3 = round(random.randrange(0, display_width - (snake_size*4))/10)*10
            covidY3 = round(random.randrange(0, display_height - (snake_size*4))/10)*10
            covidX4 = round(random.randrange(0, display_width - (snake_size*4))/10)*10
            covidY4 = round(random.randrange(0, display_height - (snake_size*4))/10)*10
            covidX5 = round(random.randrange(0, display_width - (snake_size*4))/10)*10
            covidY5 = round(random.randrange(0, display_height - (snake_size*4))/10)*10
            covidX6 = round(random.randrange(0, display_width - (snake_size*4))/10)*10
            covidY6 = round(random.randrange(0, display_height - (snake_size*4))/10)*10
            
            length_of_snake += 1
            snake_speed += 0.8
            snake_color = True
        
        if x1 + 6 == covidX + 6 and y1 == covidY or x1 + 6 == covidX2 + 6 and y1 == covidY2 or x1 + 6 == covidX3 + 6 and y1 == covidY3 or x1 + 6 == covidX4 + 6 and y1 == covidY4 or x1 + 6 == covidX5 + 6 and y1 == covidY5 or x1 + 6 == covidX6 + 6 and y1 == covidY6:
            covidX = round(random.randrange(0, display_width - (snake_size*4))/10)*10
            covidY = round(random.randrange(0, display_height - (snake_size*4))/10)*10                    
            covidX2 = round(random.randrange(0, display_width - (snake_size*4))/10)*10
            covidY2 = round(random.randrange(0, display_height - (snake_size*4))/10)*10
            covidX3 = round(random.randrange(0, display_width - (snake_size*4))/10)*10
            covidY3 = round(random.randrange(0, display_height - (snake_size*4))/10)*10
            covidX4 = round(random.randrange(0, display_width - (snake_size*4))/10)*10
            covidY4 = round(random.randrange(0, display_height - (snake_size*4))/10)*10
            covidX5 = round(random.randrange(0, display_width - (snake_size*4))/10)*10
            covidY5 = round(random.randrange(0, display_height - (snake_size*4))/10)*10
            covidX6 = round(random.randrange(0, display_width - (snake_size*4))/10)*10
            covidY6 = round(random.randrange(0, display_height - (snake_size*4))/10)*10
            
            foodX = round(random.randrange(0, display_width - (snake_size*4))/10)*10
            foodY = round(random.randrange(0, display_height - (snake_size*4))/10)*10
            length_of_snake -= 1
            snake_color = False
            snake_body.pop()        

        speed.tick(snake_speed) 
    pygame.quit()
    quit()

repeat_game()