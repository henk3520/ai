#chatgpt輔助
import numpy as np

# 定義目標函數的係數
def objective_function(x, y, z):
    return 3*x + 2*y + 5*z

# 定義約束條件
def constraints(x, y, z):
    return [
        x + y <= 10,
        2*x + z <= 9,
        y + 2*z <= 11,
        x >= 0,
        y >= 0,
        z >= 0
    ]

# 設定隨機搜索的參數
num_samples = 1000000  # 生成的隨機樣本數

# 初始化最佳解
best_value = -np.inf
best_solution = None

# 隨機生成解並檢查是否滿足約束條件
for _ in range(num_samples):
    x = np.random.uniform(0, 10)
    y = np.random.uniform(0, 10)
    z = np.random.uniform(0, 9)
    
    if all(constraints(x, y, z)):
        value = objective_function(x, y, z)
        if value > best_value:
            best_value = value
            best_solution = (x, y, z)

# 輸出結果
if best_solution:
    print(f"Optimal value (approximate): {best_value}")
    print(f"x = {best_solution[0]}")
    print(f"y = {best_solution[1]}")
    print(f"z = {best_solution[2]}")
else:
    print("No solution found")
