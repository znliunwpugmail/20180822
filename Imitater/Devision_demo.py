from ImitaterData import imitater_user
import time
import tensorflow as tf
from ImitaterData import imitater_user
from ImitaterData import imitater_capacility
from DQN_net import dqn
import numpy as np
import datetime
import operator as op
import random
EPISDOE = 10000
STEP = 10000
LAMBDA = 0.01

class Devision():
    def __init__(self):
        self.user_create = imitater_user.User_Create()
        self.capacility_create = imitater_capacility.Capacility_Create()

    def generate_state(self):
        if len(self.user_create.alluser_sequence) > 0:
            nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            i = 0;
            while i < len(self.user_create.alluser_sequence):
                user_attributes = self.user_create.alluser_sequence[i]
                user_leavetime = user_attributes[-1]
                if op.ge(nowTime, user_leavetime):
                    print('i',i)
                    self.user_create.alluser_sequence.remove(user_attributes)
                    del self.user_create.alluser_action[i]
                    i-=2
                    print('i1',i)
                i+=1

        self.user_create.Imitate_User()
        self.user_create.alluser_sequence.extend(self.user_create.currentuser_sequence)

    def relu(self,x):
        """Compute softmax values for each sets of scores in x."""
        x[x<0] = 0
        return x
    def train(self):
        while 1 == 1:
            for episode in range(EPISDOE):
                action_dim = 3
                state_dim = action_dim*2
                agent = dqn.DQN(action_dim, state_dim)
                total_reward = 0
                self.user_create = imitater_user.User_Create()
                self.generate_state()
                user_state_list = self.user_create.currentuser_sequence
                user_states = []

                for user_list in user_state_list:
                    user_states.append(user_list[1:4])
                capacility_state = self.capacility_create.capacility_state
                print('start ')
                for step in range(len(user_states)):
                    user_state = user_states[step]
                    state = user_state+capacility_state.tolist()
                    action = agent.get_action([state])
                    accept_propability = np.array(user_state)[action]
                    rand_prop = random.uniform(0, 1)
                    if rand_prop<accept_propability:
                        g_at = 1
                    else:
                        g_at = 0
                        # action = action_dim-1
                    self.user_create.alluser_action.append(action)
                    if step == len(user_states)-1:
                        next_user_state = user_state
                    else:
                        next_user_state = user_states[step+1]

                    self.capacility_create.compute_decrease_capacility(action)
                    next_capacility_state = self.capacility_create.capacility_state
                    reward = g_at - LAMBDA * np.max(self.relu(-1*next_capacility_state)//500)
                    total_reward+=reward
                    next_state = next_user_state+next_capacility_state.tolist()
                    agent.percieve(state,action,reward,next_state,False)
                    print(capacility_state)

                print('total reward this episode is: ', total_reward)

    def motivation(self):
        pass

def generate_state():
    pass

if __name__ == '__main__':
    devision = Devision()
    devision.train()


