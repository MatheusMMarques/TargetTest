# Solicita ao usuário que digite um valor e converte a entrada para inteiro
valor = int(input("Digite um valor: "))

# Inicializa os primeiros dois números da sequência Fibonacci
v1 = 0
v2 = 1

# Inicializa a variável soma com a soma dos dois primeiros números
soma = v2 + v1

# O loop continuará enquanto o valor digitado for maior que a soma dos números da sequência
while valor > soma:
    # Atualiza os valores dos dois últimos números da sequência para avançar na sequência Fibonacci
    v1 = v2
    v2 = soma 
    soma = v2 + v1   

# Verifica se o valor digitado está na sequência Fibonacci
if valor == soma:
    print("Este número está na sequência Fibonacci")
else:
    print("Este número não está na sequência Fibonacci")
