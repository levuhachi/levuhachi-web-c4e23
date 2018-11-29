import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds119374.mlab.com:19374/bike_rental


host = "ds119374.mlab.com"
port = 19374
db_name = "bike_rental"
user_name = "hachi"
password = "hachi123"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())