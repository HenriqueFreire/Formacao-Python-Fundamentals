nome = "Henrique"
idade = 32
profissão = "Programador"
linguagem = "Python"

dados = {"nome": "Henrique", "idade": 32}

print("Nome: %s Idade: %d" % (nome, idade))
print("Nome: {} Idade: {}".format((nome, idade)))
print("Nome: {1} Idade: {0}".format(idade, nome))
print("Nome: {name} Idade: {age}".format(name=nome, age=idade))
print("Nome: {nome} Idade: {idade".format(**dados))

