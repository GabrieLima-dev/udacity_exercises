idade_inteiro = int(input())
idade = idade_inteiro
if idade < 12:
    print('crianca')
elif idade < 18:
    print('Adolecente')
elif idade < 60:
    print('Adulto')
else:
    print('Idoso')
