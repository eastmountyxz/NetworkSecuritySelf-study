# -*- coding: utf-8 -*-
import exrex

# 常见密码 弱口令
pwds = ['123456', '111111', '666666', '12345678', 'qwerty', '123456789', 'abc123']

# 生成字典密码 
def make_pass(pwds):

    #保存生成的字典
    fout = open('pass_out.txt', 'w')
    fout.close()
        
    #假设包含三种内容 1.字符串YXZ 2.数字密码 3.下划线或井号
    for pwd in pwds:
        #假设三种组合(含大小写) Yxz123456_ 123456yxz_   _yxZ123456
        rules = ['({pwd})([Yx][Xx][Zz])(_|#)',
                '([Yx][Xx][Zz])({pwd})(_|#)',
                 '(_|#)({pwd})([Yx][Xx][Zz])']

        #密码生成
        for rule in rules:
            final_pwds = list(exrex.generate(rule.format(pwd=pwd)))
            for final_pwd in final_pwds:
                print final_pwd
                #保存生成的字典
                fout = open('pass_out.txt', 'a+')
                fout.write(final_pwd + '\n')
                fout.close()
                
# 主函数
if __name__ == '__main__':
    make_pass(pwds)
