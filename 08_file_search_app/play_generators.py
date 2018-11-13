# Fibonatchi series
# 1,1,2,3,5,8,13,....


def fib(n):
    current_num = 0
    next_num = 1
    # fib_list = []
    while current_num < n:
        current_num, next_num = next_num, next_num + current_num
        yield  current_num
        # fib_list.append(current_num)
        # print(current_num,end=',')

    # return fib_list

print(type(fib(10)))

for n in fib(100):
    print(n,end=', ')