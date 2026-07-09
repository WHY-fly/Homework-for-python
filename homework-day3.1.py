import numpy as np
names = []
scores = []
while True:
    print("\n==== 成绩分析系统 ====")
    print("1. 输入成绩数据\n2. 查看成绩统计\n3. 查看成绩排名\n4. 查看成绩分布\n5. 查询学生成绩\n6. 退出系统")
    choice = input("请选择：")
    if choice == '1':
        num = int(input("请输入学生人数："))
        for i in range(num):
            name = input(f"请输入第{i+1}个学生姓名：")
            score = float(input("请输入成绩："))
            names.append(name)
            scores.append(score)
    elif choice == '2':
        if not scores:
            print("暂无数据，请先输入成绩！")
            continue
        arr = np.array(scores)
        print(f"平均分: {np.mean(arr):.2f}, 最高分: {np.max(arr)}, 最低分: {np.min(arr)}")
    elif choice == '3':
        if not scores: continue
        arr = np.array(scores)
        sort_idx = np.argsort(-arr) # 使用负号实现降序排列
        print("成绩排名：")
        for rank, idx in enumerate(sort_idx):
            print(f"第{rank+1}名: {names[idx]} - {scores[idx]}")
    elif choice == '4':
        if not scores: continue
        arr = np.array(scores)
        print(f"优秀(>=90): {np.sum(arr >= 90)}人")
        print(f"良好(80-89): {np.sum((arr >= 80) & (arr < 90))}人")
        print(f"中等(70-79): {np.sum((arr >= 70) & (arr < 80))}人")
        print(f"及格(60-69): {np.sum((arr >= 60) & (arr < 70))}人")
        print(f"不及格(<60): {np.sum(arr < 60)}人")
    elif choice == '5':
        query = input("请输入要查询的学生姓名：")
        if query in names:
            idx = names.index(query)
            print(f"{query} 的成绩是: {scores[idx]}")
        else:
            print("未找到该学生！")
    elif choice == '6':
        print("退出系统。")
        break
    else:
        print("输入无效，请重新选择。")