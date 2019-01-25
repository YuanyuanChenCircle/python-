import pymysql
import random
import numpy as np
import matplotlib.pyplot as plt
# from pylab import *
import pandas as pd

import subprocess
import pylab
import matplotlib

# matplotlib.use('qt4agg')

from matplotlib.font_manager import FontManager, FontProperties


# def getChineseFont():
# 	return FontProperties(fname='/System/Library/Fonts/PingFang.ttc')#mac os系统的字体

#显示中文
# font = FontProperties(fname='/System/Library/Fonts/PingFang.ttc')#mac os系统的字体
# # mpl.rcParams['font.sans-serif'] = ['SimHei']
# myfont = FontProperties(fname='C:/Windows/Fonts/simhei.ttf')#windows系统的字体

#读取数据库到本地
print(u'-----连接数据库读取数据-----')
user_ = input(u'请输入用户名:')
pswd_ = input(u'请输入密码:')
dbname_ = input(u'请输入数据库名:')
tablename_ = input(u'请输入你要读取的数据库表名:')

######输入Navicat mysql的数据库的user,一般默认为root，无需更改，password是mysql的密码，db是你的数据库名字，为保证不出错
#可以命名数据库为data_re
db = pymysql.connect(host = 'localhost',user = user_,password = pswd_,port = 3306,db = dbname_)
cursor = db.cursor()
# cursor.execute('SELECT VERSION()')
sql = 'select * from '+tablename_
cursor.execute(sql)
results = cursor.fetchall()#数据库的结果
# print(len(results))
# data = cursor.fetchone()
# print('Database version:',data)
# cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")
# print(results[0][0])
#如果有100个参数,随机生成100个点


#按每一行（每一个聚类）包含的数据个数排序，集合中数据个数大的排在上面，数据个数小的排在下面
d = sorted(results,key=(lambda x:x[2]),reverse=True)

# print(len(d))
# print(d)

data_list = []#把每一行放到一个集合中，把每一个集合放到一个列表中
for i in range(len(d)):
	data = set()
	data_ch = []
	data_ch = d[i][0].split(',')
	for m in range(len(data_ch)):
		data.add(data_ch[m])
	# print(d[i][0])
	# data.add()
	data_list.append(data)
# print(data_list)
print("------进行了删除数据库的子集，如果删除后数据库的数据库的行数大于10,则画图时输入一行显示的数据库行数为5\n;如果大于20；一行显示为6，即一共显示4行\n;保证所画集合在可显示范围----")

#删除列表中各个集合中的子集
data_list1 = []#把需要删除的子集保存到data_list1中
for j in range(len(data_list) - 1):

	for k in range(j+1,len(data_list)):
		# print("****************")
		# print(data_list[j])
		# print("##############")
		# print(dawta_list[k])
		if (data_list[k].issubset(data_list[j])) == True:
			# data_list.remove(data_list[k])
			# print("##############")
			# print(data_list[k])
			data_list1.append(data_list[k])
		# else:
		# 	data_list1.append(data_list[j])
		# 	# print(data_list[k])
print(len(data_list))#
# print(list(set(data_list1)))

data_list2 = []

#去除data_list1列表中关于子集的重复元素，保存到data_list2列表中
for h in range(len(data_list1)):
	if h == 0:
		data_list2.append(data_list1[h])
	if data_list1[h] not in data_list2:
		data_list2.append(data_list1[h])
# print(data_list2)

#删除数据库中的子集
for g in range(len(data_list2)):
	data_list.remove(data_list2[g])
# print(len(data_list))
# for h in range(len(data_list1)):
# 	data_list.remove(data_list1[h])
# print(len(data_list))

#可视化
plt.figure(figsize=(20,8))
x = 0
y = 0

count = 0

print(u'-----调整初始圆心，默认为 a = 0,b = 0调整半径，设置，所有集合的半径相同默认为3.一般情况下，输入默认值。-----')
a = input(u'请输入初始圆心a:')
b = input(u'请输入初始圆心b:')
r = input(u'请输入圆心的半径r:')
n = input(u'请输入一行想要显示的数据库的数据项数(大于等于4):')
a = float(a)
b = float(b)
r = float(r)
n = float(n)
#co为颜色值序列，可以动态调整其大小,为使圆正常显示,可以调整a,b,(a,b)为圆心，r为半径。
#a,b的值在下面的循环中改，改变每次增加多少
print("-----删除数据库中的子集后表中剩余的数据项的个数-----")
print(len(data_list))
print("-----请输入想要可视化的数据库的行数，希望不大于30，因为过多屏幕显示不全，会出现重叠的情况-----")
q = input(u'请输入想要可视化的数据库中表的数据项数:')
q = int(q)
data_list = data_list[:q]
co = ['b','c','g','k','m','r','y','b','c','g','k','m','r','y','b','c','g','k','m','r','y','y','b','c','g','k','m','r','y','b','c','g','k','m','r','y','b','c','g','k','m','r','y']
for u in range(len(data_list)):
	tem_list = []
	print(data_list[u])
	for item in data_list[u]:
		tem_list.append(item)

	# tem_list = data_list[a].split(',')
	#生成圆内的数
	theta = np.arange(0, 2*np.pi, 0.01)
	
	x3 = a + (r + 0.4) * np.cos(theta)
	y3 = b + (r + 0.4) * np.sin(theta) 
	degree = np.random.rand(len(tem_list))*np.pi*2
	x4 = []
	y4 = []
	for m in range(len(tem_list)):
		count_ = [1]
		judge = 0
		while judge == 0:
			x4_ = []
			y4_ = []
			degree1 = np.random.rand(len(count_))*np.pi*2
			x4_ = a + r * np.cos(degree1)*np.random.rand(len(count_))
			y4_ = b + r * np.sin(degree1)*np.random.rand(len(count_))
			print("##########")
			print(type(x4_))
			print(len(x4_))
			# print(x4_)
			if len(x4) == 0:
				x4.append(x4_[0])
				y4.append(y4_[0])
				judge = 1
			else:
				count_1 = 0
				for l in range(len(x4)):

					num = pow(pow((x4_[0] - x4[l]),2) + pow((y4_[0] - y4[l]),2),0.5)
					print("##########****************")
					print(num)

					if num > 2.5:
						count_1 += 1

						# x4.append(x4_[0])
						# y4.append(y4_[0])
						# judge = 1
						# break

				if count_1 == len(x4) - 1:
					judge = 1
					x4.append(x4_[0])
					y4.append(y4_[0])
	print("****************")
	print(len(x4))
	print(x4)


				



	# x4 = a + r * np.cos(degree)*np.random.rand(len(tem_list)) - 0.2
	# y4 = b + r * np.sin(degree)*np.random.rand(len(tem_list)) - 0.2
	# print(data_list[a][0])

	# plt.plot(x3,y3)
	plt.scatter(x4,y4,c=co[u],s=10,alpha=0.4,marker='o')#散点图
	plt.plot(x3,y3,color='blue')

	for q in range(len(x4)):
		plt.text(x4[q],y4[q],tem_list[q],family='serif',style='italic', ha='right', wrap=True,fontsize=7)
	
	# count = count + 1
	a = a + 7#调圆心，使圆之间正常显示，根据圆的数量，即一共多少个集合#####
	count = count + 1
	if count % n == 0:#每画4个圆调整一次a的值
		a = a - n*7
		b = b + 7
plt.xticks([])  #去掉横坐标值
plt.yticks([])  #去掉纵坐标值
# plt.axis('off')
plt.show()
# plt.savefig('figure2.png',bbox_inches='tight')

db.close()