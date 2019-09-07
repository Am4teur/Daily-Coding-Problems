def two_sum(lst, k):
    needed = set()
    for num in lst:
        if(num in needed):
            return True
        needed.add(k - num)
    return False


print(two_sum([4,7,1,-3,2], 3))
# True
print(two_sum([4,7,1,-3,2], 4))
# True
print(two_sum([4,7,1,-3,2], 0))
# False