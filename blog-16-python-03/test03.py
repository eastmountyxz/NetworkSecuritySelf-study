# -*- coding: utf-8 -*-
import exrex

# ------------------- URL切割并处理成按斜杠划分的格式 -------------------------
def host_pare(host):
    # 获取核心字符串
    if '://' in host: 
        host = host.split('://')[1].replace('/', '')

    if '/' in host: #demo.webdic.com
        host = host.replace('/', '')
        
    return host

# 白名单包含的字典不能作为字典的内容
web_white = ['com', 'cn', 'gov', 'edu', 'org', 'www']


# ------------------- 将获取的hosts放入字典生成函数中 -------------------------
def dic_create(hosts):
    dics = []
    
    # 切割
    web_dics = hosts.split('.')

    # 取出有用的东西，如demo、eastmount放入字典生成器
    for web_dic in web_dics:
        if web_dic not in web_white:  # 定义白名单过滤com
            #print web_dic
            dics.append(web_dic)
            
    return dics

# --------------------------------------- 生成字典密码 --------------------------------------
def make_pass(dics):

    for dic in dics:
        #打开配置文件
        f_rule = open('rule.ini', 'r')
        for i in f_rule:
            if '#' != i[0]: #判断第一个字符 非#表示配置内容
                rule = i
                print u'The rule is ', i

        #保存生成的字典
        fout = open('pass_out.txt', 'w')
        fout.close()
                
        #获取字典中的内容
        f_pass = open('pass.txt', 'r')
        for pwd in f_pass:
            #部分密码较弱 根据网站设置长度
            final_pwds = list(exrex.generate(rule.format(dic=dic, pwd=pwd.strip('\n'))))
            #遍历密码
            for final_pwd in final_pwds:
                if len(final_pwd) > 6:
                    print final_pwd
                    #保存生成的字典
                    fout = open('pass_out.txt', 'a+')
                    fout.write(final_pwd + '\n')
                    fout.close()
                
# ----------------------------------------- 主函数 ---------------------------------------------
if __name__ == '__main__':
    url = 'https://demo.eastmount.com/'
    dics = dic_create(host_pare(url))
    make_pass(dics)
