# Copyright 2022 Stepanov Dmitriy

def inputs():
    result = []
    while True:
        try:
            in_str = input()
            str_num = ''
            for i in range(len(in_str)):
                if in_str[i].isdigit():
                    str_num += in_str[i]
                elif in_str[i] == '-' and i < len(in_str) - 1:
                    if len(str_num) != 0:
                        result.append(int(str_num))
                        str_num = ''
                    if in_str[i + 1].isdigit():
                        str_num += in_str[i]
                elif str_num != '':
                    result.append(int(str_num))
                    str_num = ''
            if len(str_num) != 0:
                result.append(int(str_num))
        except EOFError:
            return result

data = [int(i) for i in inputs()]
print(sum(data))
