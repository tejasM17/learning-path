#Create a dictionary to store details of your favorite food items, including their names and dishes.


dishes = {
    "hydrabad" : "biriyani",
    "karnataka" : "ragi mudde" ,
    "maharashtra" : "pav bhaji",
    "kerala" : "appam",
    "tamilnadu" : "idli",  
}

dishes ["tiptur"] = "tenginakai" # adding new dish to the dictionary

dishes["manjunatha nagara"] = "dosa" # update

print(dishes)

del dishes["kerala"] # delete the dish from the dictionary

print(dishes)

print(dishes.keys()) # print the keys of the dictionary
print(dishes.values()) # print the values of the dictionary


# create a nested dictionary to store details of your friends, including their names, favorite car, and favorite food.

dit = {
    "frd1" : {
    "name" : "teju",
    "car" : "BMW",
    "fav_food" : "biriyani"
},
    "frd2 ": {
    "name" : "raju",
    "car" : "bugatti",
    "fav_food" : "chiken sambar"
}
    
}

t = dit["frd1"]            # access the 1st dictionary
t["status"] = "perfect human"
print(t)                # print the 1st dictionary
print(t["fav_food"])   # print the fav_food of the 1st dictionary

# or

print(dit["frd1"]["fav_food"])       # print the fav_food of the 1st dictionary alsowe can access the dictionary in this way
