from pymongo import MongoClient
import stocks

mongo = MongoClient()
db = mongo.stock
user = db.user

stocklist = user.find()

for stock in stocklist:
  price = stocks.get_quote(stock['stock'])
  try:
    user.update({'_id':stock['_id']},{'stock':stock['stock'],'price':price},upsert=False, multi=False)
    print(stock['stock'] + " updated")
    print("{'stock':"+stock['stock']+",'price':"+price+"}")
  except:
    print("Uhoh, some shit happened")

