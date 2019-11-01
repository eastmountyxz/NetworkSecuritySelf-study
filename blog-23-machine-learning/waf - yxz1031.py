# coding: utf-8
import os
import urllib
import time
import html
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

# 获取文本中的请求列表
def get_query_list(filename):
    directory = str(os.getcwd())
    print(directory)
    filepath = directory + "/" + filename
    data = open(filepath, 'r', encoding='UTF-8').readlines()
    query_list = []
    for d in data:
        # 解码
        d = str(urllib.parse.unquote(d))   #converting url encoded data to simple string
        #print(d)
        query_list.append(d)
    return list(set(query_list))

# tokenizer function, this will make 3 grams of each query
# www.foo.com/1 转换为 ['www','ww.','w.f','.fo','foo','oo.','o.c','.co','com','om/','m/1']
def get_ngrams(query):
    tempQuery = str(query)
    ngrams = []
    for i in range(0, len(tempQuery)-3):
        ngrams.append(tempQuery[i:i+3])
    return ngrams

# 主函数
if __name__ == '__main__':
    
    # 获取正常请求
    good_query_list = get_query_list('goodqueries.txt')
    print(u"正常请求: ", len(good_query_list))
    for  i in range(0, 5):
        print(good_query_list[i].strip('\n'))
    print("\n")
        
    # 获取恶意请求
    bad_query_list = get_query_list('badqueries.txt')
    print(u"恶意请求: ", len(bad_query_list))
    for  i in range(0, 5):
        print(bad_query_list[i].strip('\n'))
    print("\n")

    # 预处理 good_y标记为0 bad_y标记为1
    good_y = [0 for i in range(0, len(good_query_list))]
    print(good_y[:5])
    bad_y = [1 for i in range(0, len(bad_query_list))]
    print(bad_y[:5])
    
    queries = bad_query_list + good_query_list
    y = bad_y + good_y

    # 定义矢量化 converting data to vectors
    # TfidfTransformer + CountVectorizer  =  TfidfVectorizer
    vectorizer = TfidfVectorizer(tokenizer=get_ngrams)

    # 把不规律的文本字符串列表转换成规律的 ( [i,j], tdidf值) 的矩阵X
    # 用于下一步训练逻辑回归分类器
    X = vectorizer.fit_transform(queries)
    print(X.shape)

    # 使用 train_test_split 分割 X y 列表
    # X_train矩阵的数目对应 y_train列表的数目(一一对应)  -->> 用来训练模型
    # X_test矩阵的数目对应 	 (一一对应) -->> 用来测试模型的准确性
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=20, random_state=42)

    # 定理逻辑回归方法模型
    LR = LogisticRegression()
    
    # 训练模型
    LR.fit(X_train, y_train)

    # 使用测试值 对 模型的准确度进行计算
    print('模型的准确度:{}'.format(LR.score(X_test, y_test)))
    print("\n")

    # 对新的请求列表进行预测
    new_queries = ['www.foo.com/id=1<script>alert(1)</script>',
                   'www.foo.com/name=admin\' or 1=1','abc.com/admin.php',
                   '"><svg onload=confirm(1)>',
                   'test/q=<a href="javascript:confirm(1)>',
                   'q=../etc/passwd',
                   '/stylesheet.php?version=1331749579',
                   '/<script>cross_site_scripting.nasl</script>.idc',
                   '<img \x39src=x onerror="javascript:alert(1)">',
                   '/jhot.php?rev=2 |less /etc/passwd']
    
    # 矩阵转换
    X_predict = vectorizer.transform(new_queries)
    res = LR.predict(X_predict)
    res_list = []

    # 结果输出
    for q,r in zip(new_queries, res):
        tmp = '正常请求' if r == 0 else '恶意请求'
        q_entity = html.escape(q)
        res_list.append({'url':q_entity,'res':tmp})

    for n in res_list:
        print(n)
        
    


    
    
    
