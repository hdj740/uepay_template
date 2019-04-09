from logs.log import log1
from comfig import public_method
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

print('返回参数：', up)
Result1 = json.loads(up)

try:
    Result2 = Result1['results']['msg']
    print(Result2)
    log1.info(Result2)
except KeyError  as e:
    print("KeyError:", e)
    log1.info("KeyError:", e)

#print(type(Result))     #查看数据类型

# 测试类
class test_class(unittest.TestCase):

    def test_API(self):
        b = "您當前是最新版本，無需更新！"
        self.assertEqual(Result2, b)
    def test_API1(self):
        a = 1
        b = 2
        self.assertEqual(a, b)
    def test_API2(self):
        a = 2
        b = 2
        self.assertEqual(a, b)

if __name__ == "__main__":
    unittest.main()


