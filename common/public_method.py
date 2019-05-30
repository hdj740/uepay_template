import json
import requests
import operator
import hashlib

#class UrPayUilt:
# 删除字典一项
def Delete_item(json_parameter):
    json_parameter.pop("clientSign")  # 删除字典一项（clientSign）
#    print("删除项 clientSign ：",pop_obj)  # 输出删除项
#    print("删除后的json_parameter：",json_parameter)
    json_y = json_parameter
    return json_y

#字典排序
def Sort(sort):
    sorted_x = sorted(sort.items(), key=operator.itemgetter(0))  # 按照item中的第一个字符进行排序，即按照key排序
    sorted_y = str(sorted_x)
    print("排序后的json_parameter：",sorted_x)
    return str(sorted_y)

#字符替换
def Replace(replace):
    key = "&key=a0ebce93-809d-4519-82e1-264ee203922f"
    mo = replace # str 转换为字符串类型
    str1 = (mo.replace("', '", "="))
    str2 = (str1.replace("'), ('", "&"))
    str3 = (str2.replace("[('", ""))
    str4 = (str3.replace("')]", ""))
    k =str4 +key
#    print("整理后的json_parameter：",k)
    return k

#MD5加密
def MD5_add(str4):
    m = hashlib.md5()
    m.update(str4.encode("utf8"))
    clientSign = m.update
    #    print("MD5加密后的json_parameter：",m.hexdigest())
    return m.hexdigest()

#向服务器发送请求
def Request(test4, jsonObject):
    jsonObject["arguments"]["clientSign"] = test4 #向指点添加值
    print(jsonObject)
    header = {"Content-type": "application/json;charset=UTF-8"}  #请求格式
    r = requests.post('http://192.168.0.22:13010/app',json=jsonObject,headers = header)  #请求类型
    return r.text

def Handle(test5):
    json_tic = json.loads(test5)
    Result=json.dumps(json_tic,ensure_ascii=False, indent=4)
    return Result

def Format(jsonObject1):
    jsonObject = jsonObject1
    arguments = jsonObject["arguments"]  # 提取 jsonObject 的 arguments 值
    print(jsonObject)
    print(arguments)
    test1 = Delete_item(arguments)
    print(test1)
    print(type(test1))
    test2 = Sort(test1)
    print(test2)
    test3 = Replace(test2)
    print(test3)
    test4 = MD5_add(test3)
    print(test4)
    test5 = Request(test4,jsonObject)
    print(test5)
    Result = Handle(test5)
    return Result






