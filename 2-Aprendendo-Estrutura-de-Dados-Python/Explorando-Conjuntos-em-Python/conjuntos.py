set([1, 2, 3, 1, 3, 4]) # {1, 2, 3, 4}

set("abacaxi") # {"b", "a", "c", "x", "i"}

carros = set(("palio", "gol", "celta", "palio")) # {"palio", "gol", "celta"}

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

conjunto_a = {1, 2}
conjunto_b = {3, 4}

conjunto_a.union(conjunto_b) # {1, 2 ,3 ,4}

conjunto_c = {1, 2, 3}
conjunto_d = {2, 3, 4}

conjunto_c.intersection(conjunto_d) # {2, 3}

conjunto_c.difference(conjunto_d) # {1}
conjunto_d.difference(conjunto_c) # {4}

conjunto_c.symmetric_difference(conjunto_d) # {1,4}

conjunto_a.issubset(conjunto_c) # True
conjunto_c.issubset(conjunto_a) # False

conjunto_c.issuperset(conjunto_a) # True
conjunto_a.issubset(conjunto_c) # False

conjunto_a.isdisjoint(conjunto_b) # True
conjunto_a.isdisjoint(conjunto_c) # False

conjunto_a.add(7) # {1, 2, 7}
conjunto_a.add(2) # {1, 2, 7}

conjunto_b.clear()
conjunto_b # {}

conjunto_c.copy() 

conjunto_a.discard(7) # {1, 2}

conjunto_d.pop() # {3, 4}

1 in conjunto_a # True
5 in conjunto_a # True

