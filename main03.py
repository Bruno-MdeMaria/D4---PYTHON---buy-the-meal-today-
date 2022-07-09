import random


test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")


paga = (names[random.randint(0,len(names)-1)])  #a função len() conta quantos itens tem na lista. a função random gera um numero entre 0 (primeiro da lista) e a quanitidade final de itens da lista contadas pelo len menos 1(porque tem que contar do zero)
print(f"{paga} is going to buy the meal today!")
