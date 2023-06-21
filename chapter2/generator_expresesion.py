xs = (x for x in [1, 2, 3])
print(xs)

for x in xs:
    print(x)

# this does not work
print([x for x in xs])
