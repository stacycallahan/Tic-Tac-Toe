def print_grid(positions):
    for i in range(0, 3):
        for j in range(0, 3):
            print(f'[{positions[(i + 1, j + 1)]}]', sep = '', end ='')
        print('\n', sep = '', end = '')