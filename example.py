#!/usr/bin/python
#Call this with python3 example.py <url> <client_id> <client_secret>
import sys

from module import Module

from suiteCRMService import SuiteCRMService
from filter import FilterTriplet
from filter import Filter
from filter import Comparison
from filter import Logical

url = sys.argv[1]
webService = SuiteCRMService(url, sys.argv[2], sys.argv[3])

#TODO: Write test cases instead of using this example python script (I know, it is not developed in TDD :( )
print("Get all modules")
response = webService.get_modules()
print ("Result of get modules call: {0}".format(response.json()))

print("Get all fields of a module")
response = webService.get_module_fields(Module.ACCOUNTS)
print ("Result of get all fields of a module call: {0}".format(response.json()))

print("Get data for opportunities")
response = webService.get_data(Module.OPPORTUNITIES)

filterTriplet = FilterTriplet(Comparison.GTE, "probability", "75")
filter = Filter(Logical.AND, [filterTriplet])

response = webService.get_data(Module.OPPORTUNITIES, ["name", "probability"], filter)
print ("Result of opportunities call: {0}".format(response.json()))