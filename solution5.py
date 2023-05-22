# Write code for algorithm 5 below
def palindrome(str):
    if len(str) < 2:
        return True
    else:
        if str[0] == str[-1]:
            return palindrome(str[1:-1])
        else: return False

print(palindrome("racecar"))
print(palindrome("football"))