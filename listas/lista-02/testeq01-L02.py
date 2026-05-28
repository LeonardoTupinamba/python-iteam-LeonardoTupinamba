# dados = {"nome": "Ana", "notas": [8.0, 7.5, 9.0]}
# dados["notas"].append(6.5)
# media = sum(dados["notas"]) / len(dados["notas"])
# dados["media"] = round(media, 2)
# chaves = list(dados.keys())
# print(dados["nome"])
#print(media)
#print(chaves)

x = 'global'
def externa():
  x = 'enclosing'
  def interna():
    print(x)
  interna()
  print(x)
  
externa()
print(x)