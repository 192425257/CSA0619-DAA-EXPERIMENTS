import math

def complexity(n):
    return n * math.log2(n)

n = int(input("Enter number of users: "))

print("Approximate operations =", complexity(n))
print("Time Complexity = Θ(n log n)")
