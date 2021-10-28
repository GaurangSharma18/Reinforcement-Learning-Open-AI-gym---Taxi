# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 23:37:01 2021

@author: gaurang
"""

# Load OpenAI Gym and other necessary packages
import gym
import random
import numpy
import time

# Environment
env = gym.make("Taxi-v3")

# Training parameters for Q learning
alpha = 0.9 # Learning rate
gamma = 0.9 # Future reward discount factor
num_of_episodes = 1000
num_of_steps = 500 # per each episode

#print(alpha)
# Q tables for rewards
#Q_reward = -100000*numpy.ones((500,6)) # All same
# Q_reward = -100000*numpy.random.random((500, 6)) # Random
Q_reward = -100000*numpy.zeros((500,6))
for episodesCount in range(0,num_of_episodes):
    stateBeforeAction = env.reset();
    # action = random.randint(0,3);
    actionLoop = numpy.argmax(Q_reward[stateBeforeAction,:])
    for stateLoop in range(0,num_of_steps):
        
        getOldQ=(1-alpha)*Q_reward[stateBeforeAction,actionLoop];
        
        stateAfterAction, rewardAfterAction, doneAfterAction, infoAfterAction = env.step(actionLoop);
        
        
        getLearnedValue=alpha*(rewardAfterAction+(gamma*(numpy.max(Q_reward[stateAfterAction,:]))))
        
        getNewQvalue=getOldQ+getLearnedValue;
        Q_reward[stateBeforeAction,actionLoop]=getNewQvalue;
        actionLoop = numpy.argmax(Q_reward[stateAfterAction,:])
        stateBeforeAction=stateAfterAction
        

#taxi_row, taxi_col, passenger_location, destination = env.encode(state);
#print(taxi_row)
# Testing

rewardList=numpy.array([]);
actionLists=numpy.array([]);
for takingAverages in range(0,20):
    state = env.reset()
    tot_reward = 0;
    countActions =0;
    for t in range(50):  # default 50
        action = numpy.argmax(Q_reward[state,:])
        state, reward, done, info = env.step(action)
        tot_reward += reward
        env.render()
        time.sleep(0.1);
        countActions+=1;
        if done:
            print("Total reward %d" %tot_reward)
            rewardList=numpy.append(rewardList,[tot_reward]);
            actionLists=numpy.append(actionLists,[countActions]);
            print("Total Actions "+str(countActions));
            break

print("------------------------------------------------")
print("Averages are : - ")
print("All Actions :- "+str(actionLists))
print("All Rewards :- "+str(rewardList))
print("Average Actions "+str(numpy.mean(actionLists)));
print("Average Rewards "+str(numpy.mean(rewardList)));