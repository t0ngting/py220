a=1;b=2;c=3;d=4
math=[1,2,3,4]
math.append(5)#尾巴加5
print(math)
math.insert(2,6)#陣列2位置新增6
print(math)
del math[0:2]#2刪除0到2(不包含2
print(math)
del math[-2]#刪除倒數第兩個-
print(math)
print(3 in math)#布林值
print(math.count(3)) #計算3在陣列的個數
chinese=['x','y']
print(math+chinese)#用加號把陣列串聯
ls=[[0,1],[2,3]]
print(ls[1][0])#前面讀最外層後面是第二層以此類推
print(sorted(math))#sorted由小到大
#實作1
grade=[[5,14,7],[23,36,28],[88,80,92]]
print(grade[2])
print(sum(grade[0])/len(grade[0]),sum(grade[1])/len(grade[1]),sum(grade[2])/len(grade[2]))
grade.insert(3,[94,90,96])
print(grade)