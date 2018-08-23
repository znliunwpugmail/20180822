import os
import datetime
import time
import random
import numpy as np
import sqlite3

from ImitaterData.imitater_user import *
from DQN_net import dqn

np.set_printoptions(suppress=True)

"自助、引流、人工"

class Capacility_Create():
    def __init__(self):
        self.user_dict = {}
        self.capacility_state = np.ones(shape=[3])*1000
        self.capacility_state[0:2] = self.capacility_state[0:2]*5

    def compute_decrease_capacility(self,actions):#"actions is a number"
        actions = np.array(actions)
        self.capacility_state[actions]-=1

    def compute_increase_capacility(self,actions):#"actions is a number"
        actions = np.array(actions)
        self.capacility_state[actions] += 1

if __name__ == '__main__':

    second = sleeptime(0, 0, 4);
    user_create = User_Create()
    while 1 == 1:
        # time.sleep(second);
        print(len(user_create.alluser_sequence))
        if len(user_create.alluser_sequence) > 0:
            nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            for i in range(len(user_create.alluser_sequence)):
                user_attributes = user_create.alluser_sequence[i]
            # for user_attributes in user_create.alluser_sequence:
                user_leavetime = user_attributes[-1]
                if op.gt(nowTime, user_leavetime):
                    user_create.alluser_sequence.remove(user_attributes)
        print(len(user_create.alluser_sequence))
        user_create.Imitate_User()
        user_create.alluser_sequence.extend(user_create.currentuser_sequence)