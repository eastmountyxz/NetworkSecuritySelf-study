# AI-for-Malware-Analysis

这是作者恶意代码分析、网络安全、系统安全等系列教程，主要是通过机器学习、人工智能和深度学习来分析恶意代码的在线笔记。希望对您有所帮助，学无止境，一起加油。

---

## 第一个案例：通过机器学习来识别恶意代码

[[网络安全自学篇] 二十三.基于机器学习的恶意请求识别及安全领域中的机器学习](https://blog.csdn.net/Eastmount/article/details/102852458) <br />

LogisticsRegression-WebURL - 数据集及实验

基本思路如下：
- 读取正常请求和恶意请求数据集，预处理设置类标y和数据集x
- 通过N-grams处理数据集，并构建TF-IDF特征矩阵，每个请求对应矩阵的一行数据
- 数据集拆分为训练数据和测试数据
- 使用机器学习逻辑回归算法对特征矩阵进行训练，得出对应的模型
- 使用训练的模型对 未知URL请求进行检测，判断其是恶意请求或正常请求


<div align=center><img src="https://img-blog.csdnimg.cn/20191101135601145.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0Vhc3Rtb3VudA==,size_16,color_FFFFFF,t_70" width="60%" height="60%" />
</div>

---

## 第二个案例：KDD CUP99数据集 KNN入侵攻击检测

[[网络安全自学篇] 二十四.基于机器学习的入侵检测和攻击识别——以KDD CUP99数据集为例](https://blog.csdn.net/Eastmount/article/details/103189405) <br /> 

KDD_CUP99_KNN_Attack - KNN数据分析  <br /> 
KDD_CUP99_KNN_Preprocess - 数据预处理&KNN分析 <br />
KDD_CUP_1999_AllData - 完整数据集  <br />

它有几个亮点：
- 详细介绍了数据分析预处理中字符特征转换为数值特征、数据标准化、数据归一化，这都是非常基础的工作。
- 结合入侵检测应用KNN实现分类。
- 绘制散点图采用序号、最小欧式距离、类标，ROC曲线绘制都是之前没分享的。

但也存在很多缺点，希望后续继续完善及深入学习。



<div align=center><img src="https://img-blog.csdnimg.cn/20191123010453811.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0Vhc3Rtb3VudA==,size_16,color_FFFFFF,t_70#pic_center" width="60%" height="60%" />
</div>

---

By:Easatmount 杨秀璋
2019-11-23
