import redisManagement
import massGenerator
import mongoConnection


redisManagement.backgroundDef.start()

print("Seja bem vindo ao cache companion")

while True:

  userOption = input("Por favor, escolha uma opção: \n0) Para Sair \n1) Ver todos os dados do banco \n2) Ver todas as chaves do redis \n3) Inserir estudantes no banco de dados \n4) Inserir um estudantes no banco de dados \n5) Encontrar um estudante no banco \n6) Encontrar um estudante no REDIS \n7) Limpar banco de dados \n8) Excluir um Estudante \n9) Para limapr o Cache\n")
  
  match userOption:
      case '0':
          break
      case '1':
          print(list(mongoConnection.col.find()))
      case '2':
          i = 1
          for key in redisManagement.redisClient.scan_iter("*"):
            print(i, '° ' ,key)
            i+=1
      case '3':
          qtdStudents = int(input("Digite a quantidade de estudantes que deseja inserir: "))
          newStudents = []
          try:
            for qtd in range(qtdStudents):
              newStudents.append(massGenerator.generatePerson())
            mongoConnection.col.insert_many(newStudents)
            print("Alunos inseridos com Sucesso!")
          except Exception as ex:
             print("Erro ao inserir alunos! Erro:", ex)
      case '4':
        nomeStudent = input("Digite o nome do Estudande: ")
        cpfStudent = input("Digite o cpf do Estudante: ")
        statusStudent = input("Digite o status do Estudante: ")
        uniStudent = input("Digite a faculdade do Estudante: ")
        anoStudent = input("Digite o ano em que o Estudante ingressou na instituição: ")

        try:
          mongoConnection.col.insert_one(massGenerator.createPerson(nomeStudent, cpfStudent, statusStudent, uniStudent, anoStudent))
          print("Aluno inserido com sucesso!")
        except Exception as ex:
          print("Erro ao inserir aluno! Erro:", ex)
      case '5':
        nameStudent = input("Digite o nome do estudante: ")
        found = list(mongoConnection.col.find({"nome": nameStudent}))
        if found != []:
          print(found)
        else:
          print("Estudante não consta no banco de dados")
      case '6':
        nameStudent = input("Digite o nome do estudante: ")
        print(redisManagement.getFromCache(nameStudent))
      case '7':
        try:
           mongoConnection.col.delete_many({})
           print("Banco de dados limpado!")
        except Exception as ex:
           print("Erro ao limpar o banco de dados!", ex)
      case '8':
        campo = input("Digite o campo: ")
        valor = input("Digite o valor: ")
        try:
          mongoConnection.deleteUm(campo, valor)
        except Exception as ex:
           print("Erro ao excluir!", ex)
      case '9':
        redisManagement.clearCache()