import numpy as np
import matplotlib.pyplot as plt

a, b, c, d, e = -12, -18, 5, 10, -30
x_min = -10
x_max = 10
step = 0.01
x = np.arange(x_min, x_max, step)
list_roots = []
list_max = []
list_min = []
list_pos = []
list_neg = []
list_asc = []
list_desc = []

def func(x):
    function = a*x**4*np.sin(np.cos(x)) + b*x**3 + c*x**2 + d*x + e
    return function

def extrem(x, list_min, list_max):
    for i in x:
        if func(i - 0.01) < func(i) > func(i + 0.01):
            list_max.append(round(i,4))
        elif func(i - 0.01) > func(i) < func(i + 0.01):
            list_min.append(round(i,2))

def roots(x, list_roots):
    for i in x:
        if (func(i) > 0 and func(i-0.01) < 0) or (func(i) < 0 and func(i-0.01) > 0) or func(i) == 0:
            list_roots.append(round(i, 2))

def find_top(x):
    top_point = [round(x[0], 3), round(func(x[0]), 3)]
    for i in x:
        if func(i) > top_point[1]:
            top_point[0] = round(i, 3)
            top_point[1] = round(func(i), 3)
    return top_point

def list_func_value(list):
    list_func = []
    for i in list:
        list_func.append(round(func(i), 2))
    return list_func

def find_range_posneg(x, list_pos, list_neg):
    x_start = x[0] 
    for i in x:
        if func (i) < 0 and func(i - 0.01) >= 0:
            x_end = i
            list_pos.append((round(x_start, 3), round(x_end, 3)))
            x_start = x_end
        elif func (i) >= 0 and func(i - 0.01) < 0:
            x_end = i
            list_neg.append((round(x_start, 3), round(x_end, 3)))
            x_start = x_end

def find_range_ascdesc(x, list_asc, list_desc):
    x_start = x[0]
    for i in x:
        if func(i - 0.01) < func(i) > func(i + 0.01):
            x_end = i
            list_asc.append((round(x_start, 3), round(x_end, 3)))
            x_start = x_end
        elif func(i - 0.01) > func(i) < func(i + 0.01):
            x_end = i
            list_desc.append((round(x_start, 3), round(x_end, 3)))
            x_start = x_end

def draw_func_main(x):
    x_start = x[0]
    asc_switch = 1
    if func(x_start) > func(x_start + 0.01):
        asc_switch = 0
    pos_switch = 1
    if func(x_start) < 0:
        pos_switch = 0 
    for i in x:
        if func(i - 0.01) < func(i) > func(i + 0.01):
            if pos_switch == 1:
                x_end = i
                x_temp = np.arange(x_start, x_end, 0.01)
                plt.plot(x_temp, func(x_temp), 'g')
                x_start = x_end
            else:
                x_end = i
                x_temp = np.arange(x_start, x_end, 0.01)
                plt.plot(x_temp, func(x_temp), '--g')
                x_start = x_end
            asc_switch = 0
        elif func (i) < 0 and func(i - 0.01) >= 0:
            if asc_switch == 1:
                x_end = i
                x_temp = np.arange(x_start, x_end, 0.01)
                plt.plot(x_temp, func(x_temp), 'g')
                x_start = x_end
            else:
                x_end = i
                x_temp = np.arange(x_start, x_end, 0.01)
                plt.plot(x_temp, func(x_temp), 'r')
                x_start = x_end
            pos_switch = 0
        elif func(i - 0.01) > func(i) < func(i + 0.01):
            if pos_switch == 1:
                x_end = i
                x_temp = np.arange(x_start, x_end, 0.01)
                plt.plot(x_temp, func(x_temp), 'r')
                x_start = x_end
            else:
                x_end = i
                x_temp = np.arange(x_start, x_end, 0.01)
                plt.plot(x_temp, func(x_temp), '--r')
                x_start = x_end
            asc_switch = 1
        elif func (i) >= 0 and func(i - 0.01) < 0:
            if asc_switch == 1:
                x_end = i
                x_temp = np.arange(x_start, x_end, 0.01)
                plt.plot(x_temp, func(x_temp), '--g')
                x_start = x_end
            else:
                x_end = i
                x_temp = np.arange(x_start, x_end, 0.01)
                plt.plot(x_temp, func(x_temp), '--r')
                x_start = x_end
            pos_switch = 1

def draw_func(x):
    roots(x, list_roots)
    extrem(x, list_min, list_max)
    find_range_posneg(x, list_pos, list_neg)
    find_range_ascdesc(x, list_asc, list_desc)
    list_max_func = list_func_value(list_max)
    list_min_func = list_func_value(list_min)
    title_roots = f'* {len(list_roots)} корней функции на промежутке от {x_min} до {x_max}:  {", ".join(map(str, list_roots))}\n'
    title_max = f'* {len(list_max)} максимумов функции на промежутке от {x_min} до {x_max}:  {", ".join(map(str, list_max))}\n'
    title_min = f'* {len(list_min)} минимумов функции на промежутке от {x_min} до {x_max}:  {", ".join(map(str, list_min))}\n'
    title_top = f'* Вершина функции на промежутке от {x_min} до {x_max}:  {find_top(x)}\n'
    title_pos = f'* Функция отрицательна на промежутках:  {", ".join(map(str, list_pos))}\n'
    title_neg = f'* Функция положительна на промежутках:  {", ".join(map(str, list_neg))}\n'
    title_asc = f'* Функция возрастает на промежутках:  {", ".join(map(str, list_asc))}\n'
    title_desc = f'* Функция убывает на промежутках:  {", ".join(map(str, list_desc))}\n'
    f = plt.figure()
    f.set_figwidth(30)
    f.set_figheight(15)
    plt.title(title_roots + title_min + title_max + title_top + title_pos + title_neg + title_asc + title_desc, fontsize=10, loc='left')
    plt.xlabel('Ось X')
    plt.ylabel('Ось Y')
    plt.grid()
    draw_func_main(x)
    plt.plot(0, 0, '--k', label='отрицательные значения')
    plt.plot(0, 0, 'k', label='положительные значения')
    plt.plot(0, 0, 'g', label='функция возрастает')
    plt.plot(0, 0, 'r', label='функция убывает')
    plt.plot(find_top(x)[0], find_top(x)[1], 'om', label='вершина')
    plt.plot(list_roots, list_roots, 'xb', label='корни')
    plt.plot(list_max, list_max_func, '^g', label='максимумы')
    plt.plot(list_min, list_min_func, 'vr', label='минимумы')
    plt.legend()
    plt.show()

draw_func(x)