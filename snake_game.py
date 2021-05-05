import pygame
import random

# 초기화
pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("SNAKE")

# fps
clock = pygame.time.Clock()

# 배경, 캐릭터 설정
background = pygame.image.load('C:/Users/user/Desktop/python_projects/snake_game/background.png')

snake = pygame.image.load('C:/Users/user/Desktop/python_projects/snake_game/snake.png')
snake_size = snake.get_rect().size
snake_width = snake_size[0]
snake_height = snake_size[1]
snake_x_pos = 0
snake_y_pos = 0
snake_speed = 0.1

food = pygame.image.load('C:/Users/user/Desktop/python_projects/snake_game/food.png')
food_size = food.get_rect().size
food_width = food_size[0]
food_height = food_size[1]
food_x_pos = random.randint(0, screen_width-food_width)
food_y_pos = random.randint(0, screen_height-food_height)


to_x = 0
to_y = 0

#이벤트 루프
running = True

while running:
  dt = clock.tick(30)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running=False
    
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
          to_x -= snake_speed
          to_y=0
          
        elif event.key == pygame.K_RIGHT:
          to_x += snake_speed
          to_y=0
        elif event.key == pygame.K_UP:
          to_y -= snake_speed
          to_x=0
        elif event.key == pygame.K_DOWN:
          to_y += snake_speed
          to_x=0

     
  snake_x_pos += to_x * dt
  snake_y_pos += to_y * dt

  if snake_x_pos < 0:
    snake_x_pos = 0
  elif snake_x_pos > screen_width-snake_width:
    snake_x_pos = screen_width - snake_width
  
  if snake_y_pos < 0 :
    snake_y_pos = 0
  elif snake_y_pos > screen_height - snake_height:
    snake_y_pos = screen_height - snake_height

  screen.blit(background, (0, 0))
  screen.blit(snake, (snake_x_pos, snake_y_pos))
  screen.blit(food, (food_x_pos, food_y_pos))

  pygame.display.update()
    



pygame.quit()
