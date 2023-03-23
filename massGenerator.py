import random
import universities
import pymongo
from faker import Faker
from cpf_generator import CPF

uni = universities.API()
unis = uni.search(country = "Brazil")
uniNameList = []
for n in unis:
  uniNameList.append(n.name)

def generatePerson():
  fake = Faker()
  nome = fake.name()
  cpf = CPF.generate()
  status = random.choice(['Aprovado','Reprovado'])
  if(status != "Reprovado"):
    universidade = random.choice(uniNameList)
  else:
    universidade = ""
  ano = random.randint(1980, 2023)
  return{
      'nome': nome,
      'cpf': cpf,
      'status': status,
      'universidade': universidade,
      'ano': ano
  }

listaPessoas = [];

for i in range(10):
  pessoa = generatePerson()
  listaPessoas.append(pessoa)

#print(listaPessoas);

cli = pymongo.MongoClient('mongodb+srv://jvgomide:jvgc2001@cluster0.r8ulunl.mongodb.net/?retryWrites=true&w=majority')
database = cli['Cluster0']
col = database["Participantes"]

#clearCol = col.delete_many({})
#print(clearCol.deleted_count, " elements deleted")

firstsStudents = col.insert_many(listaPessoas)
print(firstsStudents.inserted_ids)