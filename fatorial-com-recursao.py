def fatorial(num):
    """Fatorial implementado de forma recursiva"""
    if num <= 1:
        return 1
    else:
        return(num * fatorial(num-1))

# Testando fatorial()
print(fatorial(5))
