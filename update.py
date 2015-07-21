#from pymongo import MongoClient
from mongoengine import MongoEngine, Document, StringField, DateTimeField, FloatField, ArrayField, DictField
import stocks

mongo = MongoEngine()
db = mongo.stock


 
  
  
# Grab user stocks 
#user = db.user
#stocklist = user.find()



#for stock in stocklist:
#  price = stocks.get_quote(stock['stock'])
#  try:
#    user.update({'_id':stock['_id']},{'stock':stock['stock'],'price':price},upsert=False, multi=False)
#    print(stock['stock'] + " updated")
#    print("{'stock':"+stock['stock']+",'price':"+price+"}")
#  except:
#    print("Error location stock %s" % stock['name'])



