number = int(input())
product = 1

for num in range(2, number + 1):
    product *= num

print("Este é o resultado para a fatoração de {}: {}".format(number, product))
