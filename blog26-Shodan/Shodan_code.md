Shodan常见的命令包括：
- hostname：搜索指定的主机或域名，例如 hostname:“google”
- port：搜索指定的端口或服务，例如 port:“21”
- country：搜索指定的国家，例如 country:“CN”
- city：搜索指定的城市，例如 city:“Hefei”
- org：搜索指定的组织或公司，例如 org:“google”
- isp：搜索指定的ISP供应商，例如 isp:“China Telecom”
- product：搜索指定的操作系统/软件/平台，例如 product:“Apache httpd”
- version：搜索指定的软件版本，例如 version:“1.6.2”
- geo：搜索指定的地理位置，参数为经纬度，例如 geo:“31.8639, 117.2808”
- before/after：搜索指定收录时间前后的数据，格式为 dd-mm-yy，例如 before:“11-11-15”
- net：搜索指定的IP地址或子网，例如 net:“210.45.240.0/24”


**1.Shodan获取指定IP地址信息**

```python
shodan host ip地址
```


**2.Shodan获取账号信息**


```python
shodan info
```


**3.Shodan获取自身外部IP地址**

```python
shodan myip
```

**4.Shodan检测是否有蜜罐**

```python
shodan honeyscore
```
