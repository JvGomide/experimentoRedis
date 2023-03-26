import random
import universities
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

def createPerson(nome: str, cpf: str, status: str, universidade: str, ano: str) -> dict:
  return {
    'nome': nome,
    'cpf': cpf,
    'status': status,
    'universidade': universidade,
    'ano': ano
  }