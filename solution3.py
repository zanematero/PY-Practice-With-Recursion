# Write code for algorithm 3 below
def fib_seq(num):
    if num <= 0:
        print("Invalid")
    elif num==1:
        return 0
    elif num==2:
        return 1
    else:
        return fib_seq(num-1)+fib_seq(num-2)

print(fib_seq(17))