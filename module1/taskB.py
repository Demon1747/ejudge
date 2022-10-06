# Copyright 2022 Stepanov Dmitriy

# printing deque
def print_deq(arr, h, t):
    if t == h:
        print("empty")
        return
    i = h
    while True:
        if (i + 1) % len(arr) == t:
            print(arr[i])
            return
        else:
            print(arr[i], end=' ')
        if i + 1 == len(arr):
            i = 0
        else:
            i += 1



# "main" function
head = 0          # the index of the beginning of the queue
tail = 0          # the index of the position after the last deque element
is_init = False   # init flag

# deque initialisation
while not is_init:
    try:
        input_text = input()
        in_str = input_text.split(' ')
        if not len(input_text):
            continue
        if len(in_str) != 2 or in_str[0] != "set_size" or not in_str[1].isdigit():
            print("error")
        else:
            deq = ['' for _ in range(int(in_str[1]) + 1)]       # the size of the array must be 1 larger than the queue size
            is_init = True
    except EOFError:
        break

# executing commands
while is_init:
    try:
        input_text = input()
        in_str = input_text.split(' ')


        # empty input check
        if not len(input_text):
            continue

        # push_back
        if len(in_str) == 2 and in_str[0] == "pushb":
            if head == (tail + 1) % len(deq):
                print("overflow")
            else:
                deq[tail] = in_str[1]
                tail = (tail + 1) % len(deq)

        # push_front
        elif len(in_str) == 2 and in_str[0] == "pushf":
            if head == (tail + 1) % len(deq):
                print("overflow")
            else:
                head = (head - 1) % len(deq)
                deq[head] = in_str[1]

        # pop_back
        elif in_str == ["popb"]:
            if head == tail:
                print("underflow")
            else:
                print(deq[tail - 1])
                tail = (tail - 1) % len(deq)

        # pop_front
        elif in_str == ["popf"]:
            if head == tail:
                print("underflow")
            else:
                print(deq[head])
                head = (head + 1) % len(deq)

        # print
        elif in_str == ["print"]:
            print_deq(deq, head, tail)

        # by all means
        else:
            print("error")

    except EOFError:
        break
