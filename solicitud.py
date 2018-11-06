import requests, json
class Request:
    def __init__(self):
        self.api_url = 'https://api-cuenta-django.herokuapp.com/'

    def sendRequest(self, endpoint, data = None, type = ""):
        make_request = None
        headers = {'content-type': 'application/json'}
        if(data != None):
            if(type == "POST"):
                make_request = requests.post(self.api_url+endpoint+'/', data=json.dumps(data), headers=headers)
            elif type == "PUT":
                make_request = requests.put(self.api_url+endpoint+'/', data=json.dumps(data), headers=headers)
        else:
            if type == "DEL":
                make_request = requests.delete(self.api_url+endpoint+'/1')
            else:
                make_request = requests.get(self.api_url+endpoint+'/')
        return make_request.content


