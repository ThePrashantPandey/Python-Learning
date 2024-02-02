import json

x ={
    "name" : "prashant",
    "age" : 21,
    "married" : False,
    "divorced" : False,
    "children" : None,
    "pets" : None,
    "cars" : [
        {"model" : "BMW 230", "mpg" : 27.5},
        {"model" : "Ford Edge", "mpg" : 24.1}
    ]
}
print (json.dumps(x))
