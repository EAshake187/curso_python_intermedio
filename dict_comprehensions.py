from math import sqrt


def run():
    # cubes = {}
    # for i in range(1,101):
    #     if i % 3 != 0:
    #         cubes[i]=i**3
    # print(cubes)

    # cubes = {i: i**3 for i in range(1,101) if i % 3 != 0}
    # print(cubes)

    dict = {i:sqrt(i) for i in range(1,100)}
    print(dict)


if __name__ == '__main__':
    run()