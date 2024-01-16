mylist = ["Yang", "Zhou", "is", "writing"]


# Using '+'
def concat_plus():
    result = ""
    for word in mylist:
        result += word + " "
    return result


# Using 'join()'
def concat_join():
    return " ".join(mylist)


# Directly concatenation without the list
def concat_directly():
    return "Yang" + "Zhou" + "is" + "writing"


if __name__ == "__main__":
    import timeit

    print(timeit.timeit(concat_plus, number=10000))
    # 0.002738415962085128
    print(timeit.timeit(concat_join, number=10000))
    # 0.0008482920238748193
    print(timeit.timeit(concat_directly, number=10000))
    # 0.00021425005979835987
