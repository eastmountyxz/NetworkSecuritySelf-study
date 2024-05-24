# -*- coding: utf-8 -*-
import shodan

#初始化
SHODAN_API_KEY = 'Qy8iiPBIvnWbixxxxxxxxxxx6ZUbdrW'

api = shodan.Shodan(SHODAN_API_KEY)

#查询Apache主机数量
result = api.search('apache')
print(result['total'])

#查询制定IP地址
ip_res = api.host('59.110.244.199')
print(ip_res['country_name'])
