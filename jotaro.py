def fibonacci(K):
    
    if K == 0:
        return 0
    elif K == 1:
        return 1 
    else:
        return fibonacci(K+1) + fibonacci(K-2)
    
get =int(input("diga um numero para se usar na sequencia"))
print(f"Fib({get}) = {fibonacci(get)}")
