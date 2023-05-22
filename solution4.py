# Write code for algorithm 4 below
def power_of(num, exp):
    if exp == 1:
        return num
    elif exp == 0:
        return 1
    else:
        return num * power_of(num, exp-1)

print(power_of(6, 3))