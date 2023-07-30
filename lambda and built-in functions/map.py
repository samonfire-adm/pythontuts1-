x= [
    {"first": "Sameer", "last" : "Dey"},
    {"first": "Arpit", "last" : "Rathore"},
    {"first": "Shobhit", "last" : "Kumar"}
]

y = list(map(lambda z : z["first"], x))
print(y)