numero_desejado = int(input('Digite o número inteiro desejado: '))
a = 0
b = 1
fibonacci = [a, b]
while True:
    proximo_numero = a + b
    fibonacci.append(proximo_numero)
    a = b
    b = proximo_numero
    if proximo_numero >= numero_desejado:
        break
print(f'Sequência Fibonacci: {fibonacci}')
if numero_desejado in fibonacci:
    print('O número desejado encontra-se na sequência fibonacci.')
else:
    print('O número desejado não encontra-se na sequência fibonacci.')
