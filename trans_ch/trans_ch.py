import pandas as pd
from xpinyin import Pinyin
py=Pinyin()
# default splitter is `-`
gongchandang=py.get_pinyin(u"共产党宣言")
print(gongchandang)

#remove splitter
#chapter1
gongchandangxuanyan=py.get_pinyin(u"一个幽灵，共产主义的幽灵，在欧洲游荡。"
                   u"为了对这个幽灵进行神圣的围剿，旧欧洲的一切势力，"
                   u"教皇和沙皇、梅特涅和基佐、法国的激进派和德国的警察，"
                   u"都联合起来了。有哪一个反对党不被它的当政的敌人骂为共产党呢？"
                   u"又有哪一个反对党不拿共产主义这个罪名去回敬更进步的反对党人和自己的反动敌人呢？",' ')
#统计每个字母出现频率
a=gongchandangxuanyan.count("a")
b=gongchandangxuanyan.count("b")
c=gongchandangxuanyan.count("c")
d=gongchandangxuanyan.count("d")
e=gongchandangxuanyan.count("e")
f=gongchandangxuanyan.count("f")
g=gongchandangxuanyan.count("g")
h=gongchandangxuanyan.count("h")
i=gongchandangxuanyan.count("i")
j=gongchandangxuanyan.count("j")
k=gongchandangxuanyan.count("k")
l=gongchandangxuanyan.count("l")
m=gongchandangxuanyan.count("m")
n=gongchandangxuanyan.count("n")
o=gongchandangxuanyan.count("o")
p=gongchandangxuanyan.count("p")
q=gongchandangxuanyan.count("q")
r=gongchandangxuanyan.count("r")
s=gongchandangxuanyan.count("s")
t=gongchandangxuanyan.count("t")
u=gongchandangxuanyan.count("u")
v=gongchandangxuanyan.count("v")
w=gongchandangxuanyan.count("w")
x=gongchandangxuanyan.count("x")
y=gongchandangxuanyan.count("y")
z=gongchandangxuanyan.count("z")

#chapter2
gongchandangxuanyan=py.get_pinyin(u"有哪一个反对党不被它的当政的敌人"
                                 u"骂为共产党呢？又有哪一个反对党不"
                                 u"拿共产主义这个罪名去回敬更进步的"
                                 u"反对党人和自己的反动敌人呢？一个"
                                 u"幽灵，共产主义的幽灵，在欧洲游荡。",' ')
a1=gongchandangxuanyan.count("a")
b1=gongchandangxuanyan.count("b")
c1=gongchandangxuanyan.count("c")
d1=gongchandangxuanyan.count("d")
e1=gongchandangxuanyan.count("e")
f1=gongchandangxuanyan.count("f")
g1=gongchandangxuanyan.count("g")
h1=gongchandangxuanyan.count("h")
i1=gongchandangxuanyan.count("i")
j1=gongchandangxuanyan.count("j")
k1=gongchandangxuanyan.count("k")
l1=gongchandangxuanyan.count("l")
m1=gongchandangxuanyan.count("m")
n1=gongchandangxuanyan.count("n")
o1=gongchandangxuanyan.count("o")
p1=gongchandangxuanyan.count("p")
q1=gongchandangxuanyan.count("q")
r1=gongchandangxuanyan.count("r")
s1=gongchandangxuanyan.count("s")
t1=gongchandangxuanyan.count("t")
u1=gongchandangxuanyan.count("u")
v1=gongchandangxuanyan.count("v")
w1=gongchandangxuanyan.count("w")
x1=gongchandangxuanyan.count("x")
y1=gongchandangxuanyan.count("y")
z1=gongchandangxuanyan.count("z")

#chapter3
gongchandangxuanyan=py.get_pinyin(u"从这一事实中可以得出两个结论："
                                 u"共产主义已经被欧洲的一切势力公认为一种势力；"
                                 u"现在是共产党人向全世界公开说明自己的观点、"
                                 u"自己的目的、自己的意图并且拿党自己的宣言来"
                                 u"反驳关于共产主义幽灵的神话的时候了。为了这"
                                 u"个目的，各国共产党人集会于伦敦，拟定了如下"
                                 u"的宣言，用英文、法文、德文、意大利文、弗拉"
                                 u"芒文和丹麦文公布于世。",' ')
a2=gongchandangxuanyan.count("a")
b2=gongchandangxuanyan.count("b")
c2=gongchandangxuanyan.count("c")
d2=gongchandangxuanyan.count("d")
e2=gongchandangxuanyan.count("e")
f2=gongchandangxuanyan.count("f")
g2=gongchandangxuanyan.count("g")
h2=gongchandangxuanyan.count("h")
i2=gongchandangxuanyan.count("i")
j2=gongchandangxuanyan.count("j")
k2=gongchandangxuanyan.count("k")
l2=gongchandangxuanyan.count("l")
m2=gongchandangxuanyan.count("m")
n2=gongchandangxuanyan.count("n")
o2=gongchandangxuanyan.count("o")
p2=gongchandangxuanyan.count("p")
q2=gongchandangxuanyan.count("q")
r2=gongchandangxuanyan.count("r")
s2=gongchandangxuanyan.count("s")
t2=gongchandangxuanyan.count("t")
u2=gongchandangxuanyan.count("u")
v2=gongchandangxuanyan.count("v")
w2=gongchandangxuanyan.count("w")
x2=gongchandangxuanyan.count("x")
y2=gongchandangxuanyan.count("y")
z2=gongchandangxuanyan.count("z")

#chapter4
gongchandangxuanyan=py.get_pinyin(u"从这一事实中可以得出两个结论："
                                 u"共产主义已经被欧洲的一切势力公认为一种势力；"
                                 u"现在是共产党人向全世界公开说明自己的观点、"
                                 u"自己的目的、自己的意图并且拿党自己的宣言来"
                                 u"反驳关于共产主义幽灵的神话的时候了。为了这"
                                 u"个目的，各国共产党人集会于伦敦，拟定了如下"
                                 u"的宣言，用英文、法文、德文、意大利文、弗拉"
                                 u"芒文和丹麦文公布于世。",' ')
a3=gongchandangxuanyan.count("a")
b3=gongchandangxuanyan.count("b")
c3=gongchandangxuanyan.count("c")
d3=gongchandangxuanyan.count("d")
e3=gongchandangxuanyan.count("e")
f3=gongchandangxuanyan.count("f")
g3=gongchandangxuanyan.count("g")
h3=gongchandangxuanyan.count("h")
i3=gongchandangxuanyan.count("i")
j3=gongchandangxuanyan.count("j")
k3=gongchandangxuanyan.count("k")
l3=gongchandangxuanyan.count("l")
m3=gongchandangxuanyan.count("m")
n3=gongchandangxuanyan.count("n")
o3=gongchandangxuanyan.count("o")
p3=gongchandangxuanyan.count("p")
q3=gongchandangxuanyan.count("q")
r3=gongchandangxuanyan.count("r")
s3=gongchandangxuanyan.count("s")
t3=gongchandangxuanyan.count("t")
u3=gongchandangxuanyan.count("u")
v3=gongchandangxuanyan.count("v")
w3=gongchandangxuanyan.count("w")
x3=gongchandangxuanyan.count("x")
y3=gongchandangxuanyan.count("y")
z3=gongchandangxuanyan.count("z")



data = {'Alphabet': ['a', 'b', 'c', 'd','e','f','g','h','i','j','k','l','m',
                     'n','o','p','q','r','s','t','u','v','w','x','y','z'],
        'Times': [a, b, c, d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]}
# 用Lists的字典创建数据集

df = pd.DataFrame(data)  # 这里默认的 index 就是 range(n)，n 是列表的长度
print(df)
df.to_csv("../count_alp.csv", encoding="gbk", index=False)


dat={'a':[a,a1,a2,a3],'b':[b,b1,b2,b3],'c':[c,c1,c2,c3],'d':[d,d1,d2,d3],'e':[e,e1,e2,e3],'f':[f,f1,f2,f3],
     'g': [g,g1,g2,g3], 'h': [h,h1,h2,h3], 'i': [i,i1,i2,i3], 'j': [j,j1,j2,j3], 'k': [k,k1,k2,k3], 'l': [l,l1,l2,l3],
     'm': [m,m1,m2,m3], 'n': [n,n1,n2,n3], 'o': [o,o1,o2,o3], 'p': [p,p1,p2,p3], 'q': [q,q1,q2,q3], 'r': [r,r1,r2,r3],
     's': [s,s1,s2,s3], 't': [t,t1,t2,t3], 'u': [u,u1,u2,u3], 'v': [v,v1,v2,v3], 'w': [w,w1,w2,w3], 'x': [x,x1,x2,x3],
     'y': [y,y1,y2,y3], 'z': [z,z1,z2,z3]
     }
dff = pd.DataFrame(dat)
#dfData=dff.corr()
#print(dfData)
dff.to_csv("../count_alp_f.csv", encoding="gbk", index=False)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore") #过滤掉警告的意思
from pyforest import *

data=pd.read_csv("../count_alp_f.csv",encoding='gbk')
data.head()
print(data)
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] =False #减号unicode编码
corr =data.corr()
print(corr)

ax = plt.subplots(figsize=(20, 16))#调整画布大小
ax=sns.heatmap(corr, vmax=.8, square=True, annot=True)#画热力图   annot=True 表示显示系数
# 设置刻度字体大小
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.show()

