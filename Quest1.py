# Define o valor de índice como 13
indice = 13
soma = 0

# Inicializa a variável K como 0 para servir como contador no loop
K = 0

# Enquanto K for menor que o índice, o loop continuará, garantindo que somaremos até o índice definido
while K < indice:
    # Incrementa o valor de K em 1 para avançar para o próximo número a ser somado
    K = K + 1
    
    # Adiciona o valor de K ao valor atual de soma, acumulando os resultados da soma
    soma = soma + K

print("O valor da variável soma é:", soma)
