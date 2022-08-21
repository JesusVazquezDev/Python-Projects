import gym
import random
import numpy as np
import time
from collections import deque
import pickle


from collections import defaultdict


EPISODES =  20000
LEARNING_RATE = .1 # Alpha
DISCOUNT_FACTOR = .99 # Gamma
EPSILON = 1
EPSILON_DECAY = .999


def default_Q_value():
    return 0

if __name__ == "__main__":

    random.seed(1)
    np.random.seed(1)
    env = gym.envs.make("FrozenLake-v1")
    env.seed(1)
    env.action_space.np_random.seed(1)

    # You will need to update the Q_table in your iteration
    Q_table = defaultdict(default_Q_value) # starts with a pessimistic estimate of zero reward for each state.
    episode_reward_record = deque(maxlen=100)

    for i in range(EPISODES):
        episode_reward = 0
        done = False
        obs = env.reset()
        test = 0

        ##########################################################
        # YOU DO NOT NEED TO CHANGE ANYTHING ABOVE THIS LINE
        while (not done):
            if random.uniform(0,1) < EPSILON:
                current_best_action = env.action_space.sample()
            else:
                prediction = np.array([Q_table[(obs,i)] for i in range(env.action_space.n)])
                current_best_action =  np.argmax(prediction)
                
            # env.step(action):
            # Given that the environment is in state s, step takes an
            # integer specifiying the chosen action, and returns a tuple
            # of the form (s, r, done, info). ’done’ specifies whether or
            # not s′ is the final state for that particular episode, and
            # ’info’ is unused in this assignment.
            next_obs,reward,done,info = env.step(current_best_action)
            
            next_prediction = np.array([Q_table[(next_obs,i)] for i in range(env.action_space.n)])
            
            # Finding next best action values 
            # (not the argument, but the values themselves)
            next_best_action = max(next_prediction)
            
            # Assigning new value in Q_table
            Q_table[obs, current_best_action] = (1-LEARNING_RATE) * Q_table[(obs, current_best_action)] + LEARNING_RATE * (reward + DISCOUNT_FACTOR * next_best_action)
        
            # Setting next state
            obs = next_obs
            
            # Updating episode reward
            episode_reward += reward 
            
            
        # Once done
        if random.uniform(0,1) < EPSILON:
            current_best_action = env.action_space.sample()
        else:
            prediction = np.array([Q_table[(obs,i)] for i in range(env.action_space.n)])
            current_best_action =  np.argmax(prediction)
                
        next_obs,reward,done,info = env.step(current_best_action)

        # Assigning new value in Q_table
        Q_table[obs, current_best_action] = (1-LEARNING_RATE) * Q_table[(obs, current_best_action)] + LEARNING_RATE * reward
        
        # Updating episode reward
        episode_reward += reward
        
        # Updating for new episode
        EPSILON = EPSILON * EPSILON_DECAY
        
        # END of TODO
        # YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE
        ##########################################################

        # record the reward for this episode
        episode_reward_record.append(episode_reward) 

        
        if i%100 ==0 and i>0:
            print("LAST 100 EPISODE AVERAGE REWARD: " + str(sum(list(episode_reward_record))/100))
            print("EPSILON: " + str(EPSILON) )
    
    
    #### DO NOT MODIFY ######
    model_file = open('Q_TABLE.pkl' ,'wb')
    pickle.dump([Q_table,EPSILON],model_file)
    model_file.close()
    #########################