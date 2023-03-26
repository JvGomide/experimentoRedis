import pymongo
import redisManagement

cli = pymongo.MongoClient('mongodb+srv://comum:qwerty123456@cluster0.r8ulunl.mongodb.net/?retryWrites=true&w=majority')
database = cli['Cluster0']
col = database["Participantes"]

listaPessoas = [];

def deleteUm(campo, valor):
  query = {campo: valor}
  try:
    col.delete_one(query)
    redisKey = str(valor)
    print(redisKey)
    redisManagement.clearCache(redisKey)

  except Exception as ex:
    print("Erro:", ex)

#for i in range(5):
#  pessoa = massGenerator.generatePerson()
# listaPessoas.append(pessoa)

#print(listaPessoas);

#clearCol = col.delete_many({})
#print(clearCol.deleted_count, " elements deleted")

#firstsStudents = col.insert_many(listaPessoas)