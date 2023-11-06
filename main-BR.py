def func():

    # Pergunta quantas dimensões e pontos
    dimensoes = int(input('Quantas dimensões tem? '))
    quantidade_de_pontos = int(input('Quantos pontos tem? '))

    # Faz as coisas serem variáveis globais
    termos = []
    lista = []
    quase_la = []
    resultadoo = []

    # Pergunta as coordenadas dos pontos
    for ponto in range(0, quantidade_de_pontos):
        for dimension in range(0, dimensoes):
            termo = float(input(f'Diga qual o {ponto + 1} termo, da {dimension + 1} dimensão: '))
            termos.append(termo)

    # Faz a computação de x1 - x2 para n dimensões com s pontos
    for permutacao2 in range(0, quantidade_de_pontos):  
        for permutacao1 in range(1, quantidade_de_pontos - permutacao2):  
            for j in range(0, dimensoes):
                # Em j, faço a permutação entre 2 pontos, após isso, em permutacao1 faço ela considerando 
                # a permutação que ocorre no eixo x (visualização disso no final do código), e por último a permutação2
                # que ocorre no eixo y, note que na permutacao1 se retira parte dela 
                # pelo número da permutação 2, é possível ver o porquê disso, no gráfico
                lista.append((termos[j + (permutacao2 * dimensoes)] - termos[
                    j + (dimensoes * (permutacao1 + permutacao2))]) ** 2)
                
    # Computa a quantidade de resultados usando uma fórmula da teoria dos grafos
    np = int((quantidade_de_pontos * (quantidade_de_pontos - 1)) / 2)

    # Torna a lista numa lista de listas para poder usar sum em cada uma delas deve
    for s in range(0, np):
        quase_la.append(lista[s * dimensoes: s * dimensoes + dimensoes])
        
    # Aqui se soma e já computa a raiz quadrada de cada par de pontos e coloca numa lista chamada resultadoo
    for resultado in range(0, np):  # faço isso np vezes, pois só tera np resultados
        resultadoo.append(sum(quase_la[resultado]) ** (1 / 2))

    print('=' * 70)
    for RESULTADO in range(0, np):
        print(f'A distância entre o {RESULTADO + 1} par de pontos é {resultadoo[RESULTADO]}')
    print('=' * 70)


if __name__ == "__main__":
    func()
    
    

# Para 2 dimensões e 5 pontos fica assim:
#
# 11   12   21   22   31   32    41    42    51   52
#                                                          eixo x-----------------
# j1  j2   jd1 jd2  -      -     -     -     -    -      = |  I I I I
# j1  j2   -   -    j2d1   j2d2  -     -     -    -      = |  I I     I I
# j1  j2   -   -    -       -    j3d1 j2d2   -    -      = e  I I         I I
# j1  j2   -   -    -       -     -     -   j4d1 j4d2    = i  I I             I I
#                                                          x
#  -   -   jd1 jd2  j2d1   j2d2   -     -    -    -      = o      I I I I
#  -   -   jd1 jd2  -       -     j3d1 j3d2  -    -      = |      I I     I I
#  -   -   jd1 jd2  -       -     -     -   j4d1 j4d2    = y      I I         I I
#                                                          |
#  -   -    -   -   j2d1   j2d2   j3d1 j3d2  -    -      = |          I I I I
#  -   -    -   -   j2d1   j2d2   -     -   j4d1 j4d2    = |          I I     I I
#                                                          |
#  -   -    -   -   -       -     j3d1 j3d2 j4d1 j4d2    = |              I I I I
