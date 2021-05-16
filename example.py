#!/usr/bin/python
#Call this with python3 example.py <url> <client_id> <client_secret>
import sys

from .module import Module

from .suiteCRMService import SuiteCRMService
from .filter import FilterTriplet
from .filter import Filter
from .filter import Comparison
from .filter import Logical

url = sys.argv[1]
webService = SuiteCRMService(url, sys.argv[2], sys.argv[3])

response = webService.get_data(Module.OPPORTUNITIES)

filterTriplet = FilterTriplet(Comparison.GTE, "probability", "75")
filter = Filter(Logical.AND, [filterTriplet])

response = webService.get_data(Module.OPPORTUNITIES, ["name", "probability"], filter)
print (response.json())