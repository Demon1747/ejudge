# Copyright 2022 Stepanov Dmitriy

head = 0          # the index of the beginning of the queue
tail = 0          # the index of the position after the last deque element
is_init = False   # init flag

# deque initialisation
while not is_init:
    try:
        in_str = input().split()
        if not len(in_str):
            continue
        if len(in_str) != 2 or in_str[0] != "set_size" or not in_str[1].isdigit():
            print("error")
        else:
            deq = [0 for _ in range(int(in_str[1]))]
            is_init = True
    except EOFError:
        break

# executing commands
while is_init:
    try:
        in_str = input().split()
        
        if not len(in_str):
            continue
        
        if len(in_str) == 2 and in_str[0] == "pushb" and in_str[1].isdigit():
            if head == (tail + 1) % len(deq):
                print("overflow")
            else:
                deq[tail] = int(in_str[1])
                tail = (tail + 1) % len(deq)
                
        if len(in_str) == 2 and in_str[0] == "pushf" and in_str[1].isdigit():
            if head == (tail + 1) % len(deq):
                print("overflow")
                print((tail + 1) % len(deq))
            else:
                head = (head - 1) % len(deq)
                deq[head] = int(in_str[1])
            
    except EOFError:
        break
        
print(*deq)
