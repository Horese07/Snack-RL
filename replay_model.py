import torch
import numpy as np
from model import Linear_QNet
from game import SnakeGameAI, Direction, Point

model = Linear_QNet(11, 256, 3)
model.load_state_dict(torch.load("model/best_model.pth"))
model.eval()

def get_state(game):
    head = game.snake[0]
    point_l = Point(head.x - 20, head.y)
    point_r = Point(head.x + 20, head.y)
    point_u = Point(head.x, head.y - 20)
    point_d = Point(head.x, head.y + 20)

    dir_l = game.direction == Direction.LEFT
    dir_r = game.direction == Direction.RIGHT
    dir_u = game.direction == Direction.UP
    dir_d = game.direction == Direction.DOWN

    state = [
        (dir_r and game.is_collision(point_r)) or
        (dir_l and game.is_collision(point_l)) or
        (dir_u and game.is_collision(point_u)) or
        (dir_d and game.is_collision(point_d)),

        (dir_u and game.is_collision(point_r)) or
        (dir_d and game.is_collision(point_l)) or
        (dir_l and game.is_collision(point_u)) or
        (dir_r and game.is_collision(point_d)),

        (dir_d and game.is_collision(point_r)) or
        (dir_u and game.is_collision(point_l)) or
        (dir_r and game.is_collision(point_u)) or
        (dir_l and game.is_collision(point_d)),

        dir_l,
        dir_r,
        dir_u,
        dir_d,

        game.food.x < game.head.x,
        game.food.x > game.head.x,
        game.food.y < game.head.y,
        game.food.y > game.head.y
    ]
    return np.array(state, dtype=int)

def play():
    game = SnakeGameAI()
    while True:
        state = get_state(game)
        state0 = torch.tensor(state, dtype=torch.float)
        prediction = model(state0)
        move = torch.argmax(prediction).item()
        final_move = [0, 0, 0]
        final_move[move] = 1
        reward, done, score = game.play_step(final_move)
        if done:
            game.reset()
            print("Score:", score)

if __name__ == '__main__':
    play()
