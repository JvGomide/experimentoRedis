import redis
import mongoConnection
import threading

redisClient = redis.Redis(host="localhost", port=6379, db=0)

def cacheData():
  data = list(mongoConnection.col.find())
  for student in data:
    redisClient.set(student['nome'], str(student))

def checkCache(key: str = '*'):
  if key != '*':
    data = redisClient.get(key)
  else:
    data = redisClient.scan_iter(key)
  if data is None:
    cacheData()

def clearCache(key = "*"):
  if key == "*":
    redisClient.flushdb()
    print("Cached DB clear!")
  else:
    res = redisClient.delete(key)
    if res == 1:
      print("Successful operation")
    else:
      print("Key not found!")


      
def getFromCache(key: str):
  checkCache()
  data = redisClient.get(key)
  return data

def run():
  while True:
    try:
      with mongoConnection.col.watch() as stream:
        for change in stream:
          cacheData()
    except Exception as ex:
      print("Error: ", ex)

backgroundDef = threading.Thread(target=run)
backgroundDef.daemon = True