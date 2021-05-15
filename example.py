#!/usr/bin/python

import sys

import constant

from suiteCRMService import SuiteCRMService
from filter import FilterTriplet
from filter import Filter

url = sys.argv[1]
webService = SuiteCRMService(url, sys.argv[2], sys.argv[3])

response = webService.get_data(constant.OPPORTUNITIES)

filterTriplet = FilterTriplet("GTE", "probability", "75")
filter = Filter("and", [filterTriplet])

response = webService.get_data(constant.OPPORTUNITIES, ["name", "probability"], filter)
print (response.json())