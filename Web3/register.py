from mongoengine import *

class Register(Document):
    email = EmailField()
    # email_verified = BooleanField(default=False) # --> users need to click on a website on the email, then verify email
    username = StringField()
    password = StringField()