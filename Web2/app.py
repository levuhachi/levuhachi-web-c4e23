import mlab
from movie import Movie
from resource import Resource

from faker import Faker

mlab.connect()

faker = Faker("en_US")

# for _ in range(5):
#     print(faker.name())
#     print(faker.city())

# m = Movie(title = "Batman", year = 2005, image = "https://vignette.wikia.nocookie.net/marvel_dc/images/9/97/Batman_Vol_1_703.jpg/revision/latest?cb=20140104033356")
# m.save()

# resource_list = [
#     {
#         "name":"Chi",
#         "city":"Ha Noi",
#         "yob": 1998,
#         "height": 165,
#         "weight": 59,
#     },
#     {
#         "name":"Giang",
#         "city":"Ho Chi Minh",
#         "yob": 1998,
#         "height": 155,
#         "weight": 50,
#     },
#     {
#         "name":"Minh",
#         "city":"New York",
#         "yob": 1998,
#         "height": 175,
#         "weight": 65,
#     }
# ]
# for i in resource_list:
#     r = Resource(names = i["name"], city = i["city"], yob = i["yob"], height = i["height"], weight = i["weight"])
#     r.save()
# -----
# movie_list = Movie.objects()
# for m in movie_list:
#     print(m.title,m.image,m.year, sep = "\n")

# resource_list = Resource.objects()
# for r in resource_list:
#     print(r.names, r.city, r.yob, r.height, r.weight, sep = "\t")
# -----
# m = Movie.objects().with_id("5bf7fa08cea0ba332ba3c28f")
# m.delete()

# r = Resource.objects().with_id("5bf7ffd0cea0ba395d88448d")
# if r is None:
#   print("Not Found")
# else:
#   print("Found")
# r.delete()

# m = Movie.objects()[0]
# m.delete()                OR:
# m = Movie.objects().first()
# m.delete()

# from random import randint
# for _ in range(100):
#     name = faker.name()
#     city = faker.state()
#     yob = randint(1953,2000)
#     height=randint(150,200)
#     weight=randint(40,200)
#     r = Resource(name = name, city = city, yob = yob, height = height, weight = weight)
#     r.save()

# records = Resource.objects(name="Tiffany Kennedy")
# print(len(records))
# for r in records:
#     print(r.city)
#     print(r.weight)
#     print(r.height)

# records = Resource.objects(height = 172)
# print(len(records))
# for r in records:
#     print(r.name,r.city,sep ="|\t")

# records_height = Resource.objects(height__gt=170)
# print(len(records_height))

find_emily = Resource.objects(name__icontains = "smith", height__lte = 160)
print(len(find_emily))
for r in find_emily:
    print(r.name)
    print("*"*20)

records = Resource.objects()
for r in records:
    r.update(set__available=False) 

s = Resource.obejcts.with_id("5bf80cb9cea0ba4218a86e4d")
s.update(set__available=True)