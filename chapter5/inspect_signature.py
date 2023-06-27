from inspect import signature


def fn(a, b=1):
    return a + b


sig = signature(fn)
print(sig)

print(sig.parameters)