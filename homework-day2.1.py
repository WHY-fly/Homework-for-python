"""这里是2026年7月8日上午的作业"""
import numpy as np
# 练习 1
arr = np.random.randint(0, 10, size=(3, 4))
print("1. 原数组 (3x4):\n", arr)
reshaped_arr = arr.reshape(4, 3).T
print("2. 重塑为 (4,3) 并转置后:\n", reshaped_arr)
filtered_arr = arr[arr > 5]
print("3. 大于5的元素:\n", filtered_arr)
print("-" * 30)
# 练习2
arr2 = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12]])
ans1 = arr2[1, 0:3]
print("1. 第2行第1~3列:", ans1)
ans2 = arr2[:, 2]
print("2. 所有行的第3列:", ans2)
ans3 = arr2[0:3:2, :]
print("3. 奇数行:\n", ans3)
print("-" * 30)
# 练习3
A = np.random.randint(1, 5, size=(2, 3))
B = np.random.randint(1, 5, size=(2, 3))
print("1. A 和 B 的逐元素乘法 (*):\n", A * B)
print("1. A 和 B 的矩阵乘法 (@):\n", A @ B.T)
C = np.array([[1, 2],
              [3, 4]])
print("2. 按列求和 (axis=0):", np.sum(C, axis=0))
print("2. 按行求和 (axis=1):", np.sum(C, axis=1))
D = np.array([1.2, 3.5, 2.8])
print("3. 均值:", np.mean(D))
print("3. 标准差:", np.std(D))
print("3. 四舍五入:", np.round(D))
print("-" * 30)
# 练习 4
rand_arr = np.random.rand(10)
arr_min = np.min(rand_arr)
arr_max = np.max(rand_arr)
normalized_arr = (rand_arr - arr_min) / (arr_max - arr_min) * 100
print("1. 归一化后的数组:\n", normalized_arr)
print("2. 累计和 (cumsum):\n", np.cumsum(normalized_arr))
print("2. 累计最大值 (cummax):\n", np.maximum.accumulate(normalized_arr))
