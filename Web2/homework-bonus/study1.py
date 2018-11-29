#Convert a string to dictionary in JSON
import json
h = '{"foo":"bar", "foo2":"bar2"}'
print(type(h))
d = json.loads(h)
print(type(d))
# References:
# https://developer.rhino3d.com/guides/rhinopython/python-xml-json/
# https://pythonspot.com/json-encoding-and-decoding-with-python/
