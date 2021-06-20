# topics:
# bikes
    # _id: ObjectId("")
    # BikeId: 1
    # X: 1
    # Y: 2
    # __v: 0
# logs
    # _id: ObjectId("")
    # BikeId: 1
    # Time: datetime
    # X: 1
    # Y: 2
    # __v: 0
# places:
    # _id: ObjectId("")
    # Name: "b&w"
    # Info: "This is a fun place"
    # Genre: "Coffee Place"
    # X: 1
    # Y: 2
    # __v: 0
import json
from time import sleep
from bson import json_util
from kafka import KafkaProducer, KafkaConsumer, KafkaClient

# producer = KafkaProducer(bootstrap_servers= 'localhost:9092')
# for i in range(10):
#     data = { 'tag ': 'blah',
#         'name' : 'sam',
#         'index' : i,
#         'score': 
#             {'row1': 100,
#              'row2': 200
#         }
#     }   
#     producer.send('orders', json.dumps(data, default=json_util.default).encode('utf-8'))


from pprint import pprint
class Bicycle:
    def __init__(self, bike_id, time, x, y):
        self.bike_id = bike_id
        self.time = time
        self.x = x
        self.y = y
    def movement(self, x, y):
        self.x = x
        self.y = y
# testing variables
tv_bike_id = 1
tv_time = 11
tv_x = 1
tv_y = 2

bicycle = Bicycle(bike_id=tv_bike_id, time=tv_time, x= tv_x, y=tv_y)
bicycle_json = json.dumps(bicycle.__dict__)
pprint(bicycle_json)

bicycle.movement(x=2, y=2)
bicycle_json = json.dumps(bicycle.__dict__)
pprint(bicycle_json)

json_route_object = open('route.json')
json_route_data = json.load(json_route_object)
print(type(json_route_data))

# test lengte van json simulatie bestand
#route_len = len(json_route_data[0]['locaties'])
# print(len(json_route_data[0]['locaties']))

print("\n\tBegin route")
# step is een [Integer] van het json bestand
for step in json_route_data['locaties']:
    step_x = step['X']
    step_y = step['Y']
    print()
    print("steps: ",step_x, step_y)
    bicycle.movement(x=step_x, y=step_y)

    bicycle_json = json.dumps(bicycle.__dict__)
    pprint(bicycle_json)
    #print(bicycle)
    # time.sleep(1)
    # print("hello")


json_places_object = open('test_places.json')
json_places_data = json.load(json_places_object)

class Places:
    def __init__(self, name, info, genre, X, Y):
        self.name = name
        self.info = info
        self.genre = genre
        self.X = X
        self.Y = Y

place = Places(
    name="b&w", 
    info="This is a fun place", 
    genre="Coffee Place", 
    X=1,
    Y=2)
place2 = Places(
    name="b", 
    info="This place", 
    genre="Coffee", 
    X=1,
    Y=2)

class Mappoints:
    def __init__(self, list_places, X, Y):
        self.list_places = list_places
        self.X = X
        self.Y = Y
    def read_mappoint(self, list_places):
        for location in list_places:
            print("\n\tOp uw locatie is een punt van interesse")
            print("\t\t",location.name)
            print("\t\t",location.info)
            print("\t\t",location.genre)
            print("\t\t",location.X)
            print("\t\t",location.Y)


            

json_roy_object = open('royjson.json')
json_roy_data = json.load(json_roy_object)
# route afleggen en locaties printen
for step in json_route_data['locaties']:
    step_x = step['X']
    step_y = step['Y']
    print()
    print("steps: ",step_x, step_y)
    bicycle.movement(x=step_x, y=step_y)

    bicycle_json = json.dumps(bicycle.__dict__)
    pprint(bicycle_json)
    #print(bicycle)
    # time.sleep(1)
    # print("hello")

    for place in json_roy_data['locaties']:
        place_x = place['x']
        place_y = place['y']
        if (place_x == step_x and place_y == step_y):
            place_descriptie = place['discription']
            place_name = place['name']
            place_genre = place['genre']
            print()
            print(
                "Te bezoeken plaatsen waar u nu bent:\n\t",  
                place_descriptie, " ", 
                place_name, " ",
                place_genre)
        else:
            place_descriptie = place['discription']
            place_name = place['name']
            place_genre = place['genre']
            print()
            print(
                "plaatsen op uw route:\n\t", 
                place_descriptie, " ", 
                place_name, " ",
                place_genre, "\n\tbij coordinaten",
                place_x, place_y)
for place in json_roy_data['route']:
    place_x = place['x']
    place_y = place['y']
    place_descriptie = place['discription']
    place_name = place['name']
    place_genre = place['genre']
    print()
    print(
        "Te bezoeken plaatsen van uw route:\n\t", 
        place_descriptie, " ", 
        place_name, " ", 
        place_genre, "\n\tbij coordinaten",
        place_x, " ", place_y)