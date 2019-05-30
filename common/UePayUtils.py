#!/usr/bin/python
# -*- coding: utf-8 -*-
import json

class Utils:
    def extract_arguments(self,date = None):
        arguments = date["arguments"]
        return arguments

    def del_clientSign(self,data):
        print("dataE:sdjflkdsjfkjdsahfhsd",date)
        data.pop("clientSign")
        return date

if __name__ == "__main__":
    date = {
        "arguments": {
            "handleType": "1",
            "userId": "196",
            "token": "MTIzNDU2Nzg5LDE3OSwyOWFkMGUzZmQzZGI2ODFmYjlmODA5MWM3NTYzMTNm NywxNTUwNzU1NjY0MDkzLGlvcw==",
            "clientSign": "0ead59fd308773cf9fa74766907e3d1b"
        },
        "appSource": "ios",
        "appVersion": "2.0.0",
        "requestType": "20060"
    }
    print(type(date))
    utils = Utils()
    test1 = utils.extract_arguments(date)
    print(test1)
    test2 = utils.del_clientSign(test1)
    print(test2)