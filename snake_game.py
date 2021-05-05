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
snake_pos = [2*snake_width, screen_height/2 - snake_height/2] # 초기 위치
snake_body = [[0, screen_height/2 - snake_height/2], [snake_width, screen_height/2 - snake_height/2], [2*snake_width, screen_height/2 - snake_height/2]] # 뱀 몸의 초기 위치

food = pygame.image.load('C:/Users/user/Desktop/python_projects/snake_game/food.png')
food_size = food.get_rect().size
food_width = food_size[0]
food_height = food_size[1]
food_pos = [random.randrange(30, screen_width-30), random.randrange(30, screen_height-30)]


direction = 'right'
score = 0
font = pygame.font.SysFont('comicsans',40)
#이벤트 루프
running = True

while running:
  dt = clock.tick(10)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running=False

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT and direction != 'right':
        direction = 'left'
      elif event.key == pygame.K_RIGHT and direction != 'left':
        direction = 'right'
      elif event.key == pygame.K_UP and direction != 'down':
        direction = 'up'
      elif event.key == pygame.K_DOWN and direction != 'up':
        direction = 'down'
 
  if direction == 'right':
      snake_pos[0] += snake_width
  elif direction == 'left':
      snake_pos[0] -= snake_width
  elif direction == 'up':
      snake_pos[1] -= snake_width
  elif direction == 'down':
      snake_pos[1] += snake_width
  
  # 충돌처리
  if snake_pos[0] + snake_width <= 0 or snake_pos[0] >= screen_width:
    running = False
  
  if snake_pos[1] <= 0 or snake_pos[1] >= screen_height:
    running = False

  for square in snake_body[1:]:
    if pygame.Rect(square[0], square[1], 30, 30).colliderect(pygame.Rect(snake_pos[0], snake_pos[1], 30, 30)):
      running = False
  
  # 그리기
  screen.blit(background, (0, 0))

  for square in snake_body:
    screen.blit(snake, (square[0], square[1]))

  screen.blit(food, (food_pos[0], food_pos[1]))

  snake_body.append(list(snake_pos))
  

  if pygame.Rect(snake_pos[0],snake_pos[1],30,30).colliderect(pygame.Rect(food_pos[0],food_pos[1],30,30)):
    food_pos = [random.randrange(30, screen_width-30), random.randrange(30, screen_height-30)]
    score += 5
  else:
    snake_body.pop(0)

  score_font = font.render(f'{score}' , True , (255,255,255))
  font_pos = score_font.get_rect(center=(screen_width/2 , 30))
  screen.blit(score_font , font_pos)

  pygame.display.update()
    
pygame.quit()
