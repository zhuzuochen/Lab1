import time

RED = "\033[48;5;1m"
WHITE = "\033[48;5;255m"
BLUE = "\033[48;5;21m"
RESET = "\033[0m"

flag_red_white_rows = 3
flag_blue_rows = 6
flag_width = 60

for _ in range(flag_red_white_rows):
    print(f"{RED}{' ' * flag_width}{RESET}")
    time.sleep(0.3)

for _ in range(flag_red_white_rows):
    print(f"{WHITE}{' ' * flag_width}{RESET}")
    time.sleep(0.3)

for _ in range(flag_blue_rows):
    print(f"{BLUE}{' ' * flag_width}{RESET}")
    time.sleep(0.3)

for _ in range(flag_red_white_rows):
    print(f"{WHITE}{' ' * flag_width}{RESET}")
    time.sleep(0.3)

for _ in range(flag_red_white_rows):
    print(f"{RED}{' ' * flag_width}{RESET}")
    time.sleep(0.3)
данные = {"больше_пяти": 0, "меньше_пяти": 0, "ноль": 0}  # 调整统计类别
with open(r"C:\Users\asus\Pictures\Screenshots\se.7", 'r', encoding='utf-8') as файл:
    for строка in файл:
        число = float(строка.strip())
        if число < 0:  # 排除负数，不统计
            continue
        elif число > 5:  # 统计大于5的数
            данные["больше_пяти"] += 1
        elif число == 0:  # 单独统计0（属于小于5的非负数，可保留独立分类）
            данные["ноль"] += 1
        else:  # 统计0 < число ≤5 的数
            данные["меньше_пяти"] += 1

общая_сумма = sum(данные.values())
if общая_сумма == 0:  # 处理无有效数据的情况
    print("Нет неотрицательных данных для анализа")
else:
    проценты = {категория: (значение / общая_сумма) * 100 for категория, значение in данные.items()}

    высота_диаграммы = 10

    # 绘制柱状图
    for i in range(высота_диаграммы, 0, -1):
        строка = ""
        for категория in ["больше_пяти", "меньше_пяти", "ноль"]:
            процент = проценты[категория]
            if (процент / 100) * высота_диаграммы >= i:
                строка += "█ "
            else:
                строка += "  "
        print(строка)

    # 显示标签和百分比（对应新类别）
    строка_меток = "больше 5    меньше 5    ноль      "  # 调整标签对齐
    строка_процентов = (f"{проценты['больше_пяти']:.1f}% "
                       f"{проценты['меньше_пяти']:.1f}% "
                       f"{проценты['ноль']:.1f}% ")
    print(строка_меток)
    print(строка_процентов)
    plot_list = [[0 for i in range(11)] for i in range(10)]
result = [0 for i in range(11)]

for i in range(11):
    if i == 0:
        result[i] = float('inf')
    else:
        result[i] = 1 / i

finite_results = [result[i] for i in range(1, 11)]
max_val = max(finite_results)
min_val = min(finite_results)
step = round((max_val - min_val) / 8, 2)
print(f"Step: {step}")

for i in range(10):
    for j in range(11):
        if j == 0:
            plot_list[i][j] = round(max_val - step * i, 2)

for i in range(10):
    for j in range(1, 11):
        if abs(plot_list[i][0] - result[j]) < step/2:
            plot_list[i][j] = 1

print("Y = 1/X Graph:")
for i in range(10):
    line = ''
    for j in range(11):
        if j == 0:
            line += '\t' + str(round(plot_list[i][j], 2)) + '\t'
        elif plot_list[i][j] == 0:
            line += '--'
        elif plot_list[i][j] == 1:
            line += '**'
    print(line)
print('\t0.00\t 0 1 2 3 4 5 6 7 8 9 10')

print("\nFunction values:")
print("X\tY")
for i in range(11):
    if i == 0:
        print(f"{i}\tundefined")
    else:
        print(f"{i}\t{result[i]:.3f}")