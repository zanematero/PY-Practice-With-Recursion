# Write code for algorithm 1 below
def count_down(num):
    print(num)
    if num == 0:
        return
    count_down(num-1)

count_down(10)
