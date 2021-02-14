import gym
from DQN_Agent import DQN
import torch as T

if __name__ =='__main__':
    env = gym.make('Acrobot-v1')
    DQN = DQN(lr=0.001, inputDims=[6], fc1Dims=128, fc2Dims=128, nActions=3)
    DQN.load_state_dict(T.load('./Acrobot/acrobot-model.pt'))

    score = 0
    state = env.reset()
    done = False

    while not done:

        action = T.argmax(DQN(T.tensor([state]).float().to(DQN.device))).item()
        stateNew, reward, done, info = env.step(action)        
        env.render()
        score += reward
        state = stateNew

    print('Score: ', score)