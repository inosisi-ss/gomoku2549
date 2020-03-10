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

def column(piece):
    colu = piece[0:-4]+piece[1:-3]+piece[2:-2]+piece[3:-1]
    if (colu==4).any(): print("True")
    print(colu)

print(board)
piece = np.where(board==2, 1, 0)
print(piece)
column(piece)
piece = np.where(board==3, 1, 0)
print(piece)
column(piece)
