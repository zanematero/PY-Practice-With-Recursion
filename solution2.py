# Write code for algorithm 2 below
def count_up(num, max):
    if num > max:
        return
    print(num)    
    count_up(num+1, max)

count_up(1, 10)