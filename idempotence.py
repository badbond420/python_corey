#idempotense example
# f(f(x)) = f(x)
print(abs(-5))
print(abs(abs(-5)))


# non idempotence example
def sum10(num):
    return num + 10

# f(f(x)) != f(x)
print(sum10(10))
print(sum10(sum10(10)))