import json
from time import sleep
from bson import json_util
from kafka import KafkaProducer, KafkaConsumer, KafkaClient
from pprint import pprint

## download jsons
bike_consumer = KafkaConsumer(
    '',
    bootstrap_servers="localhost:9092"
)
## laadt jsons
json_roy_object = open('royjson.json')
json_roy_data = json.load(json_roy_object)

json_route_object = open('route.json')
json_route_data = json.load(json_route_object)

#zet producer op KAFKA connectie
bike_producer = KafkaProducer(
    bootstrap_servers="localhost:9092")

bike_id = "LAnc3Armstr0ng"
class Bicycle:
    def __init__(self, bike_id, X, Y):
        self.bike_id = bike_id
        self.X = X
        self.Y = Y
    def movement(self, X, Y):
        self.X = X
        self.Y = Y
        bike_producer.send(
            "bikes", 
            json.dumps(self.__dict__, default=json_util.default).encode('utf-8'))
        # pretty print en breakpoint voor testen
        #pprint(self.__dict__)
        #breakpoint()


## Initieër json imports voordat je hier bent gekomen
# Start locatie halen we uit een route bestand
# bicycle
start_locatie_x = json_roy_data['x']
start_locatie_y = json_roy_data['y']
bicycle = Bicycle(bike_id=bike_id, X= start_locatie_x, Y=start_locatie_y)
bicycle_json = json.dumps(bicycle.__dict__)
pprint(bicycle_json)

print("\n\tBegin route")
# route afleggen en locaties printen
for step in json_route_data['locaties']:
    step_x = step['X']
    step_y = step['Y']
    print("\tsteps: ",step_x, step_y)
    # stappen worden up to date gebracht en stellen de locatie van de fiets voor
    # bij iedere stap word de locatie van de fiets up to date gebracht
    bicycle.movement(X=step_x, Y=step_y)
    bicycle_json = json.dumps(bicycle.__dict__)

    sleep(1)
    # print("hello")
    locations_here = []
    locations_around = []
    for place in json_roy_data['locaties']:
        place_x = place['x']
        place_y = place['y']
        # if statement, creeërt locaties op de huidige locatie
        if (place_x == step_x and place_y == step_y):
            locations_here.append(place)
        # else statement, creeërt locaties die worden gelezen uit de gegeven route
        else:
            locations_around.append(place)
    print("Te bezoeken plaatsen waar u nu bent:\n\t")  
    for place in locations_here:
        place_descriptie = place['discription']
        place_name = place['name']
        place_genre = place['genre']
        print(
            place_descriptie, " \n\t", 
            place_name, " \n\t",
            place_genre)
    print("plaatsen op uw route:")
    for place in locations_around:
        place_descriptie = place['discription']
        place_name = place['name']
        place_genre = place['genre']
        place_x = place['x']
        place_y = place['y']
        print(
            "\t", 
            place_descriptie, " \n\t", 
            place_name, " \n\t",
            place_genre, "\n\tbij coordinaten",
            place_x, place_y)

print("Te bezoeken plaatsen van uw route:")
for place in json_roy_data['route']:
    place_x = place['x']
    place_y = place['y']
    place_descriptie = place['discription']
    place_name = place['name']
    place_genre = place['genre']
    # print(
    #     #"Te bezoeken plaatsen van uw route:\n\t", 
    #     "\t",place_descriptie, " \n\t", 
    #     place_name, " \n\t", 
    #     place_genre, "\n\t\tbij coordinaten",
    #     place_x, " ", place_y, "\n")