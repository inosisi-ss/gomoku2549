#coding: utf-8
import numpy as np
board = np.zeros((7, 7))
print(board)

while True:
    act = np.random.randint(0, 7, 2)
    if (board[act[0], act[1]])==0:
        print(act)
        board[act[0], act[1]] = 2
    if (board!=0).all(): break
    act = np.random.randint(0, 7, 2)
    if (board[act[0], act[1]])==0:
        print(act)
        board[act[0], act[1]] = 3
    if (board!=0).all(): break

print(board)
piece = np.where(board==2, 1, 0)
print(piece)
piece = np.where(board==3, 1, 0)
print(piece)