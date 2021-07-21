#第2问，评价全拼输入法
import pandas as pd
import numpy as np
#load file
data=pd.read_csv("../count_alp_f.csv",encoding='gbk')
data.head()
data=pd.DataFrame(data.drop(['v'],axis=1))
#由于此次输入的文章中均未使用到v，故删去v的统计，方便后序信息熵的计算

#standardize
# 总指标数
n = list(data.columns)
# 最优指标，(x-min)/(max-min)
# 最劣指标 (max-x)/(max-min)
# 如果指标体系存在最优指标和最劣指标，采用下面的形式
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
print(data)
#计算信息熵e和信息效用值d
# 统计的文章段数
m = len(data)
E = []
# 计算信息熵值
for i in n:
    K = 1 / np.log(m)
    e = - K * np.sum(data[i] * np.log(data[i]))
    E.append(e)

# 转换为数组形式
E = np.array(E)

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


