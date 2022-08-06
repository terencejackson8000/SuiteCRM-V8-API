from .module import Module
import requests
import json

# SuiteCRM Web Service class to interact with the SuiteCRM v8 API
class SuiteCRMService:

    PARAMETER_MUST_NOT_BE_NONE = "Parameter {0} must not be None"
    PARAMETER_MUST_BE_OF_TYPE = "Parameter {0} must be of type {1}"
    
    #Constructor for the WebService. Gets the access token with the given clientId and clientSecret
    #Parameters
    #----------
    #host : string
    #    The host url of the service
    #client_id : string
    #    The client id for the authentication
    #client_secret : string
    #    The client secret for the authentication
    def __init__(self, host, client_id, client_secret):
        if host == None or host == "":
            
            raise TypeError(self.PARAMETER_MUST_NOT_BE_NONE.format("host"))
        if client_id == None or client_id == "":
            raise TypeError(self.PARAMETER_MUST_NOT_BE_NONE.format("client_id"))
        if client_secret == None or client_secret == "":
            raise TypeError(self.PARAMETER_MUST_NOT_BE_NONE.format("client_secret"))

        self._host = host
        self._auth_header = self._get_auth_header(client_id, client_secret)
        self._auth_header['Content-type'] = 'application/vnd.api+json'

    #Get the authorization token and create and authentication header
    #Parameters
    #----------
    #client_id : string
    #    The client id for the authentication
    #client_secret : string
    #    The client secret for the authentication
    def _get_auth_header(self, client_id, client_secret) -> dict:
        body = {"grant_type": "client_credentials","client_id": client_id,"client_secret": client_secret}
        response = requests.post("{0}/Api/access_token".format(self._host), data = body)
        if(response.status_code == 200):
            access_token = response.json().get("access_token")
            return {'Authorization': 'Bearer {0}'.format(access_token)}
        else:
            raise RuntimeError("Not able to get token {0}".format(response.text))
    
    #Get all available modules
    def get_modules(self) -> requests.Response:
        return requests.get("{0}/Api/V8/meta/modules".format(self._host), headers=self._auth_header)

    #Get fields for a certain module
    #Parameters
    #----------
    #module : Module
    #    The module you want to get the data for. 
    def get_module_fields(self, module) -> requests.Response:
        if module is None:
            raise TypeError(self.PARAMETER_MUST_NOT_BE_NONE.format("module"))
        if not isinstance(module, Module):
            raise TypeError(self.PARAMETER_MUST_BE_OF_TYPE.format("module", "enum Module"))

        return requests.get("{0}/Api/V8/meta/fields/{1}".format(self._host, module.value), headers=self._auth_header)

    #get data for a certain module
    #Parameters
    #----------
    #module : Module
    #    The module you want to get the data for. 
    #fields : list
    #   The fields to be returned. If None then all fields will be returned.
    #filter : Filter
    #    The filter you want ot set. Default is None
    #pagination: Pagination
    #   The pagination settings to be set. Default page size is 50
    def get_data(self, module, fields=None, filter=None, pagination=None) -> requests.Response:
        if module is None:
            raise TypeError(self.PARAMETER_MUST_NOT_BE_NONE.format("module"))
        if not isinstance(module, Module):
            raise TypeError(self.PARAMETER_MUST_BE_OF_TYPE.format("module", "enum Module"))

        seperator = ","
        
        if module != None and type(fields) == list and len(fields) > 0:
            fields = "fields[{0}]={1}".format(module.value, seperator.join(fields))
            
        response = requests.get("{0}/Api/V8/module/{1}{2}".format(self._host, module.value, self._build_query_params(fields, filter, pagination)), headers=self._auth_header)
        return response
    
    #get relationship data for a certain module
    #Parameters
    #----------
    #module : Module
    #    The module you want to get the data for. 
    #id: str
    #   The ID of the object to get the relationship for
    #relationship : Module
    #    The relationship module to get the data for. (e.g. CONTACTS for contacts of an OPPORTUNITY)
    #fields : list
    #   The fields to be returned. If None then all fields will be returned.
    #filter : Filter
    #    The filter you want ot set. Default is None
    #pagination: Pagination
    #   The pagination settings to be set. Default page size is 50
    def get_relationship_data(self, module, id, relationship, fields=None, filter=None, pagination=None) -> requests.Response:
        if module is None:
            raise TypeError(self.PARAMETER_MUST_NOT_BE_NONE.format("module"))
        if not isinstance(module, Module):
            raise TypeError(self.PARAMETER_MUST_BE_OF_TYPE.format("module", "enum Module"))

        seperator = ","
        
        if module != None and type(fields) == list and len(fields) > 0:
            fields = "fields[{0}]={1}".format(module.value, seperator.join(fields))
            
        response = requests.get("{0}/Api/V8/module/{1}/{2}/relationships/{3}{4}".format(self._host, module.value, id, relationship.value.lower(), self._build_query_params(fields, filter, pagination)), headers=self._auth_header)
        return response
    
    #Insert a record
    #Parameters
    #----------
    #module : Module
    #    The module you want to get the data for. 
    #attributes : dict[str, object]
    #    The attributes to be updated
    def insert_data(self, module, attributes) -> requests.Response:
        if module is None:
            raise TypeError(self.PARAMETER_MUST_NOT_BE_NONE.format("module"))
        if not isinstance(module, Module):
            raise TypeError(self.PARAMETER_MUST_BE_OF_TYPE.format("module", "enum Module"))
        if attributes is None:
            raise TypeError(self.PARAMETER_MUST_NOT_BE_NONE.format("attributes"))
        if not isinstance(attributes, dict):
            raise TypeError(self.PARAMETER_MUST_BE_OF_TYPE.format("attributes", "dict"))
        
        body = {'data': { 'type': module.name.lower().capitalize(), 'attributes': attributes}}
        json_data = json.dumps(body, default=lambda o: o.__dict__, sort_keys=False)
        return requests.post('{0}/Api/V8/module'.format(self._host), data = json_data, headers=self._auth_header)
    
    #Update a record
    #Parameters
    #----------
    #module : Module
    #    The module you want to get the data for. 
    #id : string
    #   The if of the object to be changed
    #attributes : dict[str, object]
    #    The attributes to be updated
    def update_data(self, module, id, attributes) -> requests.Response:
        if module is None:
            raise TypeError(self.PARAMETER_MUST_NOT_BE_NONE.format("module"))
        if not isinstance(module, Module):
            raise TypeError(self.PARAMETER_MUST_BE_OF_TYPE.format("module", "enum Module"))
        if id is None or id == "":
            raise TypeError(self.PARAMETER_MUST_NOT_BE_NONE.format("id"))
        if attributes is None:
            raise TypeError(self.PARAMETER_MUST_NOT_BE_NONE.format("attributes"))
        if not isinstance(attributes, dict):
            raise TypeError(self.PARAMETER_MUST_BE_OF_TYPE.format("attributes", "dict"))
                    
        body = {'data': { 'type': module.name.lower().capitalize(), 'id': id, 'attributes': attributes}}
        json_data = json.dumps(body, default=lambda o: o.__dict__, sort_keys=False)
        return requests.patch('{0}/Api/V8/module'.format(self._host), data = json_data, headers=self._auth_header)

    #Get data by a given id
    #Parameters
    #----------
    #module : string
    #    The name of the module you want to get the data for. You can use the constants defined in constants.py
    #id : string
    #    The if of the data (object) to get
    #fields : list
    #   The fields to be returned. If None then all fields will be returned.
    def get_data_by_id(self, module, id, fields=None) -> requests.Response:
        if module is None:
            raise TypeError(self.PARAMETER_MUST_NOT_BE_NONE.format("module"))
        if not isinstance(module, Module):
            raise TypeError(self.PARAMETER_MUST_BE_OF_TYPE.format("module", "enum Module"))
        if id is None:
            raise TypeError(self.PARAMETER_MUST_NOT_BE_NONE.format("id"))

        seperator = ","
        
        if module != None and type(fields) == list and len(fields) > 0:
            fields = "fields[{0}]={1}".format(module.value, seperator.join(fields))
            
        response = requests.get("{0}/Api/V8/module/{1}/{2}{3}".
                    format(self._host, module.value, id, self._build_query_params(fields, None, None)), 
                    headers=self._auth_header)
        return response
    
    #Build the query parameters to be appended to the API call
    #Parameters
    #----------
    #fields : list
    #   The fields to be returned. If None then all fields will be returned.
    #filter : Filter
    #    The filter you want ot set. Default is None
    #pagination: Pagination
    #   The pagination settings to be set. Default page size is 50
    def _build_query_params(self, fields, filter, pagination) -> str:
        connectors = ["?", "&"]
        query_string = ""
        connector_index = 0

        if fields != None and len(fields) > 0:
            query_string += "{0}{1}".format(connectors[connector_index], fields)
            connector_index = 1
        
        if filter != None:
            query_string += "{0}{1}".format(connectors[connector_index], filter.to_filter_string())
            connector_index = 1

        if pagination != None:
            if pagination.page_number != None:
                pages = "page[number]={0}&page[size]={1}".format(pagination.page_number, pagination.page_size)
            else:
                pages = "page[size]={0}".format(pagination.page_size)
            
            query_string += "{0}{1}".format(connectors[connector_index], pages)
            connector_index = 1

        return query_string