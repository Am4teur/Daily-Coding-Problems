# simple solution O(n) time, specifically for 1 and 2 steps
def staircase(n):
    ways = [1, 2]

    for i in range(2, n):
        ways.append(ways[i-1] + ways[i-2])

    return ways[-1]

# recursive solution, specifically for 1 and 2 steps
def staircaseRec(n):
    if(n <= 2):
        return n

    return staircase(n-1) + staircase(n-2)

# General solution for any m steps, iteratively (and recursively, commented)
def staircase(n, m=2):
    return staircaseAux(n + 1, m)
    # return staircaseAuxRec(n + 1, m)

# Auxiliar method for general solution iteratively
def staircaseAux(n, m):
    ways = [1]

    for i in range(1, n):
        val = 0
        for j in range(1, m+1):
            if(i-j >= 0):
                val += ways[i-j]
        ways.append(val)

    return ways[-1]

# Auxiliar method for general solution recursively
def staircaseAuxRec(n, m):
    if(n <= 1):
        return n

    val = 0
    for i in range(1, m+1):
        if(i<=n):
            val += staircaseAuxRec(n-i, m)

    return val



if(__name__ == "__main__"):
    print(staircase(4, 3))
    # 5
    print(staircase(5, 2))
    # 8
    print(staircase(6, 2))
    # 13