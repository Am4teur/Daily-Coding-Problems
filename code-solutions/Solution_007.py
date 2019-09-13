import time
import random

# Both are O(N**2) but the first one is faster on average because it computes
# less results and reuses already computed results
def findPythagoreanTriplets(nums):
    res = [c**2 for c in nums]

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if(res[i] + res[j] in res):
                return True

    return False


def findPythagoreanTriplets2(nums):
    res = []

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            res.append(nums[i]**2 + nums[j]**2)
    
    for c in nums:
        if(c**2 in res):
            return True

    return False



print(findPythagoreanTriplets([3, 12, 5, 13]))
#True

print(findPythagoreanTriplets([3, 4, 5, 6, 7]))
#True

print(findPythagoreanTriplets([3, 5, 6, 7]))
#False


# Proof that the first method is, in average, faster than the second method
my_randoms = [random.randrange(1, 101, 1) for _ in range(100)]

start_time = time.time()

print(findPythagoreanTriplets(my_randoms))

print(f"--- 1: {time.time() - start_time} seconds ---")

start_time = time.time()

print(findPythagoreanTriplets2(my_randoms))

print(f"--- 2: {time.time() - start_time} seconds ---")