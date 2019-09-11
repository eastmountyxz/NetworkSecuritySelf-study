# -*- coding: utf-8 -*-
import json

data = {
    'id' : 1,
    'name' : 'test1',
    'age' : '1'
}
data2 = [{
    'id' : 1,
    'name' : 'test1',
    'age' : '1'
},{
    'id' : 2,
    'name' : 'test2',
    'age' : '2'
}]

#python字典类型转换为json对象
json_str = json.dumps(data)
print(u"python原始数据：")
print(repr(data))
print (u"json对象：")
print(json_str)
print("")
 
json_str2 = json.dumps(data2)
print (u"python原始数据：")
print(repr(data2))
print (u"json对象：")
print(json_str2)
print("")
	
 
# 将json对象转换为python字典
data3 = json.loads(json_str)
print(data3)
print("data3['name']: ", data3['name'])
print("data3['age']: ", data3['age'])
