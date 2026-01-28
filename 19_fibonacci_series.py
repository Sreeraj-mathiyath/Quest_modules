def fibonacci(limit):
    a=0
    b=1
    series=[]
    while a<=limit:
        series.append(a)
        a,b=b,b+a
    return series

print(fibonacci(20))


