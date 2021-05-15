from module import Module
import requests

class SuiteCRMService:

    #Constructor for the WebService. Gets the access token with the given clientId and clientSecret
    def __init__(self, host, client_id, client_secret):
        self._host = host
        body = {"grant_type": "client_credentials","client_id": client_id,"client_secret": client_secret}
        response = requests.post("{0}/Api/access_token".format(self._host), data = body)
        if(response.status_code == 200):
            access_token = response.json().get("access_token")
            self._headersAuth = {'Authorization': 'Bearer {0}'.format(access_token)}

    #get data for a certain module
    #Parameters
    #----------
    #module : string
    #    The name of the module you want to get the data for. You can use the constants defined in constants.py
    #fields : list
    #   The fields to be returned. If None then all fields will be returned.
    #filter : array
    #    The filter you want ot set. Default is None
    def get_data(self, module, fields=None, filter=None):
        if module is None:
            raise TypeError("Parameter module cannot be None")
        if not isinstance(module, Module):
            raise TypeError("Parameter module must be of type enum Module")

        seperator = ","
        
        if module != None and type(fields) == list and len(fields) > 0:
            fields = "fields[{0}]={1}".format(module.value, seperator.join(fields))
            
        response = requests.get("{0}/Api/V8/module/{1}{2}".format(self._host, module.value, self._build_query_params(fields, filter)), headers=self._headersAuth)
        return response
    
    def _build_query_params(self, fields, filter):
        connectors = ["?", "&"]
        query_string = ""
        connector_index = 0

        if fields != None and len(fields) > 0:
            query_string += "{0}{1}".format(connectors[connector_index], fields)
            connector_index = 1
        
        if filter != None:
            query_string += "{0}{1}".format(connectors[connector_index], filter.to_filter_string())
            connector_index = 1
        
        return query_string

    #Get all available modules
    def get_modules(self):
        return requests.get("{0}/Api/V8/meta/modules".format(self._host), headers=self._headersAuth)