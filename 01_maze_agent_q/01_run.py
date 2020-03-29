import numpy as np
import cv2
import time
import sys

import q_agent
import how_made_maze

def main():
    maze_map = how_made_maze.make_map()
    maze_map.char_move()
    agent = q_agent.agent_q(maze_map.map_size, maze_map.plot_size)
    while True:
        agent.training = maze_map.training
        time.sleep(0.05)
        state = maze_map.char_posi
        act = agent.act(state)
        print("act:", act)
        reward, done = maze_map.char_act(act)
        maze_map.char_move()
        agent.training = maze_map.training
        state_ = maze_map.char_posi
        print("sars:", state, act, reward, state_)
        agent.train(state, act, reward, state_, done)
        agent.plot_heatmap()

if __name__ == "__main__":
    main()
