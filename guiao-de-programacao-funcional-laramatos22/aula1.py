### 1. Funções para processamento de listas ###

#Exercicio 1.1 -> 	Dada uma lista, retorna o seu comprimento.
def comprimento(lista):
	if lista == []:
		return 0
	size = comprimento(lista[1:]) + 1
	return size
	#pass
	
#Exercicio 1.2 -> 	Dada uma lista de números, retorna a respectiva soma.
def soma(lista):
	if lista == []:
		return 0
	sum = lista[0] + soma(lista[1:])
	return sum
	#pass

#Exercicio 1.3 -> 	Dada uma lista e um elemento, verifica se o elemento ocorre na lista. Retorna um valor booleano.
def existe(lista, elem):
	if lista == []:
		return False
	if lista[0] == elem:
		return True
	return existe(lista[1:], elem)
 	#pass

#Exercicio 1.4 -> 	Dadas duas listas, retorna a sua concatenação.
def concat(l1, l2):
	if l2 == []:
		return l1[:]
	lista = concat(l1, l2[0:len(l2)-1])
	lista.append(l2[len(l2)-1])
	return lista

	### OU ###
	#conc = l2[:]
	#conc[:0] = l1
	#return conc
	#pass

#Exercicio 1.5 -> 	Dada uma lista, retorna a sua inversa.
def inverte(lista):
	if lista == []:
		return []
	invList = inverte(lista[1:])
	invList[len(lista):] = [lista[0]]
	return invList
	#pass

#Exercicio 1.6 -> 	Dada uma lista, verifica se forma uma capicua, ou seja, se, quer se leia da esquerda para a
#					direita ou vice-versa, se obtêm a mesma sequência de elementos.
def capicua(lista):
	if lista == []:
		return True
	return lista[0] == lista[len(lista)-1] and capicua(lista[1:len(lista)-1])
	#pass

#Exercicio 1.7 ->	Dada uma lista de listas, retorna a concatenação dessas listas.
def explode(lista):
	if lista == []:
		return []
	lst = explode(lista[:len(lista)-1])
	lst += lista[len(lista)-1]
	return lst
	#pass

#Exercicio 1.8 -> 	Dada uma lista, um elemento x e outro elemento y, retorna uma lista similar à lista de
#					entrada, na qual x é substituido por y em todas as ocorrências de x.
def substitui(lista, original, novo):
	if(lista == []):
		return []
	res = substitui(lista[:len(lista)-1], original, novo)
	if(lista[len(lista)-1] == original):
		res[len(lista)-1:] = [novo]
	else:
		res[len(lista)-1:] = [lista[len(lista)-1]]
	return res
	#pass

#Exercicio 1.9 -> 	Dadas duas listas ordenadas de números, calcular a união ordenada mantendo eventuais
#					repetições.
def junta_ordenado(lista1, lista2):
	if lista1 == []:
		return lista2
	if lista2 == []:
		return lista1
	unionList = []
	if lista2[0] < lista1[0]:
		unionList[:0] = [lista2[0]]
		return unionList + junta_ordenado(lista1, lista2[1:])
	if lista1[0] > lista2[0]:
		unionList[:0] = [lista1[0]]
		return unionList + junta_ordenado(lista1[1:], lista2)
	unionList[:0] = [lista1[0], lista2[0]]
	return unionList + junta_ordenado(lista1[1:], lista2[1:])
	#pass

#Exercicio 1.10 -> 	Dado um conjunto, na forma de uma lista, retorna uma lista de listas que representa o
#					conjunto de todos os subconjuntos do conjunto dado.
def subconjuntos(lista):
	if lista == []:
		return [[]]
	res = subconjuntos(lista[1:])
	return res + [[lista[0]] + y for y in res]

### 2. Funções para processamento de listas e tuplos ###

#Exercicio 2.1 -> 	Dada uma lista de pares, produzir um par com as listas dos primeiros e segundos elementos
#					desses pares.
#					separar ([( a1, b1), ... (an, bn)]) = ([a1, ... an ], [b1, ... bn])
def separar(lista):
	if lista == []:
		return ([],[])
	result = separar(lista[0:len(lista)-1])
	result[0].append(lista[len(lista)-1][0])
	result[1].append(lista[len(lista)-1][1])
	return result
	#pass

#Exercicio 2.2 -> 	Dada uma lista l e um elemento x, retorna um par formado pela lista dos elementos de l
#					diferentes de x e pelo número de ocorrências x em l.
#					Exemplo:
#						>>> remove_e_conta( [ 1 , 6 , 2 , 5 , 5 , 2 , 5 , 2 ] , 2 )
#						([1 ,6 ,5 ,5 ,5] ,3)
def remove_e_conta(lista, elem):
	if lista == []:
		return ([], 0)
	result = remove_e_conta(lista[0:len(lista)-1], elem)
	if lista[len(lista)-1] == elem:
		aux = list(result)
		aux[1] += 1
		result = tuple(aux)
	else:
		result[0].append(lista[len(lista)-1])
	return result
	#pass

#Exercicio 2.3 -> 	Dada uma lista, retorna o número de ocorrências de cada elemento, na forma de uma lista
#					de pares (elemento,contagem).
def contar_elementos(lista):
	if lista == []:
		return []
	
	result = contar_elementos(lista[0:len(lista)-1])

	if len(result) == 0:
		result.append(lista[0], 1)
	else:
		elem = lista[len(lista)-1]
		max = len(result)
		check = False
		for i in range(0, max):
			if result[i][0] == elem:
				aux = list(result[i])
				aux[1] += 1
				result[i] =  tuple(aux)
				check = True

		if check == False:
			result.append((elem, 1))
	
	return result
	#pass

### 3. Funções que retornam None ###

#Exercicio 3.1 ->	Dada uma lista, retornar o elemento que está à cabeça (ou seja, na posição 0).
def cabeca(lista):
	if lista == []:
		return None
	return lista[0]
	#pass

#Exercicio 3.2 ->	Dada uma lista, retornar a sua cauda (ou seja, todos os elementos à excepção do primeiro).
def cauda(lista):
	if lista == []:
		return None
	return lista[1:]
	#pass

#Exercicio 3.3 ->	Dado um par de listas com igual comprimento, produzir uma lista dos pares dos elementos
#					homólogos.
def juntar(l1, l2):
	if len(l1) != len(l2):
		return None
	elif (l1 == [] and l2 == []):
		return []
	result = juntar(l1[0:len(l1)-1], l2[0:len(l2)-1])
	result.append((l1[len(l1)-1], l2[len(l2)-1]))
	return result
    #pass

#Exercicio 3.4 ->	Dada uma lista de números, retorna o menor elemento.
def menor(lista):
	if lista == []:
		return None
	min = menor(lista[0:len(lista)-1])

	if min == None:
		min = lista[0]
	if min > lista[len(lista)-1]:
		min = lista[len(lista)-1]
	return min
	#pass

#Exercicio 3.5 ->	Dada uma lista de números, retorna um par formado pelo menor elemento e pela lista dos
#					restantes elementos.
def min_lista(lista):
	if lista == []:
		return None
	min = menor(lista)
	result = []
	for value in lista:
		if value != min:
			result.append(value)
	return(min, result)
	#pass

#Exercicio 3.6 ->	Dada uma lista de números, calcular o máximo e o mı́nimo, retornando-os num tuplo.
def max_min(lista):
	if(lista == []):
		return None
		
	result = max_min(lista[0:len(lista)-1])
	
	if(result == None):
		result = (lista[0], lista[0])

	if(result[0] > lista[len(lista)-1]):
		result = (lista[len(lista)-1], result[1])

	if(result[1] < lista[len(lista)-1]):
		result = (result[0], lista[len(lista)-1])

	return result
	#pass

#Exercicio 3.7 ->	Dada uma lista de números, retorna um triplo formado pelos dois menores elementos e pela
#					lista dos restantes elementos.
def mins_lista(lista):
	if (lista == [] or len(lista) < 2):
		return None
	
	r0 = min_lista(lista)
	r1 = min_lista(r0[1])
	return (r0[0], r1[0], r1[1])
	#pass

#Exercicio 3.8 -> 	Dada uma lista ordenada de números, calcular se possı́vel a respectiva média e mediana,
#					retornando-as num tuplo.
def media_mediana(lista):
	if lista == []:
		return 0
	return (lista[0] + media_mediana(lista[1:])) / len(lista)
	#pass
