import redis
import mongoConnection
import threading

redisClient = redis.Redis(host="localhost", port=6379, db=0)

def cacheData():
  data = list(mongoConnection.col.find())
  for student in data:
    redisClient.set(student['nome'], str(student))
  #redisClient.set('mongoCached', str(data))

def checkCache(key: str = '*'):
  if key != '*':
    data = redisClient.get(key)
  else:
    data = redisClient.scan_iter(key)
  if data is None:
    cacheData()

def updateCache():
  cacheData()

def clearCache(key = None):
  if key == None:
    redisClient.flushdb()
  else:
    redisClient.delete(key)

def getFromCache(key: str):
  checkCache()
  data = redisClient.get(key)
  return data

def run():
  while True:
    try:
      with mongoConnection.col.watch() as stream:
        for change in stream:
          if change['operationType'] == 'delete':
            key = str(change['documentKey']['cpf'])
            clearCache(key)
          else:
            cacheData()
          print("Dados atualizados")
    except Exception as ex:
      print("Error: ", ex)

backgroundDef = threading.Thread(target=run)
backgroundDef.daemon = True