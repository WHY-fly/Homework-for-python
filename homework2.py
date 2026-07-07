"""这个是作业2：数学计算器"""
import math
from pathlib import Path
HISTORY_FILE = Path(__file__).with_name("calculator_history.txt")


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("除数不能为 0。")
    return a / b


def power(a, b):
    return a**b


def square_root(a):
    if a < 0:
        raise ValueError("负数不能开平方。")
    return math.sqrt(a)


def save_history(record):
    with HISTORY_FILE.open("a", encoding="utf-8") as file:
        file.write(record + "\n")


def read_history():
    if not HISTORY_FILE.exists():
        print("没有历史记录。")
        return
    print("\n==== 计算历史 ====")
    with HISTORY_FILE.open("r", encoding="utf-8") as file:
        content = file.read().strip()
        print(content if content else "没有历史记录。")


def get_number(prompt):
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("输入错误，请输入数字")


def menu():
    print("\n==== 数学计算器 ====")
    print("1.加法")
    print("2.减法")
    print("3.乘法")
    print("4.除法")
    print("5.幂运算")
    print("6.开方")
    print("7.查看历史记录")
    print("8.退出程序")


def calculate_once(choice):
    try:
        if choice in {"1", "2", "3", "4", "5"}:
            a = get_number("请输入第一个数：")
            b = get_number("请输入第二个数：")

            if choice == "1":
                result = add(a, b)
                expression = f"{a} + {b} = {result}"
            elif choice == "2":
                result = subtract(a, b)
                expression = f"{a} - {b} = {result}"
            elif choice == "3":
                result = multiply(a, b)
                expression = f"{a} * {b} = {result}"
            elif choice == "4":
                result = divide(a, b)
                expression = f"{a} / {b} = {result}"
            else:
                result = power(a, b)
                expression = f"{a} ^ {b} = {result}"
            print(f"结果：{result}")
            save_history(expression)
        elif choice == "6":
            a = get_number("请输入要开方的数字：")
            result = square_root(a)
            expression = f"sqrt({a}) = {result}"
            print(f"结果：{result}")
            save_history(expression)
        elif choice == "7":
            read_history()
        elif choice == "8":
            print("程序已退出。")
        else:
            print("输入无效，请重新选择。")
    except (ZeroDivisionError, ValueError) as exc:
        print(f"计算失败：{exc}")


def main():
    while True:
        menu()
        choice = input("请选择功能（1-8）：").strip()
        if choice == "8":
            calculate_once(choice)
            break
        calculate_once(choice)


if __name__ == "__main__":
    main()
