def get_next_id_hop(min_num: int, max_num: int, arr):
    if min_num >= max_num:
        raise Exception("max_num must > min_num")

    arr_set = set(arr)  # set is O(1)
    for num in range(min_num, max_num + 1):
        if num in arr_set:
            continue
        else:
            return num
    raise Exception("No available ID")


if __name__ == "__main__":
    aaa = [10000, 10001, 10002, 10005, 10003]
    next_hop = get_next_id_hop(10000, 19990, aaa)
    print(next_hop)
