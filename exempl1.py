def esta_ordenada(conj: list) -> bool:  #A função esta_ordenada recebe uma lista conj como argumento e retorna um valor booleano (True ou False).
    i = 0 # A variável i é inicializada com o valor 0. Ela será usada para percorrer os elementos da lista.
    while i < len(conj) - 1: # Este laço continua enquanto i for menor que o comprimento da lista menos 1. Isso garante que o laço percorra todos os elementos da lista, exceto o último.
        if conj[i] > conj[i + 1]: #  Dentro do laço, verifica-se se o elemento atual (conj[i]) é maior que o próximo elemento (conj[i + 1]). Se for, a função retorna False, indicando que a lista não está ordenada.
            return False
        i = i + 1 # O índice i é incrementado em 1 para passar ao próximo par de elementos na próxima iteração do laço.

    return True  # Se o laço terminar sem encontrar nenhum par de elementos fora de ordem, a função retorna True, indicando que a lista está ordenada.
