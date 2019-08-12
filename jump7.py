for index in range(1, 101):
    if (index % 7 != 0) and (index %10 != 7) and (index // 10 == 7):
        print(index)
