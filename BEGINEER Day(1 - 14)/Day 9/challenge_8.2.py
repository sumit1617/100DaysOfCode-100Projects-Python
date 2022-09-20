travel_log = [
    {
        "State" : "Maharashtra", 
        "cities":["Mumbai","Pune","Ratnagiri"],
        "visits" : 12
    },
    {
        "State" : "UP", 
        "cities":["Varanasi","Kanpur","Lucknow"],
        "visits": 6
    },
]

def add_new_country(state_visited, cities_visited, times_visited):
    new_state = {}
    new_state["state"] = state_visited
    new_state["cities"] = cities_visited
    new_state["visits"] = times_visited
    travel_log.append(new_state)

add_new_country("Gujarat",["Surat","Ahemdabad","Rajkot"], 10)
print(travel_log)
