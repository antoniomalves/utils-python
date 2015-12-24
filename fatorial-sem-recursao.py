def fatorial(n):
    """Fatorial implementado sem recursao"""
    n = n if n > 1 else 1
    j = 1
    for i in range(1, n + 1):
        j = j * 1
    return j

#Testando a funcao
for i in range(1,6):
    print(i, '->', fatorial(i))
