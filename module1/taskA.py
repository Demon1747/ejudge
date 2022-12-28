# Copyright 2022 Stepanov Dmitriy
# Task A module 1 -- sum

sum_var = 0
while True:
    try:
        in_str = input()
        str_num = ''
        for i in range(len(in_str)):
            if in_str[i].isdigit():
                str_num += in_str[i]
            elif in_str[i] == '-' and i < len(in_str) - 1:
                if str_num != "":
                    sum_var += int(str_num)
                    str_num = ''
                if in_str[i + 1].isdigit():
                    str_num += in_str[i]
            elif str_num != '':
                sum_var += int(str_num)
                str_num = ''
        if len(str_num) != 0:
            sum_var += int(str_num)
    except EOFError:
        print(sum_var)
        quit()
