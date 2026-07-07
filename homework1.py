"""这个是作业1 ：简单的学生管理系统"""
def parse_scores(raw_text):
    scores = {}
    items = [item.strip() for item in raw_text.split(",") if item.strip()]
    if not items:
        raise ValueError("至少输入一门课程。")
    for item in items:
        if ":" not in item:
            raise ValueError("格式应为 课程:分数")
        subject, score_text = [part.strip() for part in item.split(":", 1)]
        if not subject:
            raise ValueError("课程名称不能为空。")
        score = float(score_text)
        if score < 0 or score > 100:
            raise ValueError("成绩必须在0到100之间。")
        scores[subject] = score
    return scores


def add_student(students):
    student_id = input("请输入学号：").strip()
    if not student_id:
        print("学号不能为空。")
        return
    name = input("请输入姓名：").strip()
    if not name:
        print("姓名不能为空。")
        return

    print("请输入各科成绩，如这：数学:95,英语:88,Python:99")
    raw_scores = input("成绩：").strip()
    try:
        scores = parse_scores(raw_scores)
    except ValueError as exc:
        print(f"录入失败：{exc}")
        return

    students[student_id] = {"name": name, "scores": scores}
    print("学生信息已保存。")


def query_student(students):
    student_id = input("请输入要查询的学号：").strip()
    student = students.get(student_id)
    if not student:
        print("未找到该学生。")
        return
    print(f"姓名：{student['name']}")
    print(f"学号：{student_id}")
    scores = student["scores"]
    for subject, score in scores.items():
        print(f"{subject}：{score}")
    values = list(scores.values())
    print(f"平均分：{sum(values) / len(values):.2f}")
    print(f"最高分：{max(values):.2f}")
    print(f"最低分：{min(values):.2f}")


def statistics(students):
    if not students:
        print("当前没有学生数据。")
        return
    all_scores = []
    for student in students.values():
        all_scores.extend(student["scores"].values())
    if not all_scores:
        print("没有可统计的成绩。")
        return
    print("全体成绩统计结果：")
    print(f"平均分：{sum(all_scores) / len(all_scores):.2f}")
    print(f"最高分：{max(all_scores):.2f}")
    print(f"最低分：{min(all_scores):.2f}")


def list_students(students):
    if not students:
        print("当前没有学生数据。")
        return
    print("\n所有学生信息：")
    for student_id, student in students.items():
        subjects = ", ".join(
            f"{subject}:{score}" for subject, score in student["scores"].items()
        )
        print(f"学号：{student_id} | 姓名：{student['name']} | 成绩：{subjects}")


def show_menu():
    print("\n==== 学生成绩管理系统 ====")
    print("1. 录入/修改学生成绩")
    print("2. 查询学生成绩")
    print("3. 统计全体成绩")
    print("4. 显示所有学生")
    print("5. 退出系统")


def main():
    students = {}
    while True:
        show_menu()
        choice = input("请选择功能（1-5）：").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            query_student(students)
        elif choice == "3":
            statistics(students)
        elif choice == "4":
            list_students(students)
        elif choice == "5":
            print("系统已退出。")
            break
        else:
            print("输入无效，请重新选择。")


if __name__ == "__main__":
    main()
