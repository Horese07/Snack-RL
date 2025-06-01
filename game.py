import pygame
import random
from enum import Enum
from collections import namedtuple
import numpy as np

pygame.init()
font = pygame.font.Font('images/arial.ttf', 25)

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

Point = namedtuple('Point', 'x, y')

WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
BLACK = (0, 0, 0)
LIGHT_GREEN = (144, 238, 144)
GRID_COLOR = (40, 40, 40)

BLOCK_SIZE = 20
SPEED = 40

class SnakeGameAI:
    def __init__(self, w=640, h=480):
        self.w = w
        self.h = h
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Snake')
        try:
            self.background = pygame.image.load('images/background.jpg').convert()
            self.background = pygame.transform.scale(self.background, (w, h))
        except:
            print("Background image not found! Using fallback color.")
            self.background = None
            self.fallback_bg_color = (144, 238, 144)  
        self.clock = pygame.time.Clock()
        self.font = font
        self.apple_img = pygame.transform.scale(pygame.image.load("images/apple.png"), (BLOCK_SIZE, BLOCK_SIZE))
        self.snake_img=pygame.transform.scale(pygame.image.load("images/snake.png"), (BLOCK_SIZE, BLOCK_SIZE))
        self.reset()

    def reset(self):
        self.direction = Direction.RIGHT
        self.head = Point(self.w // 2, self.h // 2)
        self.snake = [self.head,
                      Point(self.head.x - BLOCK_SIZE, self.head.y),
                      Point(self.head.x - 2*BLOCK_SIZE, self.head.y)]
        self.score = 0
        self.food = None
        self._place_food()
        self.frame_iteration = 0
        self.steps_since_last_food = 0


    def _place_food(self):
        x = random.randint(0, (self.w - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (self.h - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        self.food = Point(x, y)
        if self.food in self.snake:
            self._place_food()

    def play_step(self, action):
       self.frame_iteration += 1
       self.steps_since_last_food += 1

       for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
       #Direction
       self._move(action)
       self.snake.insert(0, self.head)

       reward = 0
       game_over = False

    # Collision or too many unproductive steps
       if self.is_collision() or self.steps_since_last_food > 100:
        game_over = True
        reward = -10
        return reward, game_over, self.score

    # Food eaten
       if self.head == self.food:
        self.score += 1
        reward = 10
        self._place_food()
        self.steps_since_last_food = 0  # Reset step count on progress
       else:
        self.snake.pop()

       self.update_ui()
       self.clock.tick(SPEED)
       return reward, game_over, self.score
    

    def is_collision(self, pt=None):
        if pt is None:
            pt = self.head
        if pt.x > self.w - BLOCK_SIZE or pt.x < 0 or pt.y > self.h - BLOCK_SIZE or pt.y < 0:
            return True
        if pt in self.snake[1:]:
            return True
        return False

    def update_ui(self):
           # Draw background (image or fallback color)
        if self.background:
            self.display.blit(self.background, (0, 0))
        else:
            self.display.fill(self.fallback_bg_color)

        for pt in self.snake:
            self.display.blit(self.snake_img, (pt.x, pt.y))
        self.display.blit(self.apple_img, (self.food.x, self.food.y))
        text = self.font.render("Score: " + str(self.score), True, WHITE)
        self.display.blit(text, [0, 0])
        pygame.display.flip()

    def _move(self, action):
        clock_wise = [Direction.RIGHT, Direction.DOWN, Direction.LEFT, Direction.UP]
        idx = clock_wise.index(self.direction)

        if np.array_equal(action, [1, 0, 0]):
            new_dir = clock_wise[idx]
        elif np.array_equal(action, [0, 1, 0]):
            new_dir = clock_wise[(idx + 1) % 4]
        else:
            new_dir = clock_wise[(idx - 1) % 4]

        self.direction = new_dir
        x, y = self.head.x, self.head.y
        if self.direction == Direction.RIGHT: x += BLOCK_SIZE
        elif self.direction == Direction.LEFT: x -= BLOCK_SIZE
        elif self.direction == Direction.DOWN: y += BLOCK_SIZE
        elif self.direction == Direction.UP: y -= BLOCK_SIZE

        self.head = Point(x, y)
