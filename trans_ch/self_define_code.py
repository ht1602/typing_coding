from xpinyin import Pinyin
import pandas as pd
py=Pinyin()

def encode(s):
    s=s.replace("ng","jj")
    s=s.replace("k","j")
    s=s.replace("l","j")
    s=s.replace("an","aj")
    s=s.replace("un","uj")
    s=s.replace("en","ej")
    s=s.replace("vn","vj")
    s=s.replace("in","ij")
    s=s.replace("n","o")
    s=s.replace("m","o")
    s=s.replace("g","i")
    s=s.replace("h","i")
    s=s.replace("b","a")
    s=s.replace("c","a")
    s=s.replace("d","f")
    s=s.replace("q","p")
    s = s.replace("r", "p")
    s = s.replace("s", "p")
    s=s.replace("t","u")
    s=s.replace("v","u")
    s=s.replace("x","w")
    s=s.replace("y","w")
    s.replace("z","w")
    return s

def encrypt(key, s): 
    b = bytearray(str(s).encode("gbk")) 
    n = len(b) # 求出 b 的字节数 
    c = bytearray(n*2) 
    j = 0 
    for i in range(0, n): 
        b1 = b[i] 
        b2 = b1 ^ key # b1 = b2^ key 
        c1 = b2 % 16 
        c2 = b2 // 16 # b2 = c2*16 + c1 
        c1 = c1 + 97
        c2 = c2 + 97 # c1,c2都是0~15之间的数,加上97就变成了a-p 的字符的编码
        c[j] = c1 
        c[j+1] = c2 
        j = j+2 
    return c.decode("gbk") 

def decrypt(key, s): 
    c = bytearray(str(s).encode("gbk")) 
    n = len(c) # 计算 b 的字节数 
    if n % 2 != 0 : 
        return "" 
    n = n // 2 
    b = bytearray(n) 
    j = 0 
    for i in range(0, n): 
        c1 = c[j] 
        c2 = c[j+1] 
        j = j+2 
        c1 = c1 - 97
        c2 = c2 - 97
        b2 = c2*16 + c1 
        b1 = b2^ key 
        b[i]= b1 
    try: 
        return b.decode("gbk") 
    except: 
        return "failed"

key = 30
pinyin1=py.get_pinyin(u"一个幽灵，共产主义的幽灵，在欧洲游荡。"
                                  u"为了对这个幽灵进行神圣的围剿，旧欧洲"
                                  u"的一切势力，教皇和沙皇、梅特涅和基佐、"
                                  u"法国的激进派和德国的警察，都联合起来了。"
                                  u"有哪一个反对党不被它的当政的敌人骂为共产党呢？又",' ')
#s1 = encrypt(key, pinyin1)
s1=encode(pinyin1)
print(s1)
pinyin2=py.get_pinyin(u"有哪一个反对党不拿共产主义这个"
                                  u"罪名去回敬更进步的反对党人和自"
                                  u"己的反动敌人呢？从这一事实中可"
                                  u"以得出两个结论：共产主义已经被"
                                  u"欧洲的一切势力公认为一种势力；"
                                  u"现在是共产党人向全世界公开说明自己的观点、自己的目",' ')
#s2 = encrypt(key, pinyin2)
s2=encode(pinyin2)
print(s2)
pinyin3=py.get_pinyin(u"的、自己的意图并且拿党自己的"
                                  u"宣言来反驳关于共产主义幽灵的"
                                  u"神话的时候了。为了这个目的，"
                                  u"各国共产党人集会于伦敦，拟定"
                                  u"了如下的宣言，用英文、法文、"
                                  u"德文、意大利文、弗拉芒文和丹"
                                  u"麦文公布于世。一、资产者和无产者",' ')
#s3=encrypt(key,pinyin3)
s3=encode(pinyin3)
print(s3)

pinyin4=py.get_pinyin(u"至今一切社会的历史都是阶级斗争的历史。"
                                  u"自由民和奴隶、贵族和平民、领主和农奴、"
                                  u"行会师傅和帮工，一句话，压迫者和被压"
                                  u"迫者，始终处于相互对立的地位，进行不断"
                                  u"的、有时隐蔽有时公开的斗争，而每一次斗争的结局是整",' ')
#s4=encrypt(key,pinyin4)
s4=encode(pinyin4)
print(s4)

pinyin5=py.get_pinyin(u"个社会受到革命改造或者斗争的各阶级"
                                  u"同归于尽。在过去的各个历史时代，我"
                                  u"们几乎到处都可以看到社会完全划分为"
                                  u"各个不同的等级，看到社会地位分成的"
                                  u"多种多样的层次。在古罗马，有贵族、"
                                  u"骑士、平民、奴隶，在中世纪，有",' ')
#s5=encrypt(key,pinyin5)
s5=encode(pinyin5)
print(s5)

a=s1.count("a")
e=s1.count("e")
f=s1.count("f")
i=s1.count("i")
j=s1.count("j")
o=s1.count("o")
p=s1.count("p")
u=s1.count("u")
w=s1.count("w")

a1=s2.count("a")
e1=s2.count("e")
f1=s2.count("f")
i1=s2.count("i")
j1=s2.count("j")
o1=s2.count("o")
p1=s2.count("p")
u1=s2.count("u")
w1=s2.count("w")

a2=s3.count("a")
e2=s3.count("e")
f2=s3.count("f")
i2=s3.count("i")
j2=s3.count("j")
o2=s3.count("o")
p2=s3.count("p")
u2=s3.count("u")
w2=s3.count("w")

a3=s4.count("a")
e3=s4.count("e")
f3=s4.count("f")
i3=s4.count("i")
j3=s4.count("j")
o3=s4.count("o")
p3=s4.count("p")
u3=s4.count("u")
w3=s4.count("w")

a4=s5.count("a")
e4=s5.count("e")
f4=s5.count("f")
i4=s5.count("i")
j4=s5.count("j")
o4=s5.count("o")
p4=s5.count("p")
u4=s5.count("u")
w4=s5.count("w")



dat={'a':[a,a1,a2,a3,a4],'e':[e,e1,e2,e3,e4],'f':[f,f1,f2,f3,f4],
     'i': [i,i1,i2,i3,i4], 'j': [j,j1,j2,j3,j4],
     'o': [o,o1,o2,o3,o4], 'p': [p,p1,p2,p3,p4],
     'u':[u,u1,u2,u3,u4],'w':[w,w1,w2,w3,w4]
     }
dff = pd.DataFrame(dat)
print(dff)
#dfData=dff.corr()
#print(dfData)
dff.to_csv("../count_alp_newcoding.csv", encoding="gbk", index=False)

######################################
####           评价部分           ####
######################################
import pandas as pd
import numpy as np
#load file
data=pd.read_csv("../count_alp_newcoding.csv",encoding='gbk')
data.head()
data["total"] =data.apply(lambda x:x.sum(),axis =1)

#时间效率
#每个键盘按下所需要的时间为自定义的序列，根据手放在键盘上的位置而定
time_p=[1,3,2,2,1,1,2,2,1,1,2,2,2,2,1,2,2,2,2,2,2,2,1,3,3,2]
time={'Alphabet': ['a', 'b', 'c', 'd','e','f','g','h','i','j','k','l','m',
                   'n','o','p','q','r','s','t','u','v','w','x','y','z'],
      'Time/s':time_p}
df = pd.DataFrame(time)  # 这里默认的 index 就是 range(n)，n 是列表的长度
df.to_csv("../time_period.csv", encoding="gbk", index=False)
#计算输入5段100个字时间

time_quanpin=data['a'].sum()*time_p[0]+data['e'].sum()*time_p[4]+data['f'].sum()*time_p[5]+data['i'].sum()*time_p[8]
time_quanpin=time_quanpin+data['j'].sum()*time_p[9]+data['o'].sum()*time_p[14]+data['p'].sum()*time_p[15]
time_quanpin=time_quanpin+data['u'].sum()*time_p[20]+data['w'].sum()*time_p[22]
print("输入这些文字所需要的时间为：",time_quanpin,'s')
#信息熵评价系统
#data=pd.DataFrame(data.drop(['v'],axis=1))#由于此次输入的文章中均未使用到v，故删去v的统计，方便后序信息熵的计算
n = list(data.columns)
H=0
for i in n:
    P=(data[i].sum())/(data["total"].sum())
    H=H-P*np.log2(P)
print("全拼系统的信息熵为：",H,"bit")