import hashlib
import operator
import requests

class Run_Request:

    def __init__(self, data):
        self.res = self.requestIfon(data)

    def before(self,data):

        arguments = data["arguments"]
        arguments1 = 'clientSign' in arguments

        if arguments1 == False:
            pass
        else:
            arguments.pop("clientSign")

        # 0代表大写先排序，1不分大小写
        sorted_arguments = sorted(arguments.items(), key=operator.itemgetter(0))
        dict_data = (dict(sorted_arguments))
        str_data = str(dict_data)
        return str_data

    def checkReplace(self,before):

        key = "&key=a0ebce93-809d-4519-82e1-264ee203922f"

        replace1 = before.replace("{", "")
        replace2 = replace1.replace("}", "")
        replace3 = replace2.replace("'", "")
        replace4 = replace3.replace(": ", "=")
        replace5 = replace4.replace(", ", "&")
        replace6 = replace5 + key
        md5 = hashlib.md5()
        md5.update(replace6.encode("utf-8"))
        return md5.hexdigest()

    def requestIfon(self,data):

        str_data = self.before(data)
        checkReplace = self.checkReplace(str_data)
        data["arguments"]["clientSign"] = checkReplace
        return data


if __name__ == "__main__":
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

    run = Run_Request(data)

    print("run"+run.res)
    print(type(run.res))



