class Bike:
      def __init__(self, id , x, y):
            self.id = id
            self.x = x
            self.y = y



# new Bike object
thisBike = Bike(1,100,300)

#set new values -- location changing--
thisBike.x = 111
thisBike.y = 222

#convert to JSON string
jsonStr = json.dumps(thisBike.__dict__)

#print jsonstring
print(json.dumps(jsonStr))