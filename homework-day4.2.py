#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

import numpy as np
import pandas as pd

try:
    import matplotlib.pyplot as plt

    plt.switch_backend("Agg")
except ImportError:
    plt = None


OUTPUT_DIR = r"D:\codex\outputs\homework-day4.2"


def create_dirty_data():
    data = {
        "PassengerId": [1, 2, 3, 4, 4, 5, 6, 7, 8, 9],
        "Name": ["Alice", "Bob", "Cindy", "David", "David", "Eva", "Frank", "Grace", "Helen", "Ivan"],
        "Age": [22, np.nan, 35, -5, -5, 28, np.nan, 42, 120, 30],
        "Fare": [72.5, 13.0, np.nan, 8.05, 8.05, 15.5, 7.25, np.nan, 512.0, 26.0],
        "Sex": ["female", "male", "Female", "male", "male", "female", "MALE", "female", "female", "male"],
        "Embarked": ["S", "C", np.nan, "S", "S", "Q", "S", np.nan, "C", "Q"],
        "TicketDate": ["2024/01/03", "2024-01-05", "2024/01/07", "2024-01-09", "2024-01-09", "2024/01/12", "2024-01-15", "2024/01/18", "2024-01-20", "2024-01-22"],
    }
    return pd.DataFrame(data)


def task1_data_cleaning():
    print("=" * 80)
    print("任务1：数据清洗与预处理")

    raw_data = create_dirty_data()
    print("\n原始数据：")
    print(raw_data)

    print("\n1. 缺失值情况：")
    print(raw_data.isnull().sum())

    deleted_data = raw_data.dropna()
    print("\n2. 删除缺失值后的数据：")
    print(deleted_data)
    print("解释：dropna() 会直接删除包含缺失值的整行数据。")

    filled_data = raw_data.copy()
    filled_data["Age"] = filled_data["Age"].fillna(filled_data["Age"].median())
    filled_data["Fare"] = filled_data["Fare"].fillna(filled_data["Fare"].median())
    filled_data["Embarked"] = filled_data["Embarked"].fillna(filled_data["Embarked"].mode()[0])
    print("\n3. 填充缺失值后的数据：")
    print(filled_data)
    print("解释：这里对数值列用中位数填充，对分类列用众数填充。")

    interpolated_data = raw_data.copy()
    interpolated_data["Age"] = interpolated_data["Age"].interpolate(limit_direction="both")
    interpolated_data["Fare"] = interpolated_data["Fare"].interpolate(limit_direction="both")
    interpolated_data["Embarked"] = interpolated_data["Embarked"].fillna(interpolated_data["Embarked"].mode()[0])
    print("\n4. 插值后的数据：")
    print(interpolated_data)
    print("解释：插值适合处理数值型缺失值，可以根据前后数据估计空缺位置。")

    no_duplicates = raw_data.drop_duplicates()
    print("\n5. 去重后的数据：")
    print(no_duplicates)
    print("解释：drop_duplicates() 删除了完全重复的记录。")

    standardized_data = no_duplicates.copy()
    standardized_data["Age"] = pd.to_numeric(standardized_data["Age"], errors="coerce")
    standardized_data["Fare"] = pd.to_numeric(standardized_data["Fare"], errors="coerce")

    standardized_data.loc[(standardized_data["Age"] < 0) | (standardized_data["Age"] > 100), "Age"] = np.nan
    standardized_data.loc[standardized_data["Fare"] < 0, "Fare"] = np.nan

    standardized_data["Age"] = standardized_data["Age"].fillna(standardized_data["Age"].median())
    standardized_data["Fare"] = standardized_data["Fare"].fillna(standardized_data["Fare"].median())
    standardized_data["Sex"] = standardized_data["Sex"].str.lower()
    standardized_data["Embarked"] = standardized_data["Embarked"].fillna(standardized_data["Embarked"].mode()[0]).str.upper()
    standardized_data["TicketDate"] = pd.to_datetime(standardized_data["TicketDate"], format="mixed")

    print("\n6. 标准化后的数据：")
    print(standardized_data)
    print("解释：这一部分完成了异常值处理、数据类型转换和文本格式统一。")


def create_air_quality_data():
    np.random.seed(10)
    dates = pd.date_range("2024-01-01", periods=365, freq="D")
    day_index = np.arange(365)

    pm25 = 75 + 25 * np.sin(2 * np.pi * day_index / 365) + np.random.normal(0, 8, 365)
    pm10 = 110 + 30 * np.sin(2 * np.pi * day_index / 365 + 0.3) + np.random.normal(0, 10, 365)
    so2 = 18 + 5 * np.sin(2 * np.pi * day_index / 365 + 0.5) + np.random.normal(0, 2, 365)
    no2 = 42 + 10 * np.sin(2 * np.pi * day_index / 365 + 0.8) + np.random.normal(0, 4, 365)
    co = 1.2 + 0.25 * np.sin(2 * np.pi * day_index / 365 + 1.0) + np.random.normal(0, 0.08, 365)
    o3 = 95 + 20 * np.sin(2 * np.pi * day_index / 365 + 3.1) + np.random.normal(0, 7, 365)

    data = pd.DataFrame(
        {
            "date": dates,
            "PM2.5": np.clip(pm25, 5, None),
            "PM10": np.clip(pm10, 10, None),
            "SO2": np.clip(so2, 1, None),
            "NO2": np.clip(no2, 5, None),
            "CO": np.clip(co, 0.2, None),
            "O3": np.clip(o3, 20, None),
        }
    )

    season_map = {
        12: "冬季",
        1: "冬季",
        2: "冬季",
        3: "春季",
        4: "春季",
        5: "春季",
        6: "夏季",
        7: "夏季",
        8: "夏季",
        9: "秋季",
        10: "秋季",
        11: "秋季",
    }
    data["month"] = data["date"].dt.month
    data["season"] = data["month"].map(season_map)
    return data


def save_line_chart(data):
    plt.figure(figsize=(12, 5))
    plt.plot(data["date"], data["PM2.5"], label="PM2.5", color="blue")
    plt.plot(data["date"], data["PM10"], label="PM10", color="orange")
    plt.title("Air Quality Time Series")
    plt.xlabel("Date")
    plt.ylabel("Concentration")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "line_chart.png"))
    plt.close()


def save_bar_chart(stats_result):
    mean_values = stats_result.loc["mean"]
    plt.figure(figsize=(8, 5))
    plt.bar(mean_values.index, mean_values.values, color="skyblue")
    plt.title("Average Pollutant Concentration")
    plt.xlabel("Pollutant")
    plt.ylabel("Mean Value")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "bar_chart.png"))
    plt.close()


def save_scatter_chart(data):
    plt.figure(figsize=(6, 5))
    plt.scatter(data["PM2.5"], data["PM10"], alpha=0.7, color="green")
    plt.title("PM2.5 vs PM10")
    plt.xlabel("PM2.5")
    plt.ylabel("PM10")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "scatter_chart.png"))
    plt.close()


def save_heatmap(corr_result):
    plt.figure(figsize=(7, 6))
    plt.imshow(corr_result, cmap="coolwarm", interpolation="nearest")
    plt.colorbar()
    plt.xticks(range(len(corr_result.columns)), corr_result.columns, rotation=45)
    plt.yticks(range(len(corr_result.index)), corr_result.index)
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "heatmap.png"))
    plt.close()


def save_season_chart(season_result):
    pm25_by_season = season_result["PM2.5"]
    plt.figure(figsize=(7, 5))
    plt.bar(pm25_by_season.index, pm25_by_season.values, color="pink")
    plt.title("Seasonal PM2.5 Change")
    plt.xlabel("Season")
    plt.ylabel("PM2.5 Mean")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "season_chart.png"))
    plt.close()


def task2_air_quality():
    print("=" * 80)
    print("任务2：空气质量数据分析与可视化")

    air_data = create_air_quality_data()
    print("\n前 5 行空气质量数据：")
    print(air_data.head())

    print("\n1. 时间序列特征（按日期排序后前 10 条）：")
    print(air_data[["date", "PM2.5", "PM10", "O3"]].head(10))
    print("解释：可以看到空气质量数据具有明显的按日期连续变化特征。")

    pollutants = ["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]
    stats_result = air_data[pollutants].agg(["mean", "max", "min", "std"]).round(2)
    print("\n2. 不同污染物统计指标：")
    print(stats_result)
    print("解释：统计结果展示了各污染物的平均水平、极值和波动程度。")

    corr_result = air_data[pollutants].corr().round(2)
    print("\n3. 污染物相关系数矩阵：")
    print(corr_result)
    print("解释：相关系数越接近 1，表示两个污染物变化趋势越接近。")

    season_result = air_data.groupby("season")[pollutants].mean().round(2)
    print("\n4. 季节性变化规律：")
    print(season_result)
    print("解释：不同季节污染物均值不同，说明空气质量有明显季节性变化。")

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    save_line_chart(air_data)
    save_bar_chart(stats_result)
    save_scatter_chart(air_data)
    save_heatmap(corr_result)
    save_season_chart(season_result)

    print("\n5. 图表已保存到：", OUTPUT_DIR)
    print("包含：折线图、柱状图、散点图、热力图、季节性柱状图。")


def main():
    task1_data_cleaning()
    task2_air_quality()


if __name__ == "__main__":
    main()
