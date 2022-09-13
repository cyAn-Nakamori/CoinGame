import random
import numpy as np
from collections import defaultdict
# import dill

from pettingzoo.classic import tictactoe_v3

env = tictactoe_v3.env()
env.reset()
env.agents

def policy(observation, agent):
    action = random.choice(np.flatnonzero(observation['action_mask']))
    return action

env.reset()
for agent in env.agent_iter():
    observation, reward, done, info = env.last()
    action = policy(observation, agent) if not done else None
    env.step(action)
    env.render() # this visualizes a single game
    print("###############################\n")
