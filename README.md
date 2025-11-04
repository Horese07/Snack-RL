# Snack-RL

A small reinforcement learning project that trains an agent to play Snake. The repository contains game logic, an RL agent and model code, a replay buffer implementation, utilities, and a script to play the game as a human. A training progress image is included to show example training results.

## Main features
- An RL agent for the Snake game (neural-network-based Q-function + experience replay).
- Full game implementation of Snake for training and evaluation.
- Script to play the Snake game manually (human input).
- Model saving/loading and simple training visualization (training_progress.png).
- Modular layout: separate files for game logic, agent behavior, model architecture and replay buffer.

## Requirements
- Python 3.8+
- Typical packages you may need (install with pip):
  - numpy
  - pygame
  - matplotlib
  - torch (or tensorflow) — check model.py for which deep learning framework is used
  - (Optional) other utilities referenced in the code

Note: There is no requirements.txt in the repository; inspect the top of each .py file to confirm exact imports and versions.

## Installation
1. Clone the repo:
   git clone https://github.com/Horese07/Snack-RL.git
2. Change into the repo directory:
   cd Snack-RL
3. Install packages:
   pip install numpy pygame matplotlib
   pip install torch  # if model.py uses PyTorch; otherwise install the appropriate framework

## Quick start / Usage
- Train an agent:
  - The training entry point appears to be agent.py. Run:
    python agent.py
  - Check agent.py for available command-line options (e.g., number of episodes, model save path, hyperparameters).
  - During or after training, models may be saved into the `model/` directory.

- Play as a human:
  - Run the human-play script:
    python snake_game_human.py
  - This launches the Snake game controlled by keyboard input so you can play and test the environment manually.

- Evaluate / visualize:
  - training_progress.png is included to show a sample of training progress (e.g., reward or score over episodes).
  - model/ directory likely holds saved model checkpoints. Use model.py or agent.py to load and run a saved model.

## File overview
- agent.py
  - Training loop and agent orchestration. Handles interactions between the game, the agent, replay buffer, and model saving/logging.
- game.py
  - Implements the Snake game environment (state, transitions, reward logic, collisions, food placement, rendering).
- helper.py
  - Utility functions used across the project (render helpers, state processing, etc.).
- model.py
  - Neural network architecture and forward pass for the agent's Q-function / policy. Check the file for the exact framework (PyTorch/TensorFlow).
- replay_model.py
  - Implementation of an experience replay buffer used to store transitions and sample minibatches for training.
- snake_game_human.py
  - Script to run the Snake game with keyboard controls for human play/testing.
- model/ (directory)
  - Intended location for saved model checkpoints.
- images/ (directory)
  - Image assets (if used) for rendering or README visuals.
- training_progress.png
  - Example plot showing training progress (score or reward over time).

## How it works (high-level)
1. The game environment (game.py) provides states, rewards, and terminal signals for each action taken.
2. The agent (agent.py) selects actions using a model (model.py). During training it will explore and exploit to learn.
3. Transitions (state, action, reward, next_state, done) are stored in the replay buffer (replay_model.py).
4. The agent samples minibatches from the replay buffer to update model parameters (neural network) using gradient descent.
5. Models are periodically saved; training progress is logged and can be visualized.

## Tips & notes
- Check the top of each Python file for required imports and parameters (learning rate, batch size, epsilon schedule, etc.).
- If model.py uses a specific deep learning framework, install that framework (PyTorch/TensorFlow) before training.
- If you want reproducible results, set random seeds and check agent.py for seed options.
- For faster training consider running without rendering (headless training), or increase the update frequency and batch size.

## Contributing
Contributions, bug reports and improvements are welcome. Good first tasks:
- Add a requirements.txt with pinned versions.
- Add a command-line interface to agent.py and snake_game_human.py with helpful --help output.
- Add automated tests for the environment (game.py) and replay buffer (replay_model.py).
- Add documentation on hyperparameters and how to reproduce training plots.

## License
No license file is present in the repository. Add a LICENSE file if you want to make the project open source and specify reuse conditions.

## Contact
Repository owner: Horese07 — https://github.com/Horese07
