import json

person = {"name": "John", "age": 30, "city": "New York", "children": False, "titles": ["engineer", "programmer"]}

# changing from python dictionary tojson in terminal
personJSON = json.dumps(person, indent = 4, sort_keys = True)
print(personJSON)

# opening new json file and changind python dictionary to json
with open('person.json', 'w') as file:
    json.dump(person, file, indent = 4, sort_keys = True)

# changing back from json to python
person = json.loads(personJSON)
print(person)