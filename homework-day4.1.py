#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd


pd.set_option("display.max_columns", None)
pd.set_option("display.float_format", lambda x: f"{x:.2f}")


orders = pd.DataFrame(
    {
        "order_id": [f"O{number}" for number in range(1001, 1019)],
        "region": [
            "华东",
            "华北",
            "华南",
            "华东",
            "西南",
            "华北",
            "华南",
            "华东",
            "西南",
            "华北",
            "华东",
            "华南",
            "西南",
            "华东",
            "华北",
            "华南",
            "华东",
            "西南",
        ],
        "product": [
            "机械键盘",
            "无线鼠标",
            "显示器",
            "扩展坞",
            "机械键盘",
            "显示器",
            "无线鼠标",
            "显示器",
            "扩展坞",
            "机械键盘",
            "无线鼠标",
            "扩展坞",
            "显示器",
            "机械键盘",
            "扩展坞",
            "显示器",
            "无线鼠标",
            "机械键盘",
        ],
        "category": [
            "外设",
            "外设",
            "显示设备",
            "配件",
            "外设",
            "显示设备",
            "外设",
            "显示设备",
            "配件",
            "外设",
            "外设",
            "配件",
            "显示设备",
            "外设",
            "配件",
            "显示设备",
            "外设",
            "外设",
        ],
        "quantity": [2, 3, 1, 4, 5, 2, 6, 1, 3, 2, 8, 2, 1, 3, 5, 2, 4, 6],
        "unit_price": [289, 129, 1299, 399, 289, 1299, 129, 1299, 399, 289, 129, 399, 1299, 289, 399, 1299, 129, 289],
        "member_level": [
            "金卡",
            "普通",
            "银卡",
            "金卡",
            "银卡",
            "普通",
            "金卡",
            "银卡",
            "普通",
            "金卡",
            "银卡",
            "金卡",
            "普通",
            "银卡",
            "金卡",
            "金卡",
            "普通",
            "银卡",
        ],
        "coupon_rate": [0.05, 0.00, 0.08, 0.10, 0.05, 0.00, 0.12, 0.05, 0.00, 0.08, 0.10, 0.05, 0.00, 0.12, 0.05, 0.08, 0.00, 0.10],
        "salesperson": [
            "小林",
            "小周",
            "小陈",
            "小林",
            "小赵",
            "小周",
            "小陈",
            "小林",
            "小赵",
            "小周",
            "小林",
            "小陈",
            "小赵",
            "小林",
            "小周",
            "小陈",
            "小林",
            "小赵",
        ],
    }
)


def line():
    print("\n" + "=" * 80)


def explain(text):
    print("结果解释：", text)


def add_order_level(df):
    return df.assign(
        order_level=np.where(
            df["final_amount"] >= 2000,
            "战略订单",
            np.where(df["final_amount"] >= 1000, "重点订单", "普通订单"),
        )
    )


line()
print("任务1：快速理解数据")
print("\n1) 数据的行数、列数和所有列名")
print("行数：", orders.shape[0])
print("列数：", orders.shape[1])
print("列名：", list(orders.columns))
explain("原始订单表共有 18 行 9 列，包含订单、地区、商品、会员等级和销售人员等完整字段。")

print("\n2) 取出单列和多列，并打印类型")
region_series = orders["region"]
subset_df = orders[["order_id", "product", "quantity"]]
print("region 单列：")
print(region_series.head())
print("region 的类型：", type(region_series))
print("\norder_id、product、quantity 三列：")
print(subset_df.head())
print("三列结果的类型：", type(subset_df))
explain("单列选择返回 Series，多列选择返回 DataFrame。")

print("\n3) 使用 iloc 取第 4 到第 8 行、前 4 列")
iloc_result = orders.iloc[3:8, 0:4]
print(iloc_result)
explain("iloc 按位置切片，成功取出了第 4 到第 8 行的前 4 列数据。")

print("\n4) 使用 loc 找出华东订单，仅显示指定列")
loc_result = orders.loc[orders["region"] == "华东", ["order_id", "product", "member_level"]]
print(loc_result)
explain("loc 按标签和条件筛选，华东地区订单被完整提取出来。")

print("\n5) 为什么长期维护通常更推荐 loc")
print("答：loc 基于列名和行标签，代码语义更清晰；即使列顺序发生变化，筛选逻辑仍然稳定，可读性和可维护性更强。")
explain("长期业务代码更重视可读性和稳定性，因此通常优先使用 loc。")


analysis = (
    orders.assign(
        gross_amount=orders["quantity"] * orders["unit_price"],
        member_discount=np.where(
            orders["member_level"] == "金卡",
            0.10,
            np.where(orders["member_level"] == "银卡", 0.05, 0.00),
        ),
    )
    .assign(
        payable_amount=lambda df: df["gross_amount"] * (1 - df["member_discount"]) * (1 - df["coupon_rate"]),
    )
    .assign(
        shipping_fee=lambda df: np.where(df["payable_amount"] >= 1000, 0, 20),
    )
    .assign(
        final_amount=lambda df: df["payable_amount"] + df["shipping_fee"],
    )
)

money_columns = ["gross_amount", "payable_amount", "shipping_fee", "final_amount"]
analysis[money_columns] = analysis[money_columns].round(2)


line()
print("任务2：构造订单结算指标")
print(
    analysis[
        [
            "order_id",
            "member_level",
            "quantity",
            "unit_price",
            "gross_amount",
            "member_discount",
            "coupon_rate",
            "payable_amount",
            "shipping_fee",
            "final_amount",
        ]
    ].head(8)
)
explain("新表 analysis 完整计算了订单总额、会员折扣、优惠券折扣、运费和最终实付金额。")


line()
print("任务3：复杂条件筛选")
condition_region = analysis["region"].isin(["华东", "华南"])
condition_amount = analysis["final_amount"] >= 700
condition_member_or_quantity = (analysis["quantity"] >= 2) | (analysis["member_level"] == "金卡")
mask = condition_region & condition_amount & condition_member_or_quantity

key_orders = (
    analysis.loc[
        mask,
        ["order_id", "region", "product", "quantity", "member_level", "final_amount"],
    ]
    .sort_values("final_amount", ascending=False)
)
print(key_orders)
print("\n括号说明：因为 & 和 | 是按位运算符，优先级与比较运算不同，如果不加括号，多个条件容易被错误组合。")
explain("重点跟进订单同时满足地区、金额和会员/数量组合条件，并按最终金额从高到低排序。")


line()
print("任务4：封装可复用处理函数")
leveled_orders = analysis.pipe(add_order_level)
order_level_counts = leveled_orders["order_level"].value_counts()
print(order_level_counts)
explain("通过 pipe 调用函数后，订单被分成战略订单、重点订单和普通订单三类。")


line()
print("任务5：一条链完成经营汇总")
region_report = (
    analysis.pipe(add_order_level)
    .query("final_amount >= 500")
    .groupby(["region", "order_level"], as_index=False)
    .agg(
        order_count=("order_id", "count"),
        quantity_sum=("quantity", "sum"),
        revenue_sum=("final_amount", "sum"),
        revenue_mean=("final_amount", "mean"),
    )
    .assign(
        revenue_sum=lambda df: df["revenue_sum"].round(2),
        revenue_mean=lambda df: df["revenue_mean"].round(2),
    )
    .sort_values("revenue_sum", ascending=False)
)
print(region_report)
explain("一条方法链完成了订单等级补充、金额筛选、分组统计和经营汇总排序。")


line()
print("任务6：经营诊断与表达")
salesperson_revenue = analysis.groupby("salesperson", as_index=False)["final_amount"].sum().rename(
    columns={"final_amount": "total_revenue"}
)
best_salesperson_row = salesperson_revenue.sort_values("total_revenue", ascending=False).iloc[0]
best_salesperson = best_salesperson_row["salesperson"]
best_salesperson_total = round(best_salesperson_row["total_revenue"], 2)

best_region_revenue = (
    analysis.loc[analysis["salesperson"] == best_salesperson]
    .groupby("region", as_index=False)["final_amount"]
    .sum()
    .rename(columns={"final_amount": "region_revenue"})
    .sort_values("region_revenue", ascending=False)
)

core_region_row = best_region_revenue.iloc[0]
core_region = core_region_row["region"]
core_region_revenue = round(core_region_row["region_revenue"], 2)
contribution_rate = round(core_region_revenue / best_salesperson_total, 4)

diagnosis = pd.DataFrame(
    {
        "salesperson": [best_salesperson],
        "core_region": [core_region],
        "total_revenue": [best_salesperson_total],
        "core_region_revenue": [core_region_revenue],
        "contribution_rate": [contribution_rate],
    }
)
print(diagnosis)
print(
    "\n业务结论：{0} 的最终成交金额最高，其中 {1} 是其最核心的成交地区，该地区贡献了其总成交金额的 {2:.2%}。".format(
        best_salesperson,
        core_region,
        contribution_rate,
    )
)
explain("先找出总成交额最高的销售人员，再定位其贡献最大的地区，并计算该地区对个人总业绩的贡献率。")
