import numpy as np
import cv2
import time
import sys

class make_map():
    def __init__(self):
        self.map_size = 101
        while self.map_size<3 or np.mod(self.map_size, 2)==0: self.map_size += 1
        self.plot_size = 5
        #define color
        self.wall_color = [0., 0., 0.]
        self.root_color = [1., 1., 1.]
        self.init_color = [0., 0., 1.]
        self.goal_color = [0., 1., 0.]
        self.char_color = [1., 0., 0.]

        self.reset_env()
        self.make_map_base()
        #self.rander()

        self.training = True

    def reset_env(self):
        self.char_posi = np.array([1, 1])

    def make_map_base(self):
        #make map base
        self.map_base = np.full((self.map_size+2, self.map_size+2, 3), 0., dtype=np.float32)
        map = self.map_base[1:-1, 1:-1]
        map[:, :] = self.root_color
        wall_x = range(1, self.map_size-1, 2)
        wall_y = range(1, self.map_size-1, 2)

        wall_axis = np.array([np.meshgrid(wall_x, wall_y)])
        wall_axis = wall_axis.reshape(2, -1).transpose(1, 0)

        num2pose = np.array([[-1, 0], [1, 0], [0, -1], [0, 1]])
        for axis in wall_axis:
            map[axis[0], axis[1]] = self.wall_color

            index = np.arange(4)
            np.random.shuffle(index)
            for i in index:
                pose = axis+num2pose[i]
                if (map[pose[0], pose[1]]==self.root_color).all():
                    map[pose[0], pose[1]] = self.wall_color
                    break
        map[0, 0] = self.init_color
        map[-1, -1] = self.goal_color

        while True:
            map_view = self.map_base.repeat(self.plot_size, axis=0).repeat(self.plot_size, axis=1)
            cv2.imshow("maze_view", map_view)
            key = cv2.waitKey(1)
            if key == 27: sys.exit()

map = make_map()