def main():
    # squares = []
    # for x in range(1,101):
    #     if x % 3 != 0: 
    #         squares.append(x**2)
    squares = [x for x in range(1,1000) if x % 36 == 0]
    print(squares)


if __name__ == '__main__':
    main()