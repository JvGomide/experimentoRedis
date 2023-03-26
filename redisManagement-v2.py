import redis
import mongoConnection

redisClient = redis.Redis(host="localhost", port=6379, db=0)

def cacheData():
  data = list(mongoConnection.col.find())
  redisClient.set('mongoCached', str(data))

def checkCache():
  data = redisClient.get("mongoCached")
  if data is None:
    cacheData()

def getFromCache():
  checkCache()
  data = redisClient.get('mongoCached')
  return data

checkCache()

while True:
  try:
    with mongoConnection.col.watch() as stream:
      for change in stream:
        cacheData()
        print("Cache updated with latest data.")
  except Exception as e:
    print("Error: ", e)