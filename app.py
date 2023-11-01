# Collections = Arrays

# List = []
# Valores duplicados = True
# Valores alteráveis = True
# Ordenado = True

# Set = {}
# Valores duplicados = False
# Valores alteráveis = False
# Ordenado = False

# Tuple = () -> Mais rápido
# Valores duplicados = True
# Valores alteráveis = False
# Ordenado = True

# |        |
# | LISTAS |
# |        |

#            0        1          2        3
fruits = ['Maçã', 'Laranja', 'Banana', 'Mamão']

print(fruits[0])         # Primeiro valor
print(fruits[:3])        # 3 primeiros valores
fruits[2] = 'Abacaxi'    # 3 primeiros valores
# fruits.insert(0, 'Abacaxi')

print(fruits[::2])       # Mostrar a cada dois
print(fruits[::-1])      # Reverso
print(len(fruits))       # Total de items
print('Maçã' in fruits)  # Tem o valor na lista?

print(dir(fruits))       # Métodos que podem ser usados
# print(help(fruits))    # Descrição de tudo que pode ser feito com a lista

#  — -[Algumas funções úteis]--

fruits.append('Goiaba')   # Inserir valor no fim
fruits.remove('Laranja')  # Remover valor
fruits.sort()             # Ordenar em ordem alfabética (maior pro menor)
fruits.reverse()          # Reverter com base nos índices
fruits.index('Maçã')      # Retorna o index do valor passado
fruits.count('Maçã')      # Conta quantas ocorrências tem daquele item
fruits.clear()            # Remove tudo

# Para cada item dentro da lista, fazer algo...
for fruit in fruits:
    print(fruit)

print("\n\n")

# |      |
# | SETS |
# |      |

fruits_set = {'Maçã', 'Laranja', 'Banana', 'Mamão'}

print(fruits_set)
print(dir(fruits_set))
fruits_set.add('Valor')
fruits_set.remove('Valor')

# Para cada item dentro da lista, fazer algo...
for fruit in fruits_set:
    print(fruit)
