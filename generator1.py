def iter_grid_ids(fpath):
    with open(fpath) as fil:
        line = True
        while line:
            line = fil.readline()
            lis = line.strip().split()
            if len(lis) != 0 and lis[0] == 'GRID*':
                yield lis[1]
            elif len(lis) != 0 and lis[0] == 'GRID':
                yield lis[1]


if __name__ == '__main__':
    bdf = '/home/huangsunan/testmodel/generator-test-model/yoke.bdf'
    for grid_id in iter_grid_ids(bdf):
        print grid_id
