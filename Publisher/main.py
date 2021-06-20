# pip install python-kafka
# pip install pandas
# pip install numpy
# pip install requests
# pip install pprintjson

# inport
import json
from kafka import KafkaConsumer,KafkaProducer
import requests
import pandas as pd 
import numpy as np
from pprint import pprint


# create bike class
class BikeRoute:
      def __init__(self, BikeId , X, Y , route, locations):
            self.BikeId = BikeId
            self.X = X
            self.Y = Y
            self.route = route
            self.locations = locations

# setup producer
producer = KafkaProducer(bootstrap_servers='localhost:9092',value_serializer=str.encode)
bootstrap_servers = ['localhost:9092']
topicName = 'bikes'
producer = KafkaProducer(bootstrap_servers = bootstrap_servers)
producer = KafkaProducer()

#kafka consumer
bootstrap_servers = ['localhost:9092']
consumer = KafkaConsumer (topicName,bootstrap_servers = bootstrap_servers,auto_offset_reset = 'latest')

#checking bike messages
for message in consumer:
    message = json.loads(message.value.decode('utf-8'));
    
    # initialize the bike id
    id = message['BikeId']

    # initialize location of the bike
    X = message['X']
    Y = message['Y']

    #get locations from the API
    r = requests.get(url='http://localhost:5000/places')

    #get the places objects
    jsonObjects = r.json()

    #create dataframe
    df = pd.DataFrame (jsonObjects)



      
    #distance calculator
    df['location'] = X * Y
    df['weight'] = df['X'] * df['Y']    

    #giving distance "weigth" to calculate from root
    df['distance'] = np.where(df['location']> df['weight'], df['location'] - df['weight'] ,df['weight'] - df['location'])

    # making boolean series for a team name
#     filter = df["status"]=="open"
    
    # filtering data
#     df.where(filter, inplace = True)

    print(df)
    # sort on distance
    df = df.sort_values(by=['distance'])

    print(df)

    df.drop(['distance'], axis=1, inplace=True)
    df.drop(['weight'], axis=1, inplace=True)
    df.drop(['location'], axis=1, inplace=True)
    # df.drop(['__id'], axis=1, inplace=True)




    # dataframe to json format
    routeArray = df.head(1).to_json(orient='records')

    
    locationArray = df.head(3).to_json(orient='records')

    # convert to json 
    ra = json.loads(routeArray)
    la = json.loads(locationArray)
    
    # new Bike object
    current = BikeRoute(id,X,Y,ra,la)
    # route object from bike json format
    bikeRoute = json.dumps(current.__dict__)

    print(bikeRoute)
    pprint(json.loads(bikeRoute))
    
    #send bike, route and locations to route topic
    producer.send('route',bikeRoute.encode('utf-8'))



