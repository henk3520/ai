#chatgpt輔助
import gym

# 創建 CartPole 環境
env = gym.make('CartPole-v1')

def fixed_strategy(observation):
    x, x_dot, theta, theta_dot = observation
    
    # 根據竿子的角度和角速度決定行動
    if theta > 0:
        action = 1  # 向右推
    else:
        action = 0  # 向左推
        
    return action

# 運行策略
observation = env.reset()
total_reward = 0
for t in range(200):
    env.render()
    
    # 根據固定策略選擇動作
    action = fixed_strategy(observation)
    
    # 執行動作
    observation, reward, done, info = env.step(action)
    
    total_reward += reward
    
    if done:
        print(f"Episode finished after {t+1} timesteps")
        break

env.close()
print(f"Total reward: {total_reward}")


