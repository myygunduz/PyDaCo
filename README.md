# PyDaCo

![alt text](https://github.com/myygunduz/PyDaCo/blob/main/image.png?raw=true)

![Python](https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white) ![Version](https://img.shields.io/static/v1?label=Version&message=0.1.1&style=for-the-badge&labelColor=4B8BBE&color=FFE873&logo=python&logoColor=ffffff) ![LICENSE](https://img.shields.io/static/v1?label=LICENSE&message=MIT&style=for-the-badge)
## Description

PyDaCo is a Python package for easy use of dictionaries and lists.

## Installation

```bash
pip install pydaco
```

or 

```bash
python -m pip install pydaco
```

## Usage

```python
from PyDaCO import pydaco as pdc

pdc.add('name', 'John')
pdc.add('age', 25)
pdc.add('address', {'street': 'Main Street', 'number': 123})
pdc.add('friends', ['Peter', 'Mary', 'Jane'])

print(pdc) # Output: {'name': 'John', 'age': 25, 'address': {'street': 'Main Street', 'number': 123}, 'friends': ['Peter', 'Mary', 'Jane']}
print(pdc['name']) # Output: John
print(pdc['age']) # Output: 25
print(pdc['address']) # Output: {'street': 'Main Street', 'number': 123}
print(pdc['address']['street']) # Output: Main Street
print(pdc['friends']) # Output: ['Peter', 'Mary', 'Jane']
print(pdc['friends'][0]) # Output: Peter
pdc['friends'][0] = 'Peter Parker'
print(pdc['friends'][0]) # Output: Peter Parker

#or

pdc.name = 'John'
pdc.age = 25
pdc.address = {'street': 'Main Street', 'number': 123}
pdc.friends = ['Peter', 'Mary', 'Jane']

print(pdc) # Output: {'name': 'John', 'age': 25, 'address': {'street': 'Main Street', 'number': 123}, 'friends': ['Peter', 'Mary', 'Jane']}
print(pdc.name) # Output: John
print(pdc.age) # Output: 25
print(pdc.address) # Output: {'street': 'Main Street', 'number': 123}
print(pdc.address.street) # Output: Main Street
print(pdc.friends) # Output: ['Peter', 'Mary', 'Jane']
print(pdc.friends[0]) # Output: Peter
pdc.friends[0] = 'Peter Parker'
print(pdc.friends[0]) # Output: Peter Parker
```

## Methods

### `add(key, value)`

Adds a key and value to the dictionary.

### `clear()`

Clears the dictionary.

### `del`

Deletes a key and value from the dictionary.
```python
del pdc['name']
#or
del pdc.name
```


## License

[MIT](https://github.com/myygunduz/PyDaCo/blob/main/LICENSE)