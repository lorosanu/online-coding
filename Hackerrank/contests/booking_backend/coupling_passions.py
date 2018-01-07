import math

def intersection(a, b):
    return [x for x in a if x in b]

def union(a, b):
    return list(set(a).union(b))

def distance_between(point1, point2):
    EARTH_RADIUS = 6371
    point1_latitude, point1_longitude = point1
    point2_latitude, point2_longitude = point2
    
    point1_lat_in_radians  = math.radians(point1_latitude)
    point2_lat_in_radians  = math.radians(point2_latitude)
    point1_long_in_radians = math.radians(point1_longitude)
    point2_long_in_radians = math.radians(point2_longitude)

    return math.acos( math.sin( point1_lat_in_radians ) * math.sin( point2_lat_in_radians ) +
                 math.cos( point1_lat_in_radians ) * math.cos( point2_lat_in_radians ) *
                 math.cos( point2_long_in_radians - point1_long_in_radians) ) * EARTH_RADIUS;

n = int(input().strip())

passions = {}

cities = []
position = {}
activities = {}

for i in range(n):
    data = input().split()
    passions[i] = data[1:]
        
y = int(input().strip())

cities = []
position = {}
activities = {}

for i in range(y):
    data = input().split()
    name = data[0]
    lat = float(data[1])
    log = float(data[2])
    dpassions = data[4:]
    
    cities.append(name)
    position[name] = (lat, log)
    activities[name] = dpassions

if y >= 2 :
    
    podium = {}
    distance = {}

    for i in range(y):        
        for j in range(i+1, y):
            score = 0
            combined_activities = union(activities[cities[i]], activities[cities[j]])

            for member, passion in passions.items():
                match_passion = intersection(combined_activities, passion)
                score += len(match_passion)

            podium[cities[i], cities[j]] = score
            distance[cities[i], cities[j]] = distance_between(position[cities[i]], position[cities[j]])

    max_score = 0
    best_trip = ""

    for trip, score in podium.items() :
        if score > max_score:
            max_score = score
            best_trip = trip
        elif score == max_score:
            if distance[trip] < distance[best_trip]:
                max_score = score
                best_trip = trip

    print(' '.join(sorted(best_trip)))