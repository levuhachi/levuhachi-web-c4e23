import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds117334.mlab.com:17334/homework_bonus


host = "ds117334.mlab.com"
port = 17334
db_name = "homework_bonus"
user_name = "admin"
password = "admin1@3"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())