import argparse
#import json
import requests

# parser = argparse.ArgumentParser(description='Parser of arguments a, b & c from ax^2 + bx + c')
# parser.add_argument("--a")
# parser.add_argument("--b")
# parser.add_argument("--c")

# args = parser.parse_args()

a = 1
b = 2
c = -3

params = {'a': a, 'b': b, 'c': c}
response = requests.get('http://192.168.77.77:8000/solver/', params=params)
jsonDict = response.json()

if (jsonDict["x1"] == 'Negative Discriminant'):
    print('Negative Discriminant')
else:
    print(f'x1: {jsonDict["x1"]}, x2: {jsonDict["x2"]}')
