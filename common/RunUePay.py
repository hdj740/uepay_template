import requests
import json

class ulit:

    def PostRequests(self,url,data):
        requests.post(url=url, data=json.loads(data))

    def GetRequests(self):
        pass

    def RequestType(self):
        pass