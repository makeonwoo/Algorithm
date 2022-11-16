def solution(sizes):
    x_max = 0
    y_max = 0
    for i in sizes:
        i.sort()
        if i[0]>x_max:
            x_max = i[0]
        if i[1]>y_max:
            y_max = i[1]

    return x_max * y_max