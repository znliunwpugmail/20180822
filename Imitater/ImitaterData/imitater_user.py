import os
import datetime
import time
import random
import numpy as np
import sqlite3

import operator as op
np.set_printoptions(suppress=True)

class User_Create():
    def __init__(self):
        self.alluser_sequence = []
        self.alluser_action = []
        self.alluser_action = []
        self.currentuser_sequence = []

    def Time_Leave(self,nowTime,time_s):
        time_date,time_hsm = nowTime.split(' ')
        h,s,m = time_hsm.split(':')
        s = int(s)+(int(m)+time_s)//60
        m = int(m)+(int(m)+time_s)%60
        time_hsm = str(h)+":"+str(s)+":"+str(m)
        leaveTime = time_date+" "+time_hsm
        return leaveTime





    def Imitate_User(self,attributes_num = 3,max_time_interval = 60):
        "App SMS Channel_broadcast Drainage_online Reservation_callback Artificial_hotline"

        # #delete the overtime users
        # if len(self.alluser_sequence)>0:
        #     # print(len(self.alluser_sequence))
        #     nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        #     for user_attributes in self.alluser_sequence:
        #         user_leavetime = user_attributes[-1]
        #         if op.gt(nowTime,user_leavetime):
        #             self.alluser_sequence.remove(user_attributes)
        #     # print(len(self.alluser_sequence))

        users_num = random.randint(100,1000)
        users_num = 100
        Station0 = np.ones(shape=[users_num,attributes_num+1],dtype=np.float)
        seq = list(range(0, 1000))
        users_id = random.sample(seq,users_num)
        users_id = np.array(users_id)
        Station0[:,0]=users_id

        time_speed = [random.randint(0,6) for _ in range(users_num)]

        for i in range(1,attributes_num):
            f_random = [random.randint(0,100) for _ in range(users_num)]
            f_random = np.array(f_random)/100
            Station0[:,i]=f_random
        Station0_list = Station0.tolist()
        Station0_list_result=[]



        for i in range(len(Station0_list)):
            Station0_list_i = Station0_list[i]
            time_s = time_speed[i]
            nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在
            Station0_list_i.append(nowTime)
            leaveTime = self.Time_Leave(nowTime,time_s)
            # Station0_list_i.append(time_s)
            Station0_list_i.append(leaveTime)
            Station0_list_result.append(Station0_list_i)
            # self.alluser_sequence.append(Station0_list_i)
        # print(Station0_list_result)
        self.currentuser_sequence = Station0_list_result
        # print(self.currentuser_sequence)
        return np.array(Station0_list_result)

def sleeptime(hour,min,sec):
    return hour*3600 + min*60 + sec;

if __name__ == '__main__':
    second = sleeptime(0,0,4);
    user_create = User_Create()
    while 1==1:
        # time.sleep(second);
        if len(user_create.alluser_sequence) > 0:
            nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            for user_attributes in user_create.alluser_sequence:
                user_leavetime = user_attributes[-1]
                if op.gt(nowTime, user_leavetime):
                    user_create.alluser_sequence.remove(user_attributes)
        user_create.Imitate_User()
        user_create.alluser_sequence.extend(user_create.currentuser_sequence)
        # delete the overtime users

            # print(len(self.alluser_sequence))