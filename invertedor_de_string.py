indice = - 1
string = input('Digite o texto que deseja inverter: ').strip()
invertido = ''
for a in range(0, len(string)):
    letra = (string[indice])
    indice -= 1
    invertido = invertido + letra
print(invertido)
