import random

# 城市座標
citys = [
    (0, 3), (0, 0),
    (0, 2), (0, 1),
    (1, 0), (1, 3),
    (2, 0), (2, 3),
    (3, 0), (3, 3),
    (3, 1), (3, 2)
]

# 初始路徑
l = len(citys)
path = [(i + 1) % l for i in range(l)]
print('Initial path:', path)

# 計算兩個點之間的距離
def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# 計算路徑的總距離
def pathLength(p):
    dist = 0
    plen = len(p)
    for i in range(plen):
        dist += distance(citys[p[i]], citys[p[(i + 1) % plen]])
    return dist

print('Initial path length:', pathLength(path))

# 生成鄰域解
def generate_neighbors(route):
    neighbors = []
    for i in range(len(route)):
        for j in range(i + 1, len(route)):
            neighbor = route[:]
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    return neighbors

# 爬山演算法
def hill_climbing(citys, max_iterations=1000):
    l = len(citys)
    # 隨機生成初始解
    current_route = list(range(l))
    random.shuffle(current_route)
    current_distance = pathLength(current_route)
    
    for iteration in range(max_iterations):
        neighbors = generate_neighbors(current_route)
        next_route = None
        next_distance = float('inf')
        
        # 找出最好的鄰域解
        for neighbor in neighbors:
            distance = pathLength(neighbor)
            if distance < next_distance:
                next_distance = distance
                next_route = neighbor
        
        # 如果找不到更好的解，則停止
        if next_distance >= current_distance:
            break
        
        # 更新當前解
        current_route = next_route
        current_distance = next_distance
        
    return current_route, current_distance

# 測試
if __name__ == "__main__":
    route, distance = hill_climbing(citys)
    print("Best route:", route)
    print("Best distance:", distance)
