import numpy as np
import cv2
import time
import sys

class agent_q():
    def __init__(self, map_size, plot_size):
        self.map_size = map_size
        while self.map_size<3 or np.mod(self.map_size, 2)==0: self.map_size += 1
        self.plot_size = plot_size

        self.ALPHA = 0.1
        self.GAMMA = 0.9
        self.IPUSI = 0.0
        self.qvalue = np.full((self.map_size + 2, self.map_size + 2, 4), 0.01, dtype=np.float32)
        self.hitmap = np.full((self.map_size + 2, self.map_size + 2, 3), 200, dtype=np.uint8)

        self.training = 1
        
    def act(self, state):
        if np.random.rand() >= self.IPUSI:
            if self.training==1:
                return self.roulette(self.qvalue[state[0], state[1]])
            else:
                return np.argmax(self.qvalue[state[0], state[1]])
        else: return np.random.randint(4)

    def train(self, state, act, reward, state_, done):
        if self.training==1:
            #print(self.qvalue[state[0], state[1]], self.qvalue[state_[0], state_[1]])
            qvalue = self.qvalue[state[0], state[1], act]
            qvalue_ = np.max(self.qvalue[state_[0], state_[1]])
            self.qvalue[state[0], state[1], act] = qvalue + self.ALPHA*(reward + self.GAMMA*done*qvalue_ - qvalue)
            #print("value", self.qvalue[state[0], state[1]])

    def roulette(self, qvalue):
        qvalue = np.clip(qvalue, 0, None)
        prob = qvalue / np.sum(qvalue)
        move = np.random.choice(4, 1, replace=False, p=prob)[0]
        return move
        
    def norm_min_max(self, inp, axis=None):
        inp = np.array(inp)
        inp_min = inp.min(axis=axis, keepdims=True)
        inp_max = np.maximum(inp.max(axis=axis, keepdims=True), 1e-1)
        #print inp_min, inp_max
        output = (inp - inp_min) / np.maximum((inp_max - inp_min), 1e-9)
        return output

    def float2int(self, inp):
        output = np.round((inp*2+1)//2).astype(int)
        return output

    def plot_heatmap(self, name="heatmap"):
        hitmap = self.hitmap.copy()
        q_max = np.max(self.qvalue, axis=2)
        q_max = 140.*self.norm_min_max(np.log(q_max))
        hitmap[:, :, 0] = self.float2int(q_max)
        plot = cv2.cvtColor(hitmap, cv2.COLOR_HSV2RGB)
        #plot = cv2.resize(plot, (self.map_range*10, self.map_range*10))
        plot = plot.repeat(self.plot_size, axis=0).repeat(self.plot_size, axis=1)
        cv2.imshow(name, plot)
        cv2.waitKey(1)
