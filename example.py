#!/usr/bin/python

import sys

import constant

from suiteCRMService import SuiteCRMService

url = sys.argv[1]
webService = SuiteCRMService(url, sys.argv[2], sys.argv[3])

response = webService.get_data(constant.OPPORTUNITIES)

response = webService.get_data(constant.OPPORTUNITIES, ["pm_b1_b_c", "pm_b2_b_c"])
#print (response.json())