from logs.log import log1
from common import public_method
import json
import unittest


jsonObject={
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

up = public_method.Format(jsonObject)




