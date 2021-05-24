number = int(input())
product = 1
current = 1

while current <= number:
    product *= current
    current += 1

print(product)
