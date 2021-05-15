#!/usr/bin/python

import sys

import constant

from suiteCRMService import SuiteCRMService

url = sys.argv[1]
webService = SuiteCRMService(url, sys.argv[2], sys.argv[3])

response = webService.get_data(constant.OPPORTUNITIES)