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
    #filter : array
    #    The filter you want ot set. Default is None
    def get_data(self, module, filter=None):
        if module is None:
            raise TypeError("Parameter module cannot be None")
        
        response = requests.get("{0}/Api/V8/module/{1}".format(self._host, module), headers=self._headersAuth)
        print(response.json())

    #Get all available modules
    def get_modules(self):
        return requests.get("{0}/Api/V8/meta/modules".format(self._host), headers=self._headersAuth)