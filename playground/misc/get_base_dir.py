from os.path import abspath, dirname
import sys


def base_dir_by_x(no_of_layer: int = 0, file_abspath: str = __file__):
    cur_dirname = dirname(abspath(file_abspath))
    if no_of_layer <= 0:
        return cur_dirname
    for _ in range(no_of_layer):
        cur_dirname = dirname(cur_dirname)
    return cur_dirname


def insert_dir_2_syspath_by_x(no_of_layer: int = 0, file_abspath: str = __file__):
    base_dir = base_dir_by_x(no_of_layer, file_abspath)
    sys.path.insert(0, base_dir)
    return base_dir


if __name__ == "__main__":
    res = base_dir_by_x(1, __file__)
    print(res)
