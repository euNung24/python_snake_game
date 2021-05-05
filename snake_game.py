import pygame
import random

# 게임 초기화
pygame.init()

# 스크린 그리기
screen_width = 480
screen_height = 630
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

# 격자 그리기
grid_pos1 = [30,30]
grid_pos2 = [60,60]
grid_pos3 = [60, 30]
grid_pos4 = [30, 60]

# 캐릭터, 설정 그리기
snake_pos = [30*3, 30*10]
snake_body = [[30, 30*10], [30*2, 30*10], [30*3, 30*10]]


fruit_pos = [random.randrange(30, screen_width-30,30),random.randrange(30, screen_height-30,30)]
fruits = [pygame.image.load('C:/Users/user/Desktop/python_projects/snake_game/images/banana.png'),
          pygame.image.load('C:/Users/user/Desktop/python_projects/snake_game/images/orange.png'),
          pygame.image.load('C:/Users/user/Desktop/python_projects/snake_game/images/apple.png'),
          pygame.image.load('C:/Users/user/Desktop/python_projects/snake_game/images/watermelon.png'),
          pygame.image.load('C:/Users/user/Desktop/python_projects/snake_game/images/pineapple.png'),
        ]
fruit_decide = random.randint(0,len(fruits)-1)


direction = 'right'
score = 0
font = pygame.font.SysFont('comicsans', 40)

# 격자 그리기 함수
def draw_backround():
  for i in range(12):
    for j in range(14):
      pygame.draw.rect(screen,(196, 223, 100), (grid_pos1[0], grid_pos1[1], 30, 30))
      grid_pos1[1] += 60
      if grid_pos1[1] >= 600:
        grid_pos1[1] = 30
    pygame.draw.rect(screen,(196, 223, 100), (grid_pos1[0], grid_pos1[1], 30, 30))
    grid_pos1[0] += 60
    if grid_pos1[0] >= 450:
      grid_pos1[0] = 30

  for i in range(12):
    for j in range(14):
      pygame.draw.rect(screen,(196, 223, 100), (grid_pos2[0], grid_pos2[1], 30, 30))
      grid_pos2[1] += 60
      if grid_pos2[1] >= 600:
        grid_pos2[1] = 60
    pygame.draw.rect(screen,(196, 223, 100), (grid_pos2[0], grid_pos2[1], 30, 30))
    grid_pos2[0] += 60
    if grid_pos2[0] >= 450:
      grid_pos2[0] = 60

  for i in range(12):
    for j in range(14):
      pygame.draw.rect(screen, (156, 183, 68), (grid_pos3[0], grid_pos3[1], 30, 30))
      grid_pos3[1] += 60
      if grid_pos3[1] >= 600:
        grid_pos3[1] = 60
    pygame.draw.rect(screen, (156, 183, 68), (grid_pos3[0], grid_pos3[1], 30, 30))
    grid_pos3[0] += 60
    if grid_pos3[0] >= 450:
      grid_pos3[0] = 30

  for i in range(12):
    for j in range(14):
      pygame.draw.rect(screen, (156, 183, 68), (grid_pos4[0], grid_pos4[1], 30, 30))
      grid_pos4[1] += 60
      if grid_pos4[1] >= 600:
        grid_pos4[1] = 30
    pygame.draw.rect(screen, (156, 183, 68), (grid_pos4[0], grid_pos4[1], 30, 30))
    grid_pos4[0] += 60
    if grid_pos4[0] >= 450:
      grid_pos4[0] = 60


# 이벤트
running = True
while running :
  clock.tick(10)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT and direction != 'right':
        direction = 'left'
      elif event.key == pygame.K_RIGHT and direction != 'left':
        direction = 'right'
      elif event.key == pygame.K_UP and direction != 'down':
        direction = 'up'
      elif event.key == pygame.K_DOWN and direction != 'up':
        direction = 'down'
        

  if direction == 'left':
    snake_pos[0] -= 30
  elif direction == 'right':
    snake_pos[0] += 30
  elif direction == 'up':
    snake_pos[1] -= 30
  elif direction == 'down':
    snake_pos[1] += 30
  
  # 벽 충돌처리
  if snake_pos[0] <= 0 or snake_pos[0] >= screen_width-30:
    running = False
  elif snake_pos[1] <=0 or snake_pos[1] >= screen_height-30:
    running = False

  # 뱀 머리-몸 충돌처리
  for snake in snake_body[:-1]:
    if pygame.Rect(snake_pos[0], snake_pos[1], 30, 30).colliderect(pygame.Rect(snake[0], snake[1], 30, 30)):
      running = False
  
  # 캐릭터, 배경 그리기
  screen.fill((80, 120, 10))
  draw_backround()
  pygame.font 

  for snake in snake_body:
    pygame.draw.rect(screen, (100, 100, 100), (snake[0], snake[1], 30, 30))


  screen.blit(fruits[fruit_decide], (fruit_pos[0],fruit_pos[1]))

  snake_body.append(list(snake_pos))
  
  # 과일 충돌처리
  if pygame.Rect(snake_pos[0],snake_pos[1], 30, 30).colliderect(pygame.Rect(fruit_pos[0],fruit_pos[1], 30, 30)) :
    fruit_pos = [random.randrange(30, screen_width-30,30),random.randrange(30, screen_height-30,30)]
    fruit_decide = random.randint(0,len(fruits)-1)
    score += 5
    if fruit_pos in snake_body:
      fruit_pos = [random.randrange(30, screen_width-30,30),random.randrange(30, screen_height-30,30)]
  else:
    snake_body.pop(0)
  
  # 점수 나타내기
  score_font = font.render(f'score : {score}', True, (255, 255, 255))
  font_pos = score_font.get_rect(center = (screen_width/2, 15))
  screen.blit(score_font, font_pos)  
  
  pygame.display.update()

pygame.quit()