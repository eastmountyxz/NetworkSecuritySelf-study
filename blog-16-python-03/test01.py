# -*- coding: utf-8 -*-
import exrex

#填入正则表达式的代码会生成对应的内容
print exrex.getone('(ex)r\\1')

#转换列表 匹配2个hai或word
num = list(exrex.generate('((hai){2}|word!)'))
print num

#数字 如3575-7048-5984-2471
print exrex.getone('\d{4}-\d{4}-\d{4}-[0-9]{4}')

#时间
print exrex.getone('(1[0-2]|0[1-9])(:[0-5]\d){2} (A|P)M')

#计数
print exrex.count('[01]{0,9}')

#假设知道某个密码的组合方式，需要将所有的密码都列举出来
num = list(exrex.generate('[Pp][a@]ssw[Oo]rd'))
print num
