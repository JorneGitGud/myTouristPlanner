import json
from time import sleep
from bson import json_util
from kafka import KafkaProducer, KafkaConsumer, TopicPartition
from pprint import pprint


## download jsons
# Creeër topics route voor consumer
# Initialiseer consumer voor de fiets
# Wijs waarden toe nodig om de consumer uit te schakelen wanneer het einde van de messages wordt bereikt
tp = TopicPartition('route',0)
bike_consumer = KafkaConsumer(
    bootstrap_servers="localhost:9092",
    auto_offset_reset='earliest',
    value_deserializer=lambda m:
        json.loads(m.decode('utf-8')))
bike_consumer.assign([tp])
bike_consumer.seek_to_beginning(tp)
lastOffset = bike_consumer.end_offsets([tp])[tp]
try:
    for message in bike_consumer:
        pprint(message)
        if message.offset == lastOffset -1:
            break
except KeyboardInterrupt:
    pass
finally:
    bike_consumer.close()

# with open('output.json', 'w') as json_file:
#     json.dump(value_for_json, json_file)

## laadt jsons
json_roy_object = open('royjson.json')
json_roy_data = json.load(json_roy_object)
json_route_object = open('route.json')
json_route_data = json.load(json_route_object)
print(type(json_route_data))
# Eens voor testen
# producer =KafkaProducer(bootstrap_servers='localhost:9092')
# producer.send('route', json.dumps(json_roy_data, default=json_util.default).encode('utf-8'))

# a -> b -> c
# abc = route als json
# bezienswaardigheden route = abc locaties als json
# bikes, logs, route
# bij bikes, laat ik weten waar ik ben geweest
# bij logs, hetzelfde maar voor altijd
# route krijg ik binnen nadat ik vraag om een route
    # 
#zet producer op KAFKA connectie
bike_producer = KafkaProducer(
    bootstrap_servers="localhost:9092")

BikeId = 354125424
class Bicycle:
    def __init__(self, BikeId, X, Y):
        self.BikeId = BikeId
        self.X = X
        self.Y = Y
    def movement(self, X, Y):
        self.BikeId = BikeId
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
start_locatie_X = json_roy_data['X']
start_locatie_Y = json_roy_data['Y']
bicycle = Bicycle(BikeId=BikeId, X= start_locatie_X, Y=start_locatie_Y)
bicycle_json = json.dumps(bicycle.__dict__)
pprint(bicycle_json)

print("\n\tBegin route")
# route afleggen en locaties printen
for step in json_route_data['locaties']:
    step_X = step['X']
    step_Y = step['Y']
    print("\tsteps: ",step_X, step_Y)
    # stappen worden up to date gebracht en stellen de locatie van de fiets voor
    # bij iedere stap word de locatie van de fiets up to date gebracht
    bicycle.movement(X=step_X, Y=step_Y)
    sleep(3)

    # print("hello")
    locations_here = []
    locations_around = []
    for place in json_roy_data['locaties']:
        place_X = place['X']
        place_Y = place['Y']
        # if statement, creeërt locaties op de huidige locatie
        if (place_X == step_X and place_Y == step_Y):
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
        place_X = place['X']
        place_Y = place['Y']
        print(
            "\t", 
            place_descriptie, " \n\t", 
            place_name, " \n\t",
            place_genre, "\n\tbij coordinaten",
            place_X, place_Y)

print("Te bezoeken plaatsen van uw route:")
for place in json_roy_data['route']:
    place_X = place['X']
    place_Y = place['Y']
    place_descriptie = place['discription']
    place_name = place['name']
    place_genre = place['genre']
    # print(
    #     #"Te bezoeken plaatsen van uw route:\n\t", 
    #     "\t",place_descriptie, " \n\t", 
    #     place_name, " \n\t", 
    #     place_genre, "\n\t\tbij coordinaten",
    #     place_X, " ", place_Y, "\n")