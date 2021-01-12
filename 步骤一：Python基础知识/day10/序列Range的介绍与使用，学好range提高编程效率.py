#创建数字序列
r1 = range(10,20)
print(r1)   #range(10, 20)
#why:为什么不直接输出10到20之间的数字呢。
'''
只有在使用这个变量的时候，才会进行相应的处理和解析
这样做的好处是节省内存，在程序运行的时候，用到什么数字，去什么数字
不会产生额外的存储，这是他的优势所在
'''
#查看r1的类型
print(type(r1)) #<class 'range'>

#range的取值操作
print(r1[9]) #19
#print(r1[10]) #IndexError: range object index out of range ,报错，范围越界，r1中没有第10个数字

#获取连续的取值范围
print(r1[3:5]) #将索引值为3，为4的索引值提取出来 range(13, 15)
#没有输出13,14，因为它新建了一个range对象，只要用范围取值都会新建，可见是极为节省内存

#增加步长
r2 = range(10,20,2)
print(r2) #range(10, 20, 2)
print(r2[4])    #18
print(r2[0:2]) #range(10, 14, 2) 重新创建了一个range对象
#对于range函数一旦创建就不变了
#r2[4] = 20 #TypeError: 'range' object does not support item assignment 不可修改的提示

#成员运算符 in 在所有的数据结构中通用
print(12 in range(10,20)) #Ture
print(22 not in range(10,20)) #Ture




