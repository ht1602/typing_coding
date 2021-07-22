#第2问，评价全拼输入法
import pandas as pd
import numpy as np
#load file
data=pd.read_csv("../count_alp_f.csv",encoding='gbk')
data.head()
data["total"] =data.apply(lambda x:x.sum(),axis =1)

#时间效率
#每个键盘按下所需要的时间为自定义的序列，根据手放在键盘上的位置而定
time_p=[1,3,2,2,1,1,2,2,1,1,2,2,2,2,1,2,2,2,2,3,2,2,1,3,3,2]
time={'Alphabet': ['a', 'b', 'c', 'd','e','f','g','h','i','j','k','l','m',
                   'n','o','p','q','r','s','t','u','v','w','x','y','z'],
      'Time/s':time_p}
df = pd.DataFrame(time)  # 这里默认的 index 就是 range(n)，n 是列表的长度
df.to_csv("../time_period.csv", encoding="gbk", index=False)
#计算输入5段100个字时间

time_quanpin=data['a'].sum()*time_p[0]+data['b'].sum()*time_p[1]+data['c'].sum()*time_p[2]+data['d'].sum()*time_p[3]+data['e'].sum()*time_p[4]+data['f'].sum()*time_p[5]+data['g'].sum()*time_p[6]+data['h'].sum()*time_p[7]+data['i'].sum()*time_p[8]
time_quanpin=time_quanpin+data['j'].sum()*time_p[9]+data['k'].sum()*time_p[10]+data['l'].sum()*time_p[11]+data['m'].sum()*time_p[12]+data['n'].sum()*time_p[13]+data['o'].sum()*time_p[14]+data['p'].sum()*time_p[15]+data['q'].sum()*time_p[16]
time_quanpin=time_quanpin+data['r'].sum()*time_p[17]+data['s'].sum()*time_p[18]+data['t'].sum()*time_p[19]+data['u'].sum()*time_p[20]+data['v'].sum()*time_p[21]+data['w'].sum()*time_p[22]+data['x'].sum()*time_p[23]+data['y'].sum()*time_p[24]+data['z'].sum()*time_p[25]
print("输入这些文字所需要的时间为：",time_quanpin,'s')
#信息熵评价系统
data=pd.DataFrame(data.drop(['v'],axis=1))#由于此次输入的文章中均未使用到v，故删去v的统计，方便后序信息熵的计算
n = list(data.columns)
H=0
for i in n:
    P=(data[i].sum())/(data["total"].sum())
    H=H-P*np.log2(P)
print("全拼系统的信息熵为：",H,"bit")

#standardize
# 总指标数
# 最优指标，(x-min)/(max-min)
# 最劣指标 (max-x)/(max-min)
# 如果指标体系存在最优指标和最劣指标，采用混合的形式
data=pd.DataFrame(data.drop(['total'],axis=1))
n = list(data.columns)
for i in n:
    # 获取各个指标的最大值和最小值
    Max = np.max(data[i])
    Min = np.min(data[i])
    data[i] = (data[i] - Min) / (Max - Min)


# 建立数据比重矩阵
for i in n:
    # 计算指标总和
    Sum = np.sum(data[i])
    # 计算某一指标占比
    data[i] = data[i] / Sum
print("数据比重矩阵：")
print(data)

#计算信息熵e和信息效用值d
# 统计的文章段数
m = len(data)
E = []
H=[]
# 计算信息熵值
for i in n:
    K = 1 / np.log(m)
    e = - K * np.sum(data[i] * np.log(data[i]))
    E.append(e)
# 转换为数组形式
E = np.array(E)
print(E)
# 计算效用价值
D = 1 - E
#计算指标权重
W = D/np.sum(D)
# 转换形式
W = np.array([W])

# 保存 权重 为excel格式
W1 = pd.DataFrame(W.T, index = n)
W1.to_csv('../权重1.csv')

#计算样本评价
U = []
for i in range(1, len(data) + 1):
    # 获取样本各个指标的值
    y = data[i - 1:i].values
    u1 = y * W * 100
    # 转换为列表
    u1 = u1.tolist()
    u1 = u1[0]

    # 计算样本综合得分
    ## 因前文构建了数据权重矩阵，故最后综合得分总和为100
    u = np.sum(y * W) * 100
    # 转换为列表
    u = np.array([u])
    u = u.tolist()
    # 各指标得分 和 综合得分
    u = u1 + u
    U.append(u)

# 获取样本列表
area = list(data.index)

# 生成数据框
U = pd.DataFrame(U, index=area)
# 重新设置列名称
U.columns = n + ['综合得分']

# 为各个指标得分排名
for i in n:
    i1 = i + '  排名'
    U[i1] = U[i].rank(ascending=False)

# 为样本综合得分排名
U['综合得分排名'] = U['综合得分'].rank(ascending=False)

# 保存为excel文件
U.to_csv('../综合得分.csv')

#计算5段文章的均值，由于5次字数均未100，故采用数字平均值
# -*- coding:utf-8 -*-
import csv
import numpy as np

data =pd.read_csv("../综合得分.csv",encoding='utf-8')   # 分隔符方式
average_sum=data['综合得分'].mean()


print('全拼输入法的最终得分为:', average_sum)  # 输出均值

