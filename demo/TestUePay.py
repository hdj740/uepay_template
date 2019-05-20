import requests
import json
import unittest
from demo.BeforeRequest import request

class TestMetgod(unittest.TestCase):


    def test_03(self):
        data = {
            "arguments":
                {
                    "loginName": "18788782150",
                    "areaCode": "0068",
                    "pwd": "nps0111C88AE04CEC1BA554D03D5B5970333A83585826C2A985DE5520D9E934389EFB84B52D344FB21AA8EA38A4940C8332692B8D4DA2393549212EAFDC0F11CA5C9CC86FABB859E4E585CF57B02E7A928C9252403938EEC8D70A7781018F0C90E55FE475BB3881C1734697BFBA39F4A92E6727833B72F5B50ED0F4A7522E0F0F9E65nps01",
                    "OsType": "ios"
                },
            "appSource": "ios",
            "appVersion": "2.0.0",
            "requestType": "5004"
        }


        res = request(data)

        i1 = json.loads(res.res)
        i2 = json.dumps(i1,indent=4,sort_keys=True)
        print(i2)


if __name__ == "__main__":
    unittest.main()






