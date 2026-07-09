"""这里是2026年7月8日下午的作业"""
"""题目一，实现如下"""
import numpy as np
A = np.random.rand(1000, 2000)
B = np.random.rand(2000, 3000)
res1 = np.dot(A, B)
res2 = A @ B
res3 = np.matmul(A, B)
C_arr = np.ones((1000, 1000), order='C')
F_arr = np.ones((1000, 1000), order='F')
sum_row_C = C_arr.sum(axis=1)
sum_row_F = F_arr.sum(axis=1)
sum_col_C = C_arr.sum(axis=0)
sum_col_F = F_arr.sum(axis=0)
result = np.empty_like(A)
np.multiply(A, A, out=result)      # result = A^2
np.add(result, 2 * A, out=result)  # result = A^2 + 2A
np.add(result, 1, out=result)      # result = A^2 + 2A + 1


"""题目二，实现如下"""
import numpy as np
prices = np.array([100, 102, 105, 103, 107])
returns = np.diff(np.log(prices))
# 生成 100 个随机股价
sim_prices = np.random.rand(100) * 100
# 5日移动平均
ma5 = np.convolve(sim_prices, np.ones(5)/5, mode='valid')
# 20日移动平均
cumsum_prices = np.cumsum(sim_prices)
cumsum_prices[20:] = cumsum_prices[20:] - cumsum_prices[:-20]
ma20 = cumsum_prices[19:] / 20
# 生成 1000支股票 252天的随机收益率
returns_data = np.random.normal(0.001, 0.02, (1000, 252))
# 计算年化波动率
annual_volatility = np.std(returns_data, axis=1) * np.sqrt(252)
# 计算相关系数矩阵
corr_matrix = np.corrcoef(returns_data)
