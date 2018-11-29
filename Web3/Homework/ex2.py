from mongoengine import *

class Bike(Document):
    model = StringField()
    fee = IntField()
    image = StringField()
    year = IntField()
    