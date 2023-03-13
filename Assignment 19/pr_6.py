def f1(a,b,c,d):
    a = max(a,b)
    c = max(c,d)
    return max(a,c)
x = f1(c=10, a=10, b=15, d=50)
print("Max =",x)
