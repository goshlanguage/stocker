from mongoengine import connect, Document, StringField, FloatField, ListField, DictField, DateTimeField, IntField
import datetime

client = connect()
db = client.stock

class Stock(Document):
  name = StringField()
  symbol = StringField()
  last_price = FloatField(default=0.00)
  last_open = FloatField(default=0.00)
  last_high = FloatField(default=0.00)
  last_low = FloatField(default=0.00)
  last_close = FloatField(default=0.00)
  history = ListField()
  sentiment = IntField(default=0)
  meta_info = DictField()
  last_updated = DateTimeField(default=datetime.datetime.now())
