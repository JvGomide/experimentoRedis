import pymongo
import massGenerator

cli = pymongo.MongoClient('mongodb+srv://jvgomide:jvgc2001@cluster0.r8ulunl.mongodb.net/?retryWrites=true&w=majority')
database = cli['Cluster0']
col = database["Teste"]

listaPessoas = [];

def deleteUm(campo, valor):
  query = {campo: valor}
  col.delete_one(query)

#for i in range(5):
#  pessoa = massGenerator.generatePerson()
# listaPessoas.append(pessoa)

#print(listaPessoas);

#clearCol = col.delete_many({})
#print(clearCol.deleted_count, " elements deleted")

#firstsStudents = col.insert_many(listaPessoas)