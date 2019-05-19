import requests
import json

class RunMain:

    def __init__(self,url,method,data=None):
        self.run = self.run_main(url=url,method=method,data=data)

    def send_post(self,url,data):
        res = requests.post(url=url, data=json.dumps(data))
        return res.text

    def send_get(self,url,data):
        res = requests.get(url,data)
        print(res.text)
        return res.text

    def run_main(self,url,method,data=None):
        if(method == 'POST'):
            res = self.send_post(url,data)
        else:
            res = self.send_get(url,data)
        return res

if __name__ == '__main__':
    baiduurl = 'http://www.baidu.com'
    urpayurl = 'http://apptest.uepay.mo/app'
    data = {
        "arguments":
            {
                "areaCode": "0068",
                "clientSign": "5424510c4100073edd63394c6a444577",
                "loginName": "18788782150",
                "pwd": "nps0111C88AE04CEC1BA554D03D5B5970333A83585826C2A985DE5520D9E934389EFB84B52D344FB21AA8EA38A4940C8332692B8D4DA2393549212EAFDC0F11CA5C9CC86FABB859E4E585CF57B02E7A928C9252403938EEC8D70A7781018F0C90E55FE475BB3881C1734697BFBA39F4A92E6727833B72F5B50ED0F4A7522E0F0F9E65nps01",
                "OsType": "ios"
            },
        "appSource": "ios",
        "appVersion": "2.0.0",
        "requestType": "5004"
    }
    run = RunMain(urpayurl,'POST',data)
    print("run", run.run)


