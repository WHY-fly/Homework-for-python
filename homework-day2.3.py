"""这个是2026年7月8号课后作业"""
import numpy as np
import matplotlib.pyplot as plt
def task1_numpy_basic():
    print("===== 任务1：NumPy数组基础操作 =====")
    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.array([[1, 2, 3], [4, 5, 6]])
    arr3 = np.array([
        [[1, 2], [3, 4]],
        [[5, 6], [7, 8]]
    ])
    print("\n数组索引和切片")
    print("arr1 的第一个元素：", arr1[0])
    print("arr1 的第 2 到第 4 个元素：", arr1[1:4])
    print("arr2 的第一行：", arr2[0])
    print("arr2 的第二列：", arr2[:, 1])
    print("arr3 的第一个二维数组：")
    print(arr3[0])
    print("\n数组形状变换")
    new_arr1 = arr1.reshape(5, 1)
    new_arr2 = arr2.reshape(3, 2)
    flat_arr2 = arr2.flatten()
    print("arr1 变成 5 行 1 列：")
    print(new_arr1)
    print("arr2 变成 3 行 2 列：")
    print(new_arr2)
    print("arr2 展平后：")
    print(flat_arr2)
    print("\n矩阵基本运算")
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])
    print("矩阵 A：")
    print(a)
    print("矩阵 B：")
    print(b)
    print("矩阵加法 A + B：")
    print(a + b)
    print("矩阵乘法 A × B：")
    print(np.dot(a, b))
    print("矩阵 A 的转置：")
    print(a.T)
    print("\n随机数据和统计分析")
    np.random.seed(42)
    random_data = np.random.randint(1, 101, 20)
    print("随机数组：")
    print(random_data)
    print("平均值：", np.mean(random_data))
    print("最大值：", np.max(random_data))
    print("最小值：", np.min(random_data))
    print("标准差：", np.std(random_data))


def task2_finance_analysis():
    print("\n任务2：金融数据分析实践")
    np.random.seed(7)
    start_price = np.array([100.0, 80.0, 120.0])
    random_returns = np.random.normal(0.001, 0.02, (60, 3))
    prices = [start_price]
    for one_day_return in random_returns:
        next_price = prices[-1] * (1 + one_day_return)
        prices.append(next_price)
    prices = np.array(prices)
    print("前 5 天价格数据：")
    print(prices[:5])
    print("\n2. 计算收益率")
    returns = (prices[1:] - prices[:-1]) / prices[:-1]
    print("前 5 天收益率：")
    print(returns[:5])
    print("\n3. 计算平均收益率和波动率")
    mean_returns = np.mean(returns, axis=0)
    volatility = np.std(returns, axis=0)
    print("平均收益率：")
    print(mean_returns)
    print("波动率：")
    print(volatility)
    print("\n4. 计算移动平均线")
    window = 5
    weights = np.ones(window) / window
    moving_avg = np.convolve(prices[:, 0], weights, mode="valid")
    print("第一只股票的 5 日移动平均线前 10 个值：")
    print(moving_avg[:10])
    print("\n5. 投资组合风险分析")
    cov_matrix = np.cov(returns.T)
    var_array = np.var(returns, axis=0)
    weights = np.array([0.4, 0.3, 0.3])
    portfolio_var = np.dot(weights, np.dot(cov_matrix, weights))
    print("各股票方差：")
    print(var_array)
    print("协方差矩阵：")
    print(cov_matrix)
    print("投资组合方差：", portfolio_var)


def main():
    task1_numpy_basic()
    task2_finance_analysis()


if __name__ == "__main__":
    main()
