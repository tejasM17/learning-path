  #                                                       Dictionaries in Python
  
  
  
  # A dictionary in Python is a collection of key-value pairs.Each key in a dictionary is associated with a value, 
  # and you can retrieve or manipulate data using the key.
  # Unlike lists and tuples, dictionaries are unordered and mutable (changeable).
  
  
  
  
  #                                                     Dictionary Characteristics
  
#Unordered: Dictionary keys are not stored in any particular order.
#Mutable: You can change, add, or remove items.
#Keys Must Be Immutable: Keys in a dictionary must be of a data type that is immutable, such as a string, number, or tuple.
#Unique Keys: A dictionary cannot have duplicate keys. If you try to add a duplicate key, the latest value will overwrite the previous one.
  
  
  
  

#Syntax:


 
fav_car = {
  # key    :  valu
    "germen": "///M",
    "germen1": "BMW",
    "germen2": "bmw-m4"
}

print((fav_car))

# Dictionary Length

print(len(fav_car))




#                          2 .     Accessing Dictionary Elements


#  The values in dictionary items can be of any data type:

dic = {
  "brand":   "Brand         :           ///M",
  "electric":"electtric     :           False",
  "drift":   "Drift         :           100%",
  "year" :   "since         :           1916",
  "friends": ["BMW", "Bugatti","Lambo"]
}



print(dic["brand"])
print(dic["electric"])
print(dic["drift"])
print(dic["year"])


#  You can also use the get() method to access values, which is safer because it doesn’t throw an error if the key doesn’t exist

g = (dic.get("RR","Will be provoided"))
print(g)

print(dic["brand"])

# The keys() method will return a list of all the keys in the dictionary

a = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print( a.keys())


# The values() method will return a list of all the values in the dictionary
print(dic.keys())
print(dic.values())






#                                            Add a new item to the original dictionary



car = {
 "brand": "BMW",
  "model": "///M4",
  "year": "25/9/2013"
}

x = car
print(x) #before the change

print("after adding")

car["color"] = "Blue"
print(x) #after the change
print(car)





#                                3.    Adding and Updating Dictionary Elements

print("after updating...." )
car["color"] = "Black"
print(car)



#    Direct updating

print("befor editing date")
print(car["year"])
print("after editing date")
car["year"] = "27/9/1916"
print(car["year"])





#                            4.   Removing Elements from a Dictionary


d1 = {
  "c1" : "tesla",
  "c2" : "bmw",
  "c3" : "mercedece",
  "c4" : "bhagata",
  "c5" : "ferrirrreree"
}

print("before pop ")
print(d1)
print("after pop")


# pop(): Removes the specified key and returns the associated value

a = d1.pop("c1")
print(d1)
print("pop eliment is")
print(a)
#  del: Removes the specified key

del d1["c5"]
print(d1)


#   clear(): Empties the dictionary

d1.clear()
print(d1)




#                                   5.     Dictionary Methods



brobirthday =  {
  "raju" : "21/6/2004",
  "chidu" : "28/10/2004",
  "moni" : "27/4/2007",
  "sharath" : "26/3/2006",
  "tejas" : "27/9/2006"
}


#     keys(): Returns all the keys in the dictionary.

print(brobirthday.keys())   #output:   dict_keys(['raju', 'chidu', 'moni', 'sharath', 'tejas'])

#     values(): Returns all the values in the dictionary

print(brobirthday.values())    #output: dict_values(['21/6/2004', '28/10/2004', '27/4/2007', '26/3/2006', '27/9/2006'])

#     items(): Returns key-value pairs as tuples

print(brobirthday.items())   # output: dict_items([('raju', '21/6/2004'), ('chidu', '28/10/2004'), ('moni', '27/4/2007'), ('sharath', '26/3/2006'), ('tejas', '27/9/2006')])

#    update(): Updates the dictionary with another dictionary or iterable.

day =  {
  "raju" : "21/6/2004",
  "chidu" : "28/10/2004",
  "moni" : "27/4/2007",
  "sharath" : "26/3/2006",
  "tejas" : "27/9/2006"
}

d1 = {
  "c1" : "tesla",
  "c2" : "bmw",
  "c3" : "mercedece",
  "c4" : "bhagata",
  "c5" : "ferrirrreree"
}


day.update(d1)

print(day)


#   we can make multiple data type of keys and valuse inside dictinory

can = {
  "tejas" : "am a python devolopper",
  123  :"okay",
  "abc" : 9380,
  "is" : True,
  (tuple) : "why",
  #[list] : False,  --->  we can't use yake andre list na navu change madbavdu andre adu mutable, adre dictionary keys must be  unchangeable
  616 : 999,
  "brothers" : ["raju","chiduu","moni","sharath"]
}
print(can)


#  LIST OFF DICTS


l1 = {
  "n" : "car",
  "no" : 2,
  "model" : "BMW"
}

l2 = {
  "n" : "car",
  "no" : 4,
  "model" : "RR"
}


items = [l1, l2]
print(items)

print(f"total no: {l1["no"] + l2["no"]} no. of cars")

