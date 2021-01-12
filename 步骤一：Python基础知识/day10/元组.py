#元组运算符
t1 = (5,6,7) + (8,9,10)
print(t1)
#对于元组运算符，创建一个新的元组保存数据和原始数据无关
#即使修改了原始数据也不会产生任何变化，也就是t1的数据，和两个相加的元素是无关的

#使用称号，就是讲元素乘以输出
t2 = ('see','you') * 2
print(t2)

#元组的使用
#创建
t = ('a','b','c',1,2,3)
tt = 'a','b','c',1,2,3 #不加括号，用逗号进行分割
print(t)
print(tt)
print(type(tt)) #查看数据类型 <class 'tuple'>

#获取数据时，与列表完全相同
print(t[5]) #正序索引获取列表的第六个元素  3
print(t[-1]) #倒序索引，获取倒数第一个  3
print(t[1:4]) #范围取值，左闭右开    ('b', 'c', 1)
print('b' in t ) #成员运算符，判断b是否存在t中 True

#元组在创建后内容不可变
#t[0] = 2 #TypeError: 'tuple' object does not support item assignment
        #元组对象不支持重新分配
print(t)

#写入数据的函数同样不被支持
#t.append('f')  #AttributeError: 'tuple' object has no attribute 'append'
 #同样不被支持
#t.insert('f')
print(t)

#如果元组内持有列表，那么列表的内容是允许修改的
t2 = (['张三',38,5000],['李四',28,2000])
item = t2[0]
print(item) #['张三', 38, 5000]
#此时item是一个列表
item[1] = 40 #修改第二个元素
print(item) #['张三', 40, 5000]
#pop按照索引值删除函数，这个在元组中不被支持
'''
t2.pop(0) 
print(t2) #AttributeError: 'tuple' object has no attribute 'pop' 元组对象没有pop属性
'''
#元组运算符
t3 = (1,2,3) + (4,5,6)
print(t3)   #(1, 2, 3, 4, 5, 6)
t4 = ('see','you') *2
print(t4)   #('see', 'you', 'see', 'you')
#如果元组只有元素时，必须要在这个元素后增加逗号，说明这个一个元组
t5 = ('see') *5
print(t5)   #seeseeseeseesee
t6 = ('see',) *5
print(t6)   #('see', 'see', 'see', 'see', 'see')

#对于元组来说，我不管你中间有几个元素，我只认如果括号中存在逗号，那就是
#一个元组，如果没有逗号，我认为这个小括号就只是简单的算术优先级的符号，只会对这里面的
#元素进行一个优先运算，输出字符串

#元组运算符同样适合列表
t7 = [1,2,3] +[5,6,7]
print(t7)  #[1, 2, 3, 5, 6, 7]
t8 = (1,2,3) +[5,6,7] #不同类型的元组加上列表就会报错
print(t8)












