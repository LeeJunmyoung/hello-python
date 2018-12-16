## 피보나치 수열 Memoization 
memory = {}


def fibonacci(n):
    if n in memory:
        return memory[n]

    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        output = fibonacci(n-2)+fibonacci(n-1)
        memory[n]=output
        return output


print(fibonacci(30))
print(memory)

