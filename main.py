import matplotlib.pyplot as plt

def P(m) -> int:
    if m in [0,1]:
        return m
    else: 
        return sum([(nC(m, i) + P(m-i)) for i in range(m)])

def nC (n, k) -> int:
    # numero combinatorio
    return (factorial(n) / (factorial(k) * factorial(n-k)))

def factorial (n) -> int:
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

for j in [1,2]:
    print (j, P(j))

# rango_m = list(range(1,20))
# plt.plot(rango_m, [P(i) for i in rango_m])
# plt.show()