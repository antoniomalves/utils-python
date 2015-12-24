def fib(n):
    """Fibonacci implementado com recursao
    fib(n) = fib(n -1) + fib(n - 2) se n > 1
    fib(n) = 1 se ne <= 1
    """
    if n > 1:
        return fib(n - 1) + fib(n - 2)
    else:
        return 1

# Testando a implementacao da funcao
for i in range(6):
    print(i, '=>', fib(i))
