# Conway's Game of Life - Pygame Implementation

## Overview
This project is a **Pygame-based simulation** of Conway's Game of Life, a famous cellular automaton devised by the mathematician **John Conway** in 1970. The simulation runs on a 2D grid where cells evolve over discrete time steps according to a set of simple rules. The goal is to observe emergent patterns and behaviors that arise from simple initial conditions.

## Features
- **Interactive Grid**: Click to add or remove cells before starting the simulation.
- **Grid Resizing**: Modify the grid size dynamically.
- **Pause & Resume**: Start and stop the simulation at any time.

## Rules of the Game
Each cell in the grid follows these rules:
1. Any live cell with **fewer than two** live neighbors **dies** (underpopulation).
2. Any live cell with **two or three** live neighbors **survives**.
3. Any live cell with **more than three** live neighbors **dies** (overpopulation).
4. Any dead cell with **exactly three** live neighbors **becomes alive** (reproduction).

## Installation
### Prerequisites
Ensure you have Python (3.x) installed along with Pygame.

```sh
pip install pygame
```

### Running the Project
Clone the repository and execute the main script:

```sh
git clone https://github.com/your-repo/game-of-life-pygame.git
cd game-of-life-pygame
python main.py
```

## Controls
- **Left Click**: Toggle cell state (alive/dead).
- **Right Click**: Toggle cell state (alive/dead)
- **Spacebar**: Start/Pause the simulation.

## Future Improvements
- **Preset Patterns**: Load common patterns like **gliders**, **oscillators**, and **spaceships**.
- Different grid themes and color schemes.
- Optimized simulation using NumPy for better performance.
- Multiplayer mode where users can compete for survival.

## License
This project is licensed under the MIT License. Feel free to modify and contribute.

## Acknowledgments
Inspired by **John Conway's** original Game of Life and various Pygame implementations.

