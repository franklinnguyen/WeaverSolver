# WeaverSolver

**Weaver Solver**
- This is a Python-based solver for the word game "Weaver". The game challenges you to transition from a starting 4-letter English word to a target 4-letter English word. The rules are that each step of the transition can only involve changing one letter, and every intermediate word must be a valid English word.

- This repository contains a script with helper functions to find valid words, create a dictionary of possible words, and calculate the shortest path from the start to the goal.

**File Structure**
weaver/
weaver_solver.py: The Python script that contains the Weaver game solver algorithm and helper functions.
english.txt: A text file containing valid English words.

**Function Descriptions**
- Here are the primary functions included in the weaver_solver.py script:
  - get_neighbors(word): Given a 4-letter English word, this function returns all valid neighbors of the word. A neighbor is a word that differs by just one letter. The returned neighbors are sorted by their frequency in English, from most to least common.
  - weaver_solver(start, goal): This function calculates the shortest path from the starting word to the goal word. It uses a breadth-first search strategy and returns the optimal path. If no path exists, it returns an appropriate error message.
  - find_changes(start, path): This helper function identifies which letter changes between each pair of words in a given path.
  - weaver_hints(start, goal): This function interacts with the user to offer progressive hints about the solution path. It can tell you the length of the optimal solution, which letter to change at each step, and the complete solution path if requested.

**Usage**
- To use this script, follow these steps:
  1. Clone this repository to your local environment.
  2. Prepare your starting and goal 4-letter words.
  3. Call the weaver_solver(start, goal) function to find the shortest path between the two words.
  4. Alternatively, call the weaver_hints(start, goal) function if you prefer to receive hints rather than the direct solution.

**Dependencies**
- This script requires Python 3 and relies on the included english.txt text file for its list of valid English words.
