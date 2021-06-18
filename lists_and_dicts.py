def run():
    my_list = [1, 'hello', True, 4.5]
    my_dict = {'firstname':'Edgar','lastname':'Abreu'}

    super_list = [{'firstname':'Edgar','lastname':'Abreu'},{'firstname':'Miguel','lastname':'Torres'},{'firstname':'Omar','lastname':'Garcia'},{'firstname':'Laura','lastname':'Gonzalez'}]

    super_dict = {'natural_num':[1,2,3,4,5],'integer_nums':[-1,-2,0,1,2],'floating_nums':[1.1,4.5,6.43]}

    for key, value in super_dict.items():
        print(key, '-', value)

    for list in super_list:
        for key, value in list.items():
            print(value, end=' ')
        print(end='\n')


if __name__ == '__main__':
    run()