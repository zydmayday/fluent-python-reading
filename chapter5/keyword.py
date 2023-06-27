def f(a, *, b):
    return a, b

print(f(1, b=2))
print(f(a=1, b=2))
