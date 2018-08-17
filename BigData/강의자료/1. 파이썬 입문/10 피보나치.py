def f(n):
    if n == 1 or n == 2:
        return 1
    
    fibo = [1,1]

    for i in range(n-2):
        fibo.append(fibo[-1] + fibo[-2])
        

    return fibo[-1]

print(f(6))

def pass1(): # 구현할 예정인데
    pass
