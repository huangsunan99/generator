def iter_grid_ids(fpath):
    with open(fpath) as fil:
        for line in fil.readlines():
            if line.strip().__contains__('GRID' or 'GRIDS*'):
                lis = line.strip().split()
                yield lis[1]


if __name__ == '__main__':
    bdf = '/home/huangsunan/testmodel/generator-test-model/all_elems.bdf'
    for grid_id in iter_grid_ids(bdf):
        print grid_id
