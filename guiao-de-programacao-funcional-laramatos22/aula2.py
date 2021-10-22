import math

### 4. Expressões-lambda e funções de ordem superior ###
# Example:
# def sum(a, b) : return a+b
# lambda a, b : a+b
# a, b -> parameters
# a+b -> return

#Exercicio 4.1 ->   (Implementar na forma de uma expressão-lambda:) Dado um número inteiro, retorna True
#                   caso o número seja ı́mpar, e False caso contrário.
impar = lambda num : False if (num % 2 == 0) else True

#Exercicio 4.2 ->   (Implementar na forma de uma expressão-lambda:) Dado um número, retorna True caso
#                   o número seja positivo, e False caso contrário.
positivo = lambda num : True if (num >= 0) else False

#Exercicio 4.3 ->   (Implementar na forma de uma expressão-lambda:) Dados dois números, x e y, retorna
#                   True caso |x| < |y|, e False caso contrário.
comparar_modulo = lambda x, y : True if (abs(x) < abs(y)) else False

#Exercicio 4.4 ->   (Implementar na forma de uma expressão-lambda:) Dado um par (x, y), representando
#                   coordenadas cartesianas de um ponto no plano XY, retorna um par (r, θ), correspondente
#                   às coordenadas polares do mesmo ponto.
cart2pol = lambda x, y : (math.sqrt((pow(x, 2) + pow(y, 2))), math.atan2(y, x))

#Exercicio 4.5 ->   Dadas três funções de duas entradas, f, g e h, retorna uma função de três entradas, x, y e
#                   z, cujo resultado é dado por: h(f (x, y), g(y, z)).
ex5 = lambda f, g, h : lambda x, y, z : h(f(x, y), g(y, z))

#Exercicio 4.6 ->   Dada uma lista e uma função booleana unária, retorna True caso a função também retorne
#                   True para todos os elementos da lista, e False caso contrário. ( Quantificador universal )
def quantificador_universal(lista, f):
    if lista == []:
        return True
    
    if f(lista[0]):
        return quantificador_universal(lista[1:], f)
    return False
    #pass

#Exercicio 4.9 ->   Dada uma lista com pelo menos um elemento e uma relação de ordem (ou seja, uma função
#                   booleana binária usada para comparação elemento a elemento), retorna o menor elemento
#                   da lista de acordo com essa relação de ordem.
def ordem(lista, f):
    if lista == []:
        return None
    
    min = ordem(lista[0:len(lista)-1], f)

    if min == None:
            min = lista[0]
    elif (f(min, lista[len(lista)-1]) == False):
        min = lista[len(lista)-1]
    return min
    #pass

#Exercicio 4.10 ->  Dada uma lista com pelo menos um elemento e uma relação de ordem, retorna um par
#                   contendo o menor elemento da lista, de acordo com essa relação de ordem, e uma lista com
#                   os restantes elementos.
def filtrar_ordem(lista, f):
    min = ordem(lista, f)

    result = []

    for value in lista:
        if value != min:
            result.append(value)
    return (min, result)
    #pass

#Exercicio 5.2 ->   Similar ao número anterior, mas sem restrição no tipo dos elementos da lista de entrada.
#                   A função de ordenação recebe, num parâmetro adicional, a relação de ordem (uma função
#                   binária booleana para comparação elemento a elemento) segundo a qual a lista de entrada
#                   deve ser ordenada.
def ordenar_seleccao(lista, ordem):
    if lista == []:
        return []

    (min, l) = filtrar_ordem(lista, ordem)
    return [min] + ordenar_seleccao(l, ordem)
    #pass
