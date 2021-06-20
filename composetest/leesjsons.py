import json
# laadt places.json
json_places_object = open('test_places.json')
json_places_data = json.load(json_places_object)
# presenteer places.json
for place in json_places_data['locaties']:
    place_descriptie = place['descriptie']
    place_name = place['name']
    place_genre = place['genre']
    place_x = place['X']
    place_y = place['Y']
    print()
    print("plaatsen: ", place_descriptie, " ", place_name)


# laadt route.json
json_route_object = open('route.json')
json_route_data = json.load(json_route_object)
print(type(json_route_data))
# volg route.json
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


# combinatie van 
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

    for place in json_places_data['locaties']:
        place_x = place['X']
        place_y = place['Y']
        if (place_x == step_x and place_y == step_y):
            place_descriptie = place['descriptie']
            place_name = place['name']
            place_genre = place['genre']
            print()
            print("plaatsen op uw locatie: ", place_descriptie, " ", place_name)
        else:
            place_descriptie = place['descriptie']
            place_name = place['name']
            place_genre = place['genre']
            print()
            print("plaatsen op uw route: ", place_descriptie, " ", place_name)